#!/usr/bin/env python3
"""
Script to generate a markdown file from LASR card JSON files.
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict


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


def get_category_order(category: str) -> int:
    """Return sort order for categories."""
    categories = {
        "Solution Approach": 1,
        "Knowledge and Tooling": 2,
        "Goals and Expectations": 3,
        "External Systems": 4,
        "Current Solution": 5,
        "Organization": 6,
        "Deployment and Operations": 7,
        "Team and Communication": 8
    }
    return categories.get(category, 999)


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


def generate_markdown(cards: List[Dict], output_file: Path, title: str = "LASR Cards"):
    """Generate a markdown file from the cards."""

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


def main():
    """Main function to process cards and generate markdown."""

    if len(sys.argv) < 2:
        print("Usage: python generate_cards_md.py <input_directory> [output_file]")
        print("\nExample:")
        print("  python generate_cards_md.py ENG/LASR-cards-MAIN")
        print("  python generate_cards_md.py ENG/LASR-cards-MAIN output.md")
        sys.exit(1)

    input_dir = Path(sys.argv[1])

    if not input_dir.exists() or not input_dir.is_dir():
        print(f"Error: '{input_dir}' is not a valid directory")
        sys.exit(1)

    # Determine output file
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])
    else:
        output_file = input_dir / "LASR-cards.md"

    # Load all JSON files
    cards = []
    json_files = sorted(input_dir.glob("*.json"))

    if not json_files:
        print(f"No JSON files found in '{input_dir}'")
        sys.exit(1)

    print(f"Found {len(json_files)} card files")

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

    # Determine title based on directory
    if "ENG" in str(input_dir):
        title = "LASR Cards - Software Development Risks"
    elif "DE" in str(input_dir):
        title = "LASR-Karten - Risiken der Softwareentwicklung"
    else:
        title = "LASR Cards"

    # Generate markdown
    generate_markdown(cards, output_file, title)
    print(f"\nMarkdown file generated: {output_file}")
    print(f"Total cards: {len(cards)}")


if __name__ == "__main__":
    main()
