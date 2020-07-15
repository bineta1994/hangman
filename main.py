#these lines import the randon library and the words_list funtion. The words list function contains the words for the game
import random
from words import word_list

# this function returns a word for the game. It returns the words in uppercase.
def get_word():
    word = random.choice(word_list)
    return word.upper()

#this function runs condtionals to see if the letters entered is in the words. It keeps track of the number of tries, users have
# a maximum of 6 tries. The function also has a statement checking if the characters entered are alpahbets and also checks if the length of the guessed word is the same length of the actual word from the game. 
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters: #checks if the letter has already been guessed and prints it out.
                print("You already guessed the letter", guess)
            elif guess not in word: # otherwise if the letter is not in the word it prints out a statement.
                print(guess, "is not in the word.")
                tries -= 1 #reduces the number of tries  by 1
                guessed_letters.append(guess) #this appends guess to guessed_letters.
            else:
                print("Good job,", guess, "is in the word!") #this block is if the guess is in the word.
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess] 
                for index in indices:
                    word_as_list[index] = guess #replaces each underscore with guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words: # checks if the guess has already been guessed
                print("You already guessed the word", guess)
            elif guess != word: #this statement checks if the guess is not in the word
                print(guess, "is not the word.")
                tries -= 1 #reduces the number of tries by 1
                guessed_words.append(guess) 
            else: #if the user correctly guesses the word and sets word_completion to the full word.
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries)) #displays hangman depending on the number of tries.
        print(word_completion)
        print("\n")
    if guessed: #displays if user guesses the correct word
        print("Congrats, you guessed the word! You win!")
    else: # when the user runs out of tries, this block will display the correct word.
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries): # displays the states of hangman based on the number of tries.
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


def main(): #this function gives the user the option to play again. if they press y the game continues. if "n" the game ends.
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":  1#runs the script on the command line
    main()