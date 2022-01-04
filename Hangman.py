import random

def hangmanPicture():
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

def generateWord():
    f = open("d:/code/hangman/sowpods.txt", "r")
    lines = f.readlines()
    return random.choice(lines)
    # userWord = input("What word do you want to make other player guess? ")
    # return userWord

def guessWord(randomWord, pictures):
    print("Welcome to Hangman!")
    wrongTries = 0
    word = list(randomWord)
    word.pop(-1)
    guessedWord = '_' * len(word)
    guessedWord = list(guessedWord)
    lettersGuessed = []

    while(True):
        
        triesLeft = 6 - wrongTries
        print(" ".join(guessedWord))
        print(pictures[triesLeft])
        print("You have", triesLeft, "tries left")
        print()
        letter = input("Guess the word by entering a letter: ")
        letter = letter.upper()
        
        if letter in lettersGuessed:
            print("That letter has already been guessed! Try again.")
        elif letter in word:
            while letter in word:
                index = word.index(letter) 
                guessedWord[index] = letter
                word[index] = "_"
        else:
            print("Wrong!")
            wrongTries += 1

        lettersGuessed.append(letter)

        if "_" not in guessedWord:
            print(" ".join(guessedWord))
            print("Congratulations! You won.")
            break

        if wrongTries == 6:
            print("You have 0 tries left. You lost.")
            print(pictures[0])
            break

def playAgain():
    restart = input("Do you want to play again? \n Yes \t No ")
    if restart.lower() == "yes":
        main()
    elif restart.lower() == "no":
        quit()
    else:
        print("Error. Please type in 'Yes' or 'No' ")
        playAgain()

def main():
    randomWord = generateWord()
    print(randomWord) 
    hangmanPicture()
    pictures = hangmanPicture()
    guessWord(randomWord, pictures)
    playAgain()

main()  



