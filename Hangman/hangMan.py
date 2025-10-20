import random

def load_words(filename):
    with open(filename, 'r') as f:
        words = f.read().splitlines()
    return [word.strip().lower() for word in words if word.strip()]

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game(word_list):
    word = choose_word(word_list)
    guessed_letters = set()
    lives = 6

    print("\nWelcome to Hangman!")
    print("\nNote words are a random list of programing languages")
    print(f"The word has {len(word)} letters.")

    while lives > 0:
        
        print("\n" + display_word(word, guessed_letters))
        print(f"Lives left: {lives}")
        guess = input("Guess a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    if lives == 0:
        print(f"\nGame Over! The word was: {word}")

def main():
    word_list = load_words('words.txt')
    if not word_list:
        print("The word list is empty. Please check 'words.txt'.")
        return

    while True:
        play_game(word_list)
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again == 'y':
            play_game(word_list)
        else:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
