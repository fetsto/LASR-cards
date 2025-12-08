# LASR Cards Markdown Generator

This script converts LASR card JSON files into a formatted markdown document.

## Usage

```bash
python3 generate_cards_md.py <language> <deck> [output_file]
```

### Arguments

- `language` (required): Language code - `EN` or `DE`
- `deck` (required): Deck identifier - `main-deck`, `AI-coding`, etc.
- `output_file` (optional): Path for the output markdown file. If not specified, the file will be created as `LASR-cards.md` in the deck's directory

### Available Decks

The script includes built-in configuration for the following decks:
- `main-deck` - Core LASR risk cards for software development
- `AI-coding` - Agentic Software Development booster pack

New decks can be added by editing the `DECK_CONFIG` dictionary in the script.

### Examples

Generate markdown for English main deck cards:
```bash
python3 generate_cards_md.py EN main-deck
```

Generate markdown for German main deck cards:
```bash
python3 generate_cards_md.py DE main-deck
```

Generate markdown for AI coding booster pack:
```bash
python3 generate_cards_md.py EN AI-coding
python3 generate_cards_md.py DE AI-coding
```

Specify custom output file:
```bash
python3 generate_cards_md.py EN main-deck docs/english-cards.md
```

## Output Format

The generated markdown file includes:

1. **Title** - Automatically determined based on the input directory (English/German, main deck/booster pack)
2. **Table of Contents** - Organized by chapter-numbered categories with links to each card
3. **Card Details** - Each card displays:
   - Card number and title
   - Description

Cards are automatically sorted by chapter number and card number within each chapter.

## Card JSON Format

Each card JSON file should have the following structure:

```json
{
  "number": "3.3",
  "title": "No direct contact with customers or users",
  "category": "Goals and Expectations",
  "description": "Is product development lacking direct costumer feedback? Are customer needs, stakeholder interests or usage patterns of the solution unclear, ambiguous or based on hearsay?"
}
```

## Categories

The script recognizes the following categories (in order):

1. Solution Approach
2. Knowledge and Tooling
3. Goals and Expectations
4. External Systems
5. Current Solution
6. Organization
7. Deployment and Operations
8. Team and Communication
