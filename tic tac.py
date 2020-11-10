board=[" " for x in range(10)]


def inserletter(letter,pos):
    board[pos] = letter

def spaceisfree(pos):
    return board[pos] == ' '

def printboard(board):
    print("   |   |   ")
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("   |   |   ")
    print("------------")

    print("   |   |   ")
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("   |   |   ")
    print("------------")

    print("   |   |   ")
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("   |   |   ")

def isboardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        True
def iswinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[3]==l and b[5]==l and b[7]==l))

def playermove():
    run=True
    while run:
        move=input("Please select a positon to Enter the X between 1 to 9 ")
        try:
            move=int(move)
            if move > 0 and move < 10:
                if spaceisfree(move):
                    run=False
                    inserletter("X",move)
                else:
                    print("Sorry Space is occupied")

            else:
                print("Please! Enter the number between 1 to 9")

        except:
            print("Please type a Number")

def computermove():
    possiblemoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move=0
    for let in ["o","X"]:
        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if iswinner(boardcopy,let):
                move = i
                return move


    cornersopen=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen) > 0:
        move = selectRandom(cornersopen)
        return move
    if 5 in possiblemoves:
        move=5
        return move

    edgesopen=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesopen.append(i)
        if len(edgesopen) > 0:
            move= selectRandom(edgesopen)
            return move

def selectRandom(li):
    import random
    ln=len(li)   #[1,2,3]
    r=random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the TIC TAC TOE GAME ")
    printboard(board)

    while not(isboardfull(board)):
        if not(iswinner(board,"o")):
            playermove()
            printboard(board)
        else:
            print("Sorry you loose!")
            break

        if not(iswinner(board,"X")):
            move=computermove()
            if move==0 :
                print(" Game is tie ")
            else:
                inserletter("o",move)
                print("computer placed o on position",move)
                printboard(board)
        else:
            print("Congratulation you won the game ")


    if isboardfull(board):
        print("Game Tie")

while True:
    x=input("Do you want to play again? (y/n)")
    if x.lower()=='y':
        board=[" " for x in range(10)]
        print("---------------------")
        main()
    else:
        break
