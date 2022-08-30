#Import the files and libraries that will be used
from data import ES_WORDS
from data import EN_WORDS
import variables
import random
import os

def get_word(): #returns a word from data file depending the chosen lenguage
    if menu.language == "1":
        word = random.choice(ES_WORDS)
    elif menu.language == "2":
        word = random.choice(EN_WORDS)
    return word.upper()

def menu():
    while True:
        title()
        os.system ("echo '{}' | lolcat".format("1. Play")) #Output printed by console and passed trhough lolcat to give it a color
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
    os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal
    os.system ("echo '{}' | lolcat".format(variables.HANGMAN_TITLE)) #prints title and pass it trough the terminal using lolcat

def display_hangman(tries): #Takes the stages of the hangaman to print them later
   return variables.STATEGES[tries]

def play(word):
    word_completion = '_ '*len(word) #saves the lenght of the word in underscores
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
    while not guessed and tries > 0: #while guessed is false and tries > 6 run the game (total tries = 6)
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha(): #Checks if the input is a letter
            if guess in guessed_letters:
                print('\033[93m' + "You already guessed the letter" + '\033[0m', guess) #print it in yellow
            elif guess not in word:
                print('\033[91m' + guess, "is not in the word." + '\033[0m') #printed in red
                tries -= 1
                guessed_letters.append(guess) #Appends the letter guessed to the list, to check if it arleady guessed later 
            else:
                print('\033[92m' + "Good job,", guess, "is in the word!" + '\033[0m')
                guessed_letters.append(guess)
                word_completion = word_completion.replace(" ", "") #Takes out the spaces between the underscores 
                word_as_list = list(word_completion) #Makes a list of thw word to check the index later
                indices = [i for i, letter in enumerate(word) if letter == guess] #Checkd the index to change the underscore for a letter later
                for index in indices: #replaces the underscore for a letter
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                word_completion = word_completion.replace("", " ") #Adds the spaces again to make the word more legible  
                if "_" not in word_completion: #If there are not more underscores then the word is already guessed
                    guessed = True
                    print(word_completion)
        elif len(guess) == len(word) and guess.isalpha(): #Checks if the guess is a word instead of a letterls
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