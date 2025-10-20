import os
import json
import random
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Word API
WORD_API: str = "https://random-word-api.herokuapp.com/word?"

# Account storage
ACCOUNTS_FILE = "accounts_data/accounts.json"
os.makedirs("accounts_data", exist_ok=True)

# Hangman stages with emojis
HANGMAN_PICS = [
    """
     😁
     ┌───┐
     │
     │
     │
     │
    ==========
    """,
    """
     😯
     ┌───┐
     │   😯
     │
     │
     │
    ==========
    """,
    """
     😟
     ┌───┐
     │   😟
     │   👕
     │
     │
    ==========
    """,
    """
     😢
     ┌───┐
     │   😢
     │   👕
     │   🦵
     │
    ==========
    """,
    """
     😵
     ┌───┐
     │   😵
     │   👕
     │   🦵🦵
     │
    ==========
    """
]

# Rainbow intro
def rainbow_text(text: str) -> str:
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    return "".join(colors[i % len(colors)] + c for i, c in enumerate(text)) + Style.RESET_ALL


def load_accounts() -> dict:
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, "r") as f:
        return json.load(f)


def save_accounts(accounts: dict) -> None:
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=4)


def retrieve_word(length: int = 6) -> str:
    """Fetch a random word from the API."""
    while True:
        try:
            response = requests.get(f"{WORD_API}length={length}", timeout=5)
            if response.ok:
                return response.json()[0].upper()
        except Exception:
            # fallback if API fails
            return random.choice(["PYTHON", "HANGMAN", "DEVELOPER", "COMPUTER"])


def play_hangman(word: str, max_attempts: int) -> bool:
    word = word.upper()
    guessed_letters: set[str] = set()
    correct_guesses: list[str] = []
    incorrect_guesses: list[str] = []

    attempts_left = max_attempts
    display_word = ["_" for _ in word]

    while attempts_left > 0 and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print(Fore.GREEN + "✅ Correct guesses: " + ", ".join(correct_guesses) if correct_guesses else "✅ Correct guesses: None")
        print(Fore.RED + "❌ Incorrect guesses: " + ", ".join(incorrect_guesses) if incorrect_guesses else "❌ Incorrect guesses: None")
        all_guesses = correct_guesses + incorrect_guesses
        print(Fore.CYAN + "🔠 All guesses: " + ", ".join(all_guesses) if all_guesses else "🔠 All guesses: None")
        print(Style.RESET_ALL)

        guess = input("Enter a letter: ").upper().strip()

        if guess in ("QUIT", "EXIT"):
            print(Fore.YELLOW + "Exiting game early...")
            return False

        if len(guess) != 1 or not guess.isalpha():
            print(Fore.YELLOW + "⚠ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(Fore.YELLOW + f"⚠ You already guessed '{guess}'. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(Fore.GREEN + f"✅ Good job! '{guess}' is in the word.")
            correct_guesses.append(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
        else:
            print(Fore.RED + f"❌ Sorry, '{guess}' is not in the word.")
            incorrect_guesses.append(guess)
            attempts_left -= 1
            stage = len(HANGMAN_PICS) - attempts_left - 1
            stage = min(stage, len(HANGMAN_PICS) - 1)
            print(HANGMAN_PICS[stage])
            print(Fore.MAGENTA + f"Remaining attempts: {attempts_left}")

    if "_" not in display_word:
        print(Fore.GREEN + f"\n🎉 Congratulations! You guessed the word: {word}")
        return True
    else:
        print(Fore.RED + f"\n💀 Game Over! The word was: {word}")
        return False


def main():
    print(rainbow_text("WELCOME TO HANGMAN"))
    print("Enter ('quit'/'exit') at any time to quit.")
    accounts = load_accounts()

    name = input("Enter your name: ").strip()
    if not name:
        name = "Guest"

    if name not in accounts:
        accounts[name] = {"wins": 0, "losses": 0, "plays": 0}

    user = accounts[name]
    print(f"\n👤 Player: {name}")
    print(f"🏆 Wins: {user['wins']} | ❌ Losses: {user['losses']} | 🎮 Plays: {user['plays']}")

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Quick Game")
        print("2. Quit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\nSelect difficulty:")
            print("1. Beginner (7 lives)")
            print("2. Regular (5 lives)")
            print("3. Professional (3 lives)")
            diff = input("Choice: ").strip()

            if diff == "1":
                attempts = 7
                word_length = random.randint(4, 6)
            elif diff == "2":
                attempts = 5
                word_length = random.randint(6, 8)
            elif diff == "3":
                attempts = 3
                word_length = random.randint(8, 10)
            else:
                print(Fore.YELLOW + "⚠ Invalid choice, defaulting to Regular.")
                attempts = 5
                word_length = 6

            word = retrieve_word(word_length)
            result = play_hangman(word, attempts)

            accounts[name]["plays"] += 1
            if result:
                accounts[name]["wins"] += 1
            else:
                accounts[name]["losses"] += 1
            save_accounts(accounts)

        elif choice == "2":
            print(Fore.CYAN + "👋 Goodbye!")
            break
        else:
            print(Fore.YELLOW + "⚠ Invalid option, try again.")


if __name__ == "__main__":
    main()
