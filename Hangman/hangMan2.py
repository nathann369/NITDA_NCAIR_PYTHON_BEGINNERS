import random


def load_words(filename):
    with open(filename, 'r') as f:
        words = f.read().splitlines()
    return [word.strip().lower() for word in words if word.strip()]
def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def play(word_list):
    word = choose_word(word_list)
    # word_completion = "_" * len(word_list)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    #print("You have"  {tries}  "lives")
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 :
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                print(tries)
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word)
                indices = [i for i, letter in enumerate(word_list) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word = "".join(word_as_list)
                if "_" not in word:
                    guessed = True
        elif len(guess) == len(word_list):
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word_list:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word = word_list
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = load_words("words.txt")
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = load_words(f"ilename")
        play(word)


if __name__ == "__main__":
    main()