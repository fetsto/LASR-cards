#!/usr/bin/env python3
"""
Script to generate a markdown file from LASR card JSON files.
Usage: python generate_cards_md.py <language> <deck> [output_file]
"""

import json
import sys
from pathlib import Path
from typing import List, Dict


# Configuration: Define deck locations and titles
DECK_CONFIG = {
    "main-deck": {
        "path": "main-deck",
        "titles": {
            "EN": "LASR Cards - Software Development Risks",
            "DE": "LASR-Karten - Risiken der Softwareentwicklung"
        }
    },
    "AI-coding": {
        "path": "booster-packs/agentic-software-development",
        "subdirs": {"EN": "cards", "DE": "cards"},
        "titles": {
            "EN": "LASR Cards - Agentic Software Development Booster Pack",
            "DE": "LASR-Karten - Agentic Software Development Booster Pack"
        }
    }
}


def load_card(filepath: Path) -> Dict:
    """Load a single card from a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_chapter_number(cards: List[Dict], category: str) -> int:
    """Extract chapter number from the first card in a category."""
    for card in cards:
        if card.get('category') == category:
            number = card.get('number', '')
            if number and '.' in number:
                try:
                    return int(number.split('.')[0])
                except ValueError:
                    pass
    return 999


def sort_cards(cards: List[Dict]) -> List[Dict]:
    """Sort cards by chapter number (extracted from card number) and card number."""
    def sort_key(card):
        number = card.get('number', '')
        chapter = 999
        if number and '.' in number:
            try:
                chapter = int(number.split('.')[0])
            except ValueError:
                pass
        return (chapter, number)
    return sorted(cards, key=sort_key)


def generate_markdown_main_deck(cards: List[Dict], output_file: Path, title: str):
    """Generate markdown for main deck with chapter-organized categories."""

    # Sort cards
    cards = sort_cards(cards)

    # Group by category
    categories = {}
    for card in cards:
        category = card.get('category', 'Uncategorized')
        if category not in categories:
            categories[category] = []
        categories[category].append(card)

    # Create a mapping of category to chapter number
    category_chapters = {}
    for category in categories.keys():
        chapter_num = get_chapter_number(cards, category)
        category_chapters[category] = chapter_num

    # Sort categories by chapter number
    sorted_categories = sorted(categories.keys(), key=lambda cat: category_chapters[cat])

    # Generate markdown
    with open(output_file, 'w', encoding='utf-8') as f:
        # Title
        f.write(f"# {title}\n\n")

        # Table of contents
        f.write("## Table of Contents\n\n")
        for category in sorted_categories:
            chapter = category_chapters[category]
            chapter_prefix = f"{chapter}. " if chapter != 999 else ""
            anchor = f"{chapter}-{category.lower().replace(' ', '-').replace('&', '')}" if chapter != 999 else category.lower().replace(' ', '-').replace('&', '')
            f.write(f"- [{chapter_prefix}{category}](#{anchor})\n")
            for card in categories[category]:
                number = card.get('number', '')
                card_title = card.get('title', '')
                f.write(f"  - [{number} {card_title}](#{number.replace('.', '')}-{card_title.lower().replace(' ', '-').replace(',', '').replace('&', '').replace('(', '').replace(')', '').replace('/', '')})\n")
        f.write("\n---\n\n")

        # Cards by category
        for category in sorted_categories:
            chapter = category_chapters[category]
            chapter_prefix = f"{chapter}. " if chapter != 999 else ""
            f.write(f"## {chapter_prefix}{category}\n\n")

            for card in categories[category]:
                number = card.get('number', '')
                card_title = card.get('title', '')
                description = card.get('description', '')

                f.write(f"### {number} {card_title}\n\n")
                f.write(f"{description}\n\n")
                f.write("---\n\n")


def generate_markdown_booster(cards: List[Dict], output_file: Path, title: str):
    """Generate markdown for booster packs with categories shown per card."""

    # Sort cards by card number
    cards = sorted(cards, key=lambda x: x.get('number', ''))

    # Generate markdown
    with open(output_file, 'w', encoding='utf-8') as f:
        # Title
        f.write(f"# {title}\n\n")

        # Table of contents
        f.write("## Table of Contents\n\n")
        for card in cards:
            number = card.get('number', '')
            card_title = card.get('title', '')
            anchor = f"{number.replace('.', '').replace('-', '').lower()}-{card_title.lower().replace(' ', '-').replace(',', '').replace('&', '').replace('(', '').replace(')', '').replace('/', '')}"
            f.write(f"- [{number} {card_title}](#{anchor})\n")
        f.write("\n---\n\n")

        # Cards without category grouping
        for card in cards:
            number = card.get('number', '')
            card_title = card.get('title', '')
            category = card.get('category', 'Uncategorized')
            description = card.get('description', '')

            f.write(f"## {number} {card_title}\n\n")
            f.write(f"**Category:** {category}\n\n")
            f.write(f"{description}\n\n")
            f.write("---\n\n")


def main():
    """Main function to process cards and generate markdown."""

    if len(sys.argv) < 3:
        print("Usage: python generate_cards_md.py <language> <deck> [output_file]")
        print("\nArguments:")
        print("  language: EN or DE")
        print("  deck:     main-deck, AI-coding, etc.")
        print("\nAvailable decks:")
        for deck_name in DECK_CONFIG.keys():
            print(f"  - {deck_name}")
        print("\nExamples:")
        print("  python generate_cards_md.py EN main-deck")
        print("  python generate_cards_md.py DE main-deck")
        print("  python generate_cards_md.py EN AI-coding")
        print("  python generate_cards_md.py DE AI-coding output.md")
        sys.exit(1)

    language = sys.argv[1].upper()
    deck_name = sys.argv[2]

    if language not in ["EN", "DE"]:
        print(f"Error: Language must be 'EN' or 'DE', got '{language}'")
        sys.exit(1)

    if deck_name not in DECK_CONFIG:
        print(f"Error: Unknown deck '{deck_name}'")
        print(f"Available decks: {', '.join(DECK_CONFIG.keys())}")
        sys.exit(1)

    # Build the input directory path
    deck_config = DECK_CONFIG[deck_name]
    input_dir = Path(deck_config["path"]) / language

    # Add subdirectory if specified in config
    if "subdirs" in deck_config and language in deck_config["subdirs"]:
        input_dir = input_dir / deck_config["subdirs"][language]

    if not input_dir.exists() or not input_dir.is_dir():
        print(f"Error: Directory '{input_dir}' does not exist")
        sys.exit(1)

    # Determine output file
    if len(sys.argv) >= 4:
        output_file = Path(sys.argv[3])
    else:
        output_file = input_dir / "LASR-cards.md"

    # Load all JSON files
    cards = []
    json_files = sorted(input_dir.glob("*.json"))

    if not json_files:
        print(f"No JSON files found in '{input_dir}'")
        sys.exit(1)

    print(f"Found {len(json_files)} card files in {input_dir}")

    for json_file in json_files:
        try:
            card = load_card(json_file)
            cards.append(card)
            print(f"  Loaded: {json_file.name}")
        except Exception as e:
            print(f"  Error loading {json_file.name}: {e}")

    if not cards:
        print("No cards were successfully loaded")
        sys.exit(1)

    # Get title from config
    title = deck_config["titles"].get(language, "LASR Cards")

    # Generate markdown - use different format for booster packs
    is_booster = deck_name != "main-deck"

    if is_booster:
        generate_markdown_booster(cards, output_file, title)
    else:
        generate_markdown_main_deck(cards, output_file, title)

    print(f"\nMarkdown file generated: {output_file}")
    print(f"Total cards: {len(cards)}")


if __name__ == "__main__":
    main()
