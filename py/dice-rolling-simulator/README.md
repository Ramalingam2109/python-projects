# 🎲 Dice Rolling Simulator

A fun command-line tool that simulates rolling dice with beautiful ASCII art representation. Roll multiple dice and see the results displayed horizontally.

## Features

- ✨ Beautiful ASCII art dice visualization
- 🎯 Support for rolling multiple dice at once
- 📊 Automatic total calculation
- ✅ Input validation and error handling
- 🎮 Simple and intuitive interface

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

No installation required! Just download the file and run it.

**Note**: This project has a `requirements.txt` file that confirms no external dependencies are needed.

## Usage

```bash
python dice_rolling_asciii.py
```

### Example Output

```
How many dice are you rolling? 3

Dice Results:
┌─────────┐  ┌─────────┐  ┌─────────┐
│  ●   ●  │  │ ●       │  │  ●   ●  │
│    ●    │  │    ●    │  │  ●   ●  │
│  ●   ●  │  │       ● │  │  ●   ●  │
└─────────┘  └─────────┘  └─────────┘

Total: 14
```

## How It Works

1. The program prompts you to enter the number of dice you want to roll
2. It generates random numbers (1-6) for each die
3. Displays the dice using ASCII art in a horizontal layout
4. Calculates and displays the total sum

## Code Structure

- `DICE_ART`: Dictionary containing ASCII art for each die face (1-6)
- `roll_dice(num_dice)`: Generates random dice values
- `display_dice(dice_values)`: Displays dice in horizontal layout
- `main()`: Main program loop with input validation

## Customization

You can easily customize:
- Dice appearance by modifying the `DICE_ART` dictionary
- Number range (currently 1-6)
- Display format

## Error Handling

The program handles:
- Invalid input (non-numeric values)
- Zero or negative numbers
- Keyboard interrupts (Ctrl+C)

## License

This project is open source and available for educational purposes.

---

**Enjoy rolling dice! 🎲**

