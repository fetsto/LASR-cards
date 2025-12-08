# LASR Cards Markdown Generator

This script converts LASR card JSON files into a formatted markdown document.

## Usage

```bash
python3 generate_cards_md.py <input_directory> [output_file]
```

### Arguments

- `input_directory` (required): Path to the directory containing the card JSON files
- `output_file` (optional): Path for the output markdown file. If not specified, the file will be created as `LASR-cards.md` in the input directory

### Examples

Generate markdown for English cards (output to default location):
```bash
python3 generate_cards_md.py ENG/LASR-cards-MAIN
```

Generate markdown for German cards with custom output path:
```bash
python3 generate_cards_md.py DE/LASR-Karten-MAIN output/german-cards.md
```

Specify custom output file:
```bash
python3 generate_cards_md.py ENG/LASR-cards-MAIN docs/cards.md
```

## Output Format

The generated markdown file includes:

1. **Title** - Automatically determined based on the input directory (English/German)
2. **Table of Contents** - Organized by category with links to each card
3. **Card Details** - Each card displays:
   - Card number and title
   - Category
   - Description

Cards are automatically sorted by category and number.

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
