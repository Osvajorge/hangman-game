from data import ES_WORDS
from data import EN_WORDS
import variables
import random
import os

def bcolors():
    bcolors.OKGREEN = '\033[92m'
    bcolors.FAIL = '\033[91m'
    bcolors.ENDC = '\033[0m'
    bcolors.BOLD = '\033[1m'


def get_word():
    if menu.language == "1":
        word = random.choice(ES_WORDS)
    elif menu.language == "2":
        word = random.choice(EN_WORDS)
    return word.upper()

def menu():
    while True:
        title()
        os.system ("echo '{}' | lolcat".format("1. Play"))
        os.system ("echo '{}' | lolcat".format("2. Exit"))
        choice = input("Enter your choice: ")
        if choice == "1":
            title()
            print("1. Spanish")
            print("2. English")
            os.system ("echo '{}' | lolcat".format("Press any other key to exit"))
            print("\n")
            menu.language = input("Enter the language in which you want to guess: ")
            if menu.language == "1":
                get_word()
            elif menu.language == "2":
                get_word()
            break   
        elif choice == "2":
            break
        else:
            print("Invalid choice")
            continue
        
def title():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system ("echo '{}' | lolcat".format(variables.HANGMAN_TITLE)) #print title and pass it trough the terminal using lolcat

def display_hangman(tries):
   return variables.STATEGES[tries]

def play(word):
    word_completion = '_ '*len(word)
    word_as_underscore = []
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    os.system ("echo '{}' | lolcat".format(variables.SUBMENU))
    if menu.language == "1":
        print((" "*20)+'You are playing in Spanish')  
    else:
         ((" "*20)+'You are playing in Spanish')
    os.system ("echo '{}' | lolcat".format(display_hangman(tries)))
    os.system ("echo '{}' | lolcat".format(word_completion))
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('\033[93m' + "You already guessed the letter" + '\033[0m', guess)
            elif guess not in word:
                print('\033[91m' + guess, "is not in the word." + '\033[0m')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('\033[92m' + "Good job,", guess, "is in the word!" + '\033[0m')
                guessed_letters.append(guess)
                word_completion = word_completion.replace(" ", "")
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                word_completion = word_completion.replace("", " ") 
                if "_" not in word_completion:
                    guessed = True
                    print(word_completion)
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('\033[93m' + "You already guessed the word", guess + '\033[0m')
            elif guess != word:
                print('\033[91m' + guess, "is not the word." + '\033[0m')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('\033[91m' + "Not a valid guess." + '\033[0m')
        os.system ("echo '{}' | lolcat".format(display_hangman(tries)))
        os.system ("echo '{}' | lolcat".format(word_completion))
        print("\n")
    if guessed:
        print('\033[92m' + "Congrats, you guessed the word! You win!" + '\033[0m')
    else:
        print('\033[91m' + "Sorry, you ran out of tries. The word was " + word + ". Maybe next time!" + '\033[0m')


def run():
    menu()
    word = get_word()
    play(word)
    while input("play again? (Y/N) ").upper() == "Y":
        menu()
        word = get_word()
        play(word)


if __name__ == "__main__":
    run()