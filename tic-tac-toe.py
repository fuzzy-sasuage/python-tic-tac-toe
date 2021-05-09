import random
import os
emptychar = ' '
usevectors = True

theBoard = [
        [emptychar, emptychar, emptychar], 
        [emptychar, emptychar, emptychar], 
        [emptychar, emptychar, emptychar]
        ]

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
    for i in range(len(board)):
        row = ''
        for j in range(len(board[i])):
            row += ' |' + board[i][j] + '| '
        print(row + '\n')
    # print('   |   |')
    # print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    # print('   |   |')
    # print('-----------')
    # print('   |   |')
    # print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    # print('   |   |')
    # print('-----------')
    # print('   |   |')
    # print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    # print('   |   |')

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

    board[move.y][move.x] = letter

def canWin(bo, le):  # NOT FULLY IMPLEMENTED YET!
    if usevectors: # USING 2D ARRAYS

        possiblecount = 0 # Define integer to count the number of possible wins there can be.
        
        pos = Vector2(-1, -1) # Define a Vector2 to return; Will return as "(-1, -1)" if unchanged, representing there was no possible win yet.

        possible = [] # Define list of possible remaining moves, from which to simulate outcomes.
        for i in range(len(bo)):
            for j in range(len(bo[i])):
                if isSpaceFree(bo, Vector2(i, j), emptychar):
                    possible.append(Vector2(i, j)) # Add possible move to array, because that space is empty.
        
        # Iterate over each possible move (Empty spaces) for a way that a player might win.
        for i in range(len(possible)): 
            # Establish simulated board (2D Array), so as to not tamper with the original board while simulating it.
            print('Attempt: (' + str(possible[i].x) + ', ' + str(possible[i].y) + ')')
            sim_board = bo
            # Iterate over all positions of simulated board to find possible wins.
            for i in range(len(sim_board)):
                for j in range(len(sim_board[i])):
                    if isSpaceFree(sim_board, Vector2(i, j), emptychar):
                        pass
            i1 = possible[i].x
            j1 = possible[i].y
            sim_board = getBoardCopy(sim_board)
            sim_board[possible[i].y][possible[i].x] = le
            makeMove(sim_board, 'X', possible[i]) # Simulate Move
            drawBoard(sim_board)
            
            #os.system('cls' if os.name == 'nt' else 'clear')
            if ((sim_board[2][0] == le and sim_board[2][1] == le and sim_board[2][2] == le) or # across the top

            (sim_board[1][0] == le and sim_board[1][1] == le and sim_board[1][2] == le) or # across the middle

            (sim_board[0][0] == le and sim_board[0][1] == le and sim_board[0][2] == le) or # across the sim_boardttom
            (sim_board[0][0] == le and sim_board[1][0] == le and sim_board[2][0] == le) or # down the left side
            (sim_board[0][1] == le and sim_board[1][1] == le and sim_board[2][1] == le) or # down the middle
            (sim_board[0][2] == le and sim_board[1][2] == le and sim_board[2][2] == le) or # down the right side
            (sim_board[0][0] == le and sim_board[1][1] == le and sim_board[2][2] == le) or # diagonal
            (sim_board[0][2] == le and sim_board[1][1] == le and sim_board[2][0] == le)): # diagonal
                possiblecount += 1
                pos = Vector2(i, j) # Set new possible win position
        if possiblecount > 0:
            return pos
        else:
            return pos

                    
    else:
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top

        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle

        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def isWinner(bo, le):
    if usevectors: # USING 2D ARRAYS
        return ((bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or # across the top

        (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or # across the middle

        (bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or # across the bottom
        (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or # down the left side
        (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or # down the middle
        (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le) or # down the right side
        (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or # diagonal
        (bo[0][2] == le and bo[1][1] == le and bo[2][0] == le)) # diagonal
    else:
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top

        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle

        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
def getBoardCopy(board):
    return theBoard
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard
def isSpaceFree(board, move, emptychar):
    # Check (with Vector2 move) if position is empty on 2 Dimensonal array.
    return board[move.y][move.x] == emptychar
def getPlayerMove(board):
    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move), ' '):

        print('What is your next move? (1-9)')

        move = input()
    return int(move)
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []

    for i in movesList:

        if isSpaceFree(board, i, ' '):

            possibleMoves.append(i)
    if len(possibleMoves) != 0:

        return random.choice(possibleMoves)

    else:
        # Not return None, return random to not die.
        if (isBoardFull(theBoard)):
            pass
        else:
            # Get random move
            while True:
                rand = Vector2(random.randint(0,2), random.randint(0,2))
                if isSpaceFree(theBoard, rand, emptychar):
                    print('oof avoided') #Successfully returned random
                    return rand
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':

        playerLetter = 'O'

    else:

        playerLetter = 'X'
    for i in range(1, 10):

        copy = getBoardCopy(board)

    
    move = chooseRandomMoveFromList(board, [Vector2(0, 0), Vector2(0, 2), Vector2(2, 0), Vector2(2, 2)])
    print("move: " + str(move))
    if move != None:

        return move
    else:
        if (isBoardFull(theBoard)):
            print('board full')
            pass
        else:
            # Get random move
            while True:
                rand = Vector2(random.randint(0,2), random.randint(0,2))
                if isSpaceFree(theBoard, rand, emptychar):
                    print('oof avoided') #Successfully returned random
                    return rand
            return move

def isBoardFull(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if isSpaceFree(board, Vector2(i, j), emptychar):
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

            # Simulate possible winning moves 
              # NOT FULLY IMPLEMENTED YET!
            # wins = canWin(theBoard, playerLetter)
            # if wins.x != Vector2(-1, -1).x and wins.y != Vector2(-1, -1).y:

            #     #drawBoard(theBoard)

            #     print('Win available! (' + str(wins.x) + ', ' + str(wins.y) + ')')
            else:
                
                if isBoardFull(theBoard):

                    drawBoard(theBoard)

                    print('The game is a tie!')

                    break

                else:
                    turn = 'computer'
                    #print('Can\'t win yet' + '(' + str(wins.x) + ', ' + str(wins.y) + ')') # Using Escape Character "\" to allow for apostrophe -> (\')



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
