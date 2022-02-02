import random

game_version = input("Do you want to play with another player or do you want to generate the word?\nPlayer\tGenerate  >>")

def hangman_picture():
    pictureAsString6 = """

        ---------
        |       |
        |       |
        |       O
        |      /|\\
        |       |
        |      / \\
        |
        |

        """

    pictureAsString5 = """

        ---------
        |       |
        |       |
        |       O
        |      /|\\
        |       |
        |      / 
        |
        |

        """

    pictureAsString4 = """

        ---------
        |       |
        |       |
        |       O
        |      /|\\
        |       |
        |       
        |
        |

        """

    pictureAsString3 = """

        ---------
        |       |
        |       |
        |       O
        |      /|
        |       |
        |       
        |
        |

        """

    pictureAsString2 = """

        ---------
        |       |
        |       |
        |       O
        |       |
        |       |
        |       
        |
        |

        """

    pictureAsString1 = """

        ---------
        |       |
        |       |
        |       O
        |      
        |       
        |      
        |
        |

        """

    pictureAsString0 = """

        ---------
        |       |
        |       |
        |       
        |      
        |       
        |      
        |
        |

        """

    pictures = [pictureAsString6, pictureAsString5, pictureAsString4, pictureAsString3, pictureAsString2, pictureAsString1, pictureAsString0]
    return pictures

def generate_word_with_version(gameVersion):
    if gameVersion == "player":
        userWord = input("What word do you want to make other player guess? ")
        userWord = userWord.upper()
        return userWord
    elif gameVersion == "generate":
        f = open("d:/code/hangman/sowpods.txt", "r")
        lines = f.readlines()
        return random.choice(lines)
    else:
        print("Error! You have to type 'player' or 'generate' ")
        quit()

def guess_word(randomWord, pictures, game_version):
    print("Welcome to Hangman!")
    wrong_tries = 0
    word = list(randomWord)
    if game_version == "generate":
        word.pop(-1)
    guessed_word = '_' * len(word)
    guessed_word = list(guessed_word)
    letters_guessed = []

    while True:
         
        triesLeft = 6 - wrong_tries
        print(" ".join(guessed_word))
        print(pictures[triesLeft])
        print("You have", triesLeft, "tries left")
        print()
        letter = input("Guess the word by entering a letter: ")
        letter = letter.upper()
        
        if letter in letters_guessed:
            print("That letter has already been guessed! Try again.")
        elif letter in word:
            while letter in word:
                index = word.index(letter) 
                guessed_word[index] = letter
                word[index] = "_"
        else:
            print("Wrong!")
            wrong_tries += 1

        letters_guessed.append(letter)

        if "_" not in guessed_word:
            print(" ".join(guessed_word))
            print("Congratulations! You won.")
            break

        if wrong_tries == 6:
            print("You have 0 tries left. You lost.\n The word was:", randomWord)
            print(pictures[0])
            break

def play_again():
    restart = input("Do you want to play again? \n Yes \t No ")
    if restart.lower() == "yes":
        main()
    elif restart.lower() == "no":
        quit()
    else:
        print("Error. Please type in 'Yes' or 'No' ")
        play_again()

def main():
    random_word = generate_word_with_version(game_version)
    # print(random_word) 
    hangman_picture()
    pictures = hangman_picture()
    guess_word(random_word, pictures, game_version)
    play_again()

main()  



