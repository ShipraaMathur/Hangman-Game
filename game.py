from operator import length_hint
import random
import time
from subprocess import call

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

name = input("Enter your name : ")
print("Welcome to Hangman "+ name + "!!")

time.sleep(2)
print("The game is about to begin!!")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
# clear()


def main():
    global count
    global display 
    global word
    global already_done
    global length
    global play_game
    words_to_guess = ["january","image","bottle","shipra","mathur","mother","family"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'*length
    already_done = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do you want to play again? \nEnter y/Y or n/N")
    while play_game not in ["y","Y","n","N"]:
        play_game = input("Do you want to play again? \nEnter y/Y or n/N")
    if play_game == 'y' or play_game == 'Y':
        main()
    else:
        print("Thanks for playing!!\nByee!!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_done
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_done.extend([guess])
        index = word.find(guess)
        word = word[:index] + '_' + word[index+1:]
        display = display[index:] + guess + display[index+1:]
        print(display + "\n")
    elif guess in already_done:
        print("try another letter")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_done,word)
            play_loop()

    if word == '_'*length:
        print("congratulations!! You won!!")
        play_loop()

    elif count != limit:
        hangman()
main()
hangman()
        
