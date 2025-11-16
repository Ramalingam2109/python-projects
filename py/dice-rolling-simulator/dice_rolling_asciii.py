"""
Dice Rolling Simulator with ASCII Art
A fun command-line tool that simulates rolling dice with visual ASCII representation.
"""

import random

# ASCII art representation of dice faces
DICE_ART = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


def roll_dice(num_dice):
    """Roll dice and return list of results."""
    return [random.randint(1, 6) for _ in range(num_dice)]


def display_dice(dice_values):
    """Display dice in horizontal layout using ASCII art."""
    for line in range(5):
        for die in dice_values:
            print(DICE_ART[die][line], end="  ")
        print()


def main():
    """Main function to run the dice rolling simulator."""
    try:
        number_of_dice = int(input("How many dice are you rolling? "))
        if number_of_dice <= 0:
            print("Please enter a positive number.")
            return
        
        dice = roll_dice(number_of_dice)
        print("\nDice Results:")
        display_dice(dice)
        
        total = sum(dice)
        print(f"\nTotal: {total}")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        print("\n\nExiting...")


if __name__ == "__main__":
    main()