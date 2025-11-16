"""
Hangman Game
A classic word guessing game where players try to guess a word letter by letter.
"""

import random

WORDS = ["python", "programming", "hangman", "challenge", "developer", "algorithm",
         "computer", "software", "function", "variable", "dictionary", "list"]


def choose_random_word():
    """Select a random word from the word list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed and others as underscores."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def play_again(score, failed_attempts):
    """Ask the player if they want to play another game."""
    choice = input("\nEnter Y or Enter to play again, or any other key to quit: ").lower().strip()
    if choice not in ("y", ""):
        print(f"\nFinal Score: {score} wins out of {score + failed_attempts} games.")
        return False
    return True


def get_player_input(guessed_letters):
    """Get valid letter input from the player."""
    while True:
        guess = input("Enter a letter to guess: ").lower().strip()
        if guess in guessed_letters:
            print("This letter is already guessed.")
        elif len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Please enter a valid single alphabet.")


def play_game():
    """Main game loop."""
    user_name = input("Enter your name: ").strip() or "Player"
    failed_attempts = 0
    score = 0
    game = True

    while game:
        print(f"\n{'='*50}")
        print(f"Welcome to Hangman, {user_name}!")
        print(f"{'='*50}\n")
        
        word = choose_random_word()
        attempts = 6
        guessed_letters = set()

        while attempts > 0:
            print(f"\nWord: {display_word(word, guessed_letters)}")
            print(f"Attempts remaining: {attempts}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

            player_guess = get_player_input(guessed_letters)
            guessed_letters.add(player_guess)

            if player_guess not in word:
                attempts -= 1
                print(f"❌ Incorrect! The letter '{player_guess}' is not in the word.")
                if attempts == 0:
                    print(f"\n💀 Game Over, {user_name}!")
                    print(f"The word was: {word}")
                    failed_attempts += 1
                    if not play_again(score, failed_attempts):
                        game = False
                    break
            else:
                print(f"✅ Correct! The letter '{player_guess}' is in the word.")
                
                # Check if word is complete
                if "_" not in display_word(word, guessed_letters):
                    print(f"\n🎉 Congratulations, you won, {user_name}!")
                    print(f"The word was: {word}")
                    score += 1
                    if not play_again(score, failed_attempts):
                        game = False
                    break


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nExiting game...")
