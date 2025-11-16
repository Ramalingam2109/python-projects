# 🎮 Hangman Game

A classic word guessing game where players try to guess a word letter by letter. Features score tracking, multiple rounds, and a user-friendly interface.

## Features

- 🎯 Random word selection from a curated list
- ⏱️ 6 attempts per game
- 📊 Score tracking across multiple games
- 🔄 Multiple game rounds support
- ✅ Input validation (single letters only)
- 🎨 User-friendly interface with emojis
- 📝 Shows guessed letters and remaining attempts

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

No installation required! Just download the file and run it.

**Note**: This project has a `requirements.txt` file that confirms no external dependencies are needed.

## Usage

```bash
python hangman.py
```

### Gameplay

1. Enter your name when prompted
2. Try to guess the word letter by letter
3. You have 6 incorrect guesses before the game ends
4. Win by guessing all letters correctly
5. Play multiple rounds and track your score

### Example Output

```
Enter your name: Player

==================================================
Welcome to Hangman, Player!
==================================================

Word: _ _ _ _ _ _
Attempts remaining: 6
Guessed letters: None
Enter a letter to guess: a
✅ Correct! The letter 'a' is in the word.

Word: _ a _ _ _ _
Attempts remaining: 6
Guessed letters: a
Enter a letter to guess: e
❌ Incorrect! The letter 'e' is not in the word.
```

## Word List

The game includes words like:
- python
- programming
- hangman
- challenge
- developer
- algorithm
- computer
- software
- function
- variable
- dictionary
- list

## How It Works

1. **Word Selection**: Randomly selects a word from the word list
2. **Letter Guessing**: Player guesses one letter at a time
3. **Validation**: Checks if the letter is in the word
4. **Score Tracking**: Tracks wins and losses
5. **Replay**: Option to play again after each game

## Code Structure

- `WORDS`: List of words to guess
- `choose_random_word()`: Selects a random word
- `display_word()`: Shows word with guessed letters revealed
- `get_player_input()`: Validates and gets letter input
- `play_game()`: Main game loop
- `play_again()`: Handles replay functionality

## Customization

You can easily customize:
- Add more words to the `WORDS` list
- Change the number of attempts (modify `attempts = 6`)
- Modify the word list difficulty

## Error Handling

The program handles:
- Invalid input (numbers, multiple letters, special characters)
- Already guessed letters
- Keyboard interrupts (Ctrl+C)

## Tips for Players

- Start with common vowels (a, e, i, o, u)
- Look for common letter patterns
- Keep track of guessed letters
- Use process of elimination

## License

This project is open source and available for educational purposes.

---

**Have fun playing Hangman! 🎯**

