# LASR Cards Repository

A curated repository for managing the **LASR cards**—supporting tools for the **Lightweight Approach for Software Reviews (LASR)** method.

## What is LASR?

LASR (Lightweight Approach for Software Reviews) is a streamlined, community-driven method for performing fast and effective software and architecture reviews. It empowers small teams (often 3–4 people) to identify the most critical quality attributes and risks efficiently—typically within just a few hours. The method is accessible, flexible, and free to use, even in commercial contexts.

### Key Features of LASR:
- **Lean and fast**: Initial results are available after a half-day workshop.
- **Accessible**: No extensive training or documentation required; anyone curious can get started.
- **Engaging method**: Uses a gamified, card-based moderation style to facilitate discussion and decision-making.
- **Supportive toolset**: Includes downloadable templates, checklists, cheat sheets, and the all-important LASR cards (available as “Print & Play”).

Visit the official LASR site for more details: https://www.lasr-reviews.org/

---

## Why This Repository Exists

This repository is dedicated to maintaining and organizing the **LASR card decks** in multiple languages and extending their utility through additional packs and themed boosters.

### What’s Inside:
- **Core LASR card decks**, currently available in English and German.
- **Booster packs** targeting different domains (e.g., performance, security, usability).
- **Language variants** for broader adoption and accessibility.

### Objectives:
- Ensure **consistent updates** and version control for LASR cards.
- Provide a centralized location for **translations**, **localized content**, and domain-specific enhancements.
- Enable **community contributions**—anyone can add new languages or booster sets via pull requests.
- Facilitate usage in both physical workshops and digital workshops (printable PDFs, Miro/Mural-compatible formats).

---

## Getting Started

### 1. Browse the Cards
The repository is organized as follows:

**Main Deck:**
- `main-deck/EN/` — English base deck (32 core risk cards)
- `main-deck/DE/` — German base deck (32 core risk cards)

**Booster Packs:**
- `booster-packs/agentic-software-development/` — Cards addressing risks specific to AI agent-based development (alias: **AI-coding**)
  - `EN/cards/` — English booster cards
  - `DE/cards/` — German booster cards 

### 2. Generate Markdown Documentation
The repository includes a Python script to generate formatted markdown files from the JSON card data:

```bash
python3 generate_cards_md.py <language> <deck> [output_file]
```

**Examples:**
```bash
# Generate English main deck cards
python3 generate_cards_md.py EN main-deck

# Generate German main deck cards
python3 generate_cards_md.py DE main-deck

# Generate AI coding booster pack
python3 generate_cards_md.py EN AI-coding
python3 generate_cards_md.py DE AI-coding
```

The generated markdown includes:
- Table of contents with chapter-organized categories
- All cards sorted by chapter and number
- Clean, readable format suitable for documentation

See [README-SCRIPT.md](README-SCRIPT.md) for detailed usage instructions.

### 3. Contribute
- **Translations**: Add a new language folder under `main-deck/<LANG>/` or `booster-packs/<pack-name>/<LANG>/` with the translated card files.
- **Boosters**: Submit new domain-specific booster packs under `booster-packs/<pack-name>/` with `EN/` and `DE/` subdirectories.
- All contributions should follow the established naming and formatting conventions (JSON format with `number`, `title`, `category`, and `description` fields).

---

## Usage & Workshop Workflow

1. **Select quality attributes** for the review using “Top-5 Challenger” cards.
2. **Define target levels** (0–100 scale), creating the green baseline in the LASR spider chart.
3. **Identify risks** using risk cards and plot your system’s current standing against targets.
4. **Explore deeper analysis**, optionally using additional booster or extension cards to refine focus areas.
5. Use **cheat sheet** and process diagrams for guidance during the workshop.

---

## Resources

- Official LASR website: [lasr-reviews.org](https://www.lasr-reviews.org/)
- LASR community (download area for cards and templates): LASR Community
- FAQ about LASR, including access to materials and print-on-demand options

---

## Licensing & Acknowledgements

- LASR is freely available under an open license—materials may be used in commercial and non-commercial settings.
- Thank you to **Stefan Toth** and **Stefan Zörner** for developing LASR, and to **embarc** for their support.

---

## Contact & Community

Questions or ideas? Reach out via the contact options on the LASR site—especially for download issues or community support.