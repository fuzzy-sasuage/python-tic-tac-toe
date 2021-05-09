import random

#Vector2 Class

class Vector2:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def reset(self):
        self.x = 0
        self.y = 0
    def getpos(self):
        pass

def drawBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def inputPlayerLetter():
    letter = ''

    while not (letter == 'X' or letter == 'O'):

        print('Do you want to be X or O?')

        letter = input().upper()

    if letter == 'X':

        return ['X', 'O']

    else:
        return ['O', 'X']

def whoGoesFirst():

    if random.randint(0, 1) == 0:

        return 'computer'

    else:

        return 'player'

def playAgain():

    print('Do you want to play again? (yes or no)')

    return input().lower().startswith('y')

def makeMove(board, letter, move):

    board[move] = letter

def isWinner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top

    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle

    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard
def isSpaceFree(board, move):
    return board[move] == ' '
def getPlayerMove(board):
    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):

        print('What is your next move? (1-9)')

        move = input()
    return int(move)
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []

    for i in movesList:

        if isSpaceFree(board, i):

            possibleMoves.append(i)
    if len(possibleMoves) != 0:

        return random.choice(possibleMoves)

    else:
        # Not return None, return random to not die.
        print('oof avoided')
        return random.randint(0,8)
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':

        playerLetter = 'O'

    else:

        playerLetter = 'X'
    for i in range(1, 10):

        copy = getBoardCopy(board)

    
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    print("move: " + str(move))
    if move != None:

        return move
    else:
        move = random.randint(0,8)
        print('oof avoided')
        return move

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def domove():
    # Define player input
    playerx = input('Input X Coordinate: ') 
    playery = input('Input Y Coordinate: ')
    playerthing = input('Input new thing: ')

    pos = Vector2(playerx, playery)

    print('x=' + str(pos.x) + ', y=' + str(pos.y))

    theBoard[pos.y][pos.x] = playerthing

print('Welcome to Tic Tac Toe!')
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True



    while gameIsPlaying:

        if turn == 'player':
            
            usevectors = True


            drawBoard(theBoard)
            if usevectors:
                domove()
                for i in range(len(theBoard)):
                    row = ''
                    for j in range(len(theBoard[i])):
                        row += ' ' + theBoard[i][j] + ' '
                    print(row + '\n')
            else:

                move = getPlayerMove(theBoard)

                makeMove(theBoard, playerLetter, move)



            if isWinner(theBoard, playerLetter):

                drawBoard(theBoard)

                print('SKO! You have won the game!')
                # End game
                gameIsPlaying = False

            else:

                if isBoardFull(theBoard):

                    drawBoard(theBoard)

                    print('The game is a tie!')

                    break

                else:
                    turn = 'computer'



        else:
            move = getComputerMove(theBoard, computerLetter)

            makeMove(theBoard, computerLetter, move)



            if isWinner(theBoard, computerLetter):

                drawBoard(theBoard)

                print('The computer has beaten you! You lose.')

                gameIsPlaying = False

            else:

                if isBoardFull(theBoard):

                    drawBoard(theBoard)

                    print('The game is a tie!')

                    break

                else:

                    turn = 'player'



    if not playAgain():
        
        break
