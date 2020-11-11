import random
def hangman():
    word= random.choice(["tiger","peacock","lion","pugger","elephant", "monkey" ,"dog" ,"cat" ,"zebra", "deer"])
    validletters='abcdefghijklmnopqrstuvwxyz'
    turns=10
    guessmade=''

    while len(word)>0:
        main=""
        missed=0

        for letter in word:
            if letter in guessmade:
                main=main+letter

            else:
                main=main + "_"+" "

        if main==word:
            print(main)
            print("Congratulation! You WON")
            break

        print("Guess the word",main)
        guess=input()



        if guess in validletters:
            guessmade=guessmade+guess
        else:
            print("Enter the valid character")
            guess=input()
        if guess not in word:
            turns=turns-1

            if turns==9:
                print("9 turns left")
                print("----------")
            if turns==8:
                print("8 turns lef")
                print("----------")
                print("     0    ")
            if turns==7:
                print("7 turns left")
                print("----------")
                print("     0    ")
                print("     |    ")
            if turns==6:
                print("6 turns left")
                print("----------")
                print("     0    ")
                print("     |    ")
                print("    /     ")
            if turns==5:
                print("5 turns left")
                print("----------")
                print("     0    ")
                print("     |    ")
                print("    / \    ")

            if turns==4:
                print("4 turns left")
                print("----------")
                print("   \ 0    ")
                print("     |    ")
                print("    / \    ")



            if turns==3:
                print("3 turns left")
                print("----------")
                print("   \ 0 /   ")
                print("     |    ")
                print("    / \    ")



            if turns==2:
                print("2 turns left")
                print("----------")
                print("   \ 0 /|    ")
                print("     |    ")
                print("    / \    ")



            if turns==1:
                print("1 turns left")
                print("Last breaths counting!")
                print("----------")
                print("   \ 0_|/   ")
                print("     |    ")
                print("    / \    ")

            if turns==0:
                print("You Loose|")
                print("yoy did not save the hand of main")
                print("----------")
                print("     0_|   ")
                print("    /|\    ")
                print("    / \    ")
                break








print("Welcome to the Hangman Game")
name=input("Enter your name ")
print("Hello",name)
print("---------------------")
print("Try to guess the word within 10 try-- Best Of Luck")
hangman()
