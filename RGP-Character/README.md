# RPG Character Creator

> ⚠️ **Work in Progress** — This project is still under development.

A simple command-line tool for creating RPG characters with visual stat bars.

## Usage

Run the script and follow the prompts:

```bash
python RGP_Character.py
```

You will be asked to enter:
- **Character name**
- **Strength**
- **Intelligence**
- **Charisma**

### Example

```
Enter a character name: Aragorn
Enter the character strength: 3
Enter the character intelligence: 2
Enter the character charisma: 2
```

**Output:**
```
Aragorn
STR ●●●○○○○○○○
INT ●●○○○○○○○○
CHA ●●○○○○○○○○
```

## Rules

### Name
- Must be a string
- Cannot be empty
- Maximum 10 characters
- No spaces allowed

### Stats (Strength, Intelligence, Charisma)
- Each stat must be an integer between 1 and 4 (inclusive)
- The three stats must add up to exactly **7 points**
