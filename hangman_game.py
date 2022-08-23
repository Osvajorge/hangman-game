import os
import variables
import random
import data

def get_word(language):
    if language == 'es':
        get_word.word = data.ES_WORDS[random.randint(0, len(data.ES_WORDS)-1)]
    if language == 'en':
        get_word.word = data.EN_WORDS[random.randint(0, len(data.EN_WORDS)-1)]
    return get_word.word

def game_screen(word):
    game_screen.letters = []
    for letter in word:
        game_screen.letters.append(letter)
    game_screen.display = '___ ' * len(word)
    if menu.chosen_l == 'es':
        print((" "*20)+'You are playing in Spanish')
    elif menu.chosen_l == 'en':
        print((" "*20)+'You are playing in English')
    print("\n")
    while True:
        os.system("echo '{}' | lolcat".format((" "*20)+game_screen.display))
        print("\n")
        break 
    print(game_screen.letters)
        

#hangman game
def hangman_game():
    title()
    os.system ("echo '{}' | lolcat".format(variables.SUBMENU))
    get_word(menu.chosen_l)
    game_screen(get_word.word)
    guess = input('Write a letter: ')
    
    already_guessed = []
    if guess in get_word.word:
        already_guessed.extend([guess])
        index = get_word.word.find(guess) 
        get_word.word = get_word.word[:index] + "_" + get_word.word[index + 1:]
        game_screen.display = game_screen.display[:index] + guess + game_screen.display[index + 1:]
        print(game_screen.display)
                
def title():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system ("echo '{}' | lolcat".format(variables.HANGMAN_TITLE)) #print title and pass it trough the terminal using lolcat

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
            language = input("Enter the language in which you want to guess: ")
            if language == "1":
                menu.chosen_l='es'
                hangman_game()
            elif language == "2":
                menu.chosen_l='en'
                hangman_game()
            break   
        elif choice == "2":
            break
        else:
            print("Invalid choice")
            continue

def run ():
    menu()

if __name__ == '__main__':
    run()
