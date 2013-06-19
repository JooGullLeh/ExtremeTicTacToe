__author__ = 'BYH'
# connect4.py
# from tic-tac-toe2.py:
#   displays board, makes moves, takes turns
#   Now with checks for wins and ties!
#   Now also draws line when player wins
# Now also restricts moves to column-drops (as in Connect4)

import random
from Tkinter import *

#####################################
## 2d board search code from wordSearch.py
## adapted for use here
## (Searches for 4 of same player in a row)
#####################################

# wordSearch.py

# This program implements a simple wordsearch.
# The puzzle is a 2d list of characters.
# The word is a string -- the word we are searching
# for in the puzzle.

# A sample search is this:

# puzzle = [ [ 'a', 'q', 'r', 'z' ],
#            [ 'g', 'o', 'd', 'q' ],
#            [ 'w', 'm', 'z', 'c' ]
#          ]
#
# print wordSearch(puzzle, "dog")

# Notice that the word "dog" occurs in row 1
# (the second row), starting at column 2,
# heading to the left.

# To represent directions (headings), we will
# use two numbers -- (drow, dcol) -- representing
# the change in row and change in col necessary
# to take one step in that direction.

# Thus, "left" is represented as (0, -1), since
# to take one step left we do not change our
# row but we subtract one from our column.

# Thus, the example above prints:
#  (1, 2, (0, -1))
# This means the word "dog" was found, starting
# at row 1 and col 2, and heading left (0, -1).

#############################################

# This is a wrapper that packages the wordSearch
# function so that it can be used to check for
# a winner in our tic-tac-toe game

def isWinner(canvas):
    board = canvas.data["board"]
    player = canvas.data["currentPlayer"]
    word = [ player ] * 4 # 4 in a row
    winningMove = wordSearch(board, word)
    if (winningMove == None):
        return False
    else:
        (startRow, startCol, (drow, dcol)) = winningMove
        endRow = startRow + 3*drow
        endCol = startCol + 3*dcol
        canvas.data["winningLineCell1"] = (startRow, startCol)
        canvas.data["winningLineCell2"] = (endRow, endCol)
        return True

# This is the main wordSearch function.
# It checks every row,col starting position,
# and then calls a helper function which checks
# if the word is in the puzzle at that starting
# position.

def wordSearch(puzzle, word):
    rows = len(puzzle)
    cols = len(puzzle[0])
    for startingRow in range(rows):
        for startingCol in range(cols):
            found = wordSearch1(puzzle, word, startingRow, startingCol)
            if (found != None):
                return found
    return None

# This is a helper function.  It is given a
# specific startingRow and startingCol, and it
# tries every possible direction given this
# starting position.  For each direction, it
# calls yet another helper function (see below).
def wordSearch1(puzzle, word, startingRow, startingCol):
    for dRow in range(-1,2):
        for dCol in range(-1,2):
            if ((dRow != 0) or (dCol != 0)):
                found = wordSearch2(puzzle, word, startingRow, startingCol, dRow, dCol)
                if (found != None):
                    return found
    return None

# This is another helper function.  It is given
# both a specific starting location (startingRow
# and startingCol) and a specific direction (dRow
# and dCol).  This function checks if the given
# word occurs in the given puzzle, starting at the
# given starting location and heading in the given
# direction.

def wordSearch2(puzzle, word, startingRow, startingCol, dRow, dCol):
    rows = len(puzzle)
    cols = len(puzzle[0])
    for i in range(len(word)):
        row = startingRow + i*dRow
        col = startingCol + i*dCol
        if ((row < 0) or (row >= rows) or \
            (col < 0) or (col >= cols) or \
            puzzle[row][col] != word[i]):
            return None
    return (startingRow, startingCol, (dRow, dCol))

#####################################
## Tic-Tac-Toe logic
#####################################

def mousePressed(event):
    canvas = event.widget.canvas
    if (isGameOver(canvas) == False):
        cell = getCell(canvas, event.x, event.y)
        if (cell != None):
            (row, col) = cell
            doConnect4Move(canvas, col)
        redrawAll(canvas)

def doConnect4Move(canvas, col):
    # Drop a piece in the given col.
    # Actually, just do a traditional tic-tac-toe move
    # in the lowest open row of the given col
    board = canvas.data["board"]
    row = getLowestOpenRow(board, col)
    if (row == None):
        print "Sorry, that column is full!"
    else:
        doTicTacToeMove(canvas, row, col)

def getLowestOpenRow(board, col):
    # find the row where a Connect4 drop would
    # wind up in this col
    rows = len(board)
    cols = len(board[0])
    openRow = None
    for row in range(rows):
        if (board[row][col] == 0):
            openRow = row
    return openRow

def doTicTacToeMove(canvas, row, col):
    # This is the code from mousePressed that does a
    # traditional tic-tac-toe move in the given cell.
    # It is now a helper function for doConnect4Move.
    board = canvas.data["board"]
    if (board[row][col] != 0):
        print "I can't move there!"
    else:
        board[row][col] = canvas.data["currentPlayer"]
        if (isWinner(canvas) == True):
            canvas.data["gameOverMessage"] = \
                "Player " + str(canvas.data["currentPlayer"]) + " wins!!!"
        elif (isTie(board)):
            canvas.data["gameOverMessage"] = "Tie game!!!"
        else:
            switchPlayers(canvas)


def getCell(canvas, x, y):
    board = canvas.data["board"]
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            (left, top, right, bottom) = cellBounds(canvas, row, col)
            if ((left <= x) and (x <= right) and
                (top <= y) and (y <= bottom)):
                return (row, col)
    return None

def keyPressed(event):
    canvas = event.widget.canvas
    if (event.char == "r"):
        init(canvas)
    redrawAll(canvas)

def timerFired(canvas):
    pass

def redrawAll(canvas):
    canvas.delete(ALL)
    drawBoard(canvas)
    drawGameOver(canvas)
    drawWinningLine(canvas)

def drawGameOver(canvas):
    if (isGameOver(canvas) == True):
        cx = canvas.data["canvasWidth"]/2
        cy = canvas.data["canvasHeight"]/2
        color = "salmon"
        canvas.create_text(cx, cy-20, text="Game Over!",
                           font=("Helvetica", 32, "bold"),fill=color)
        canvas.create_text(cx, cy+20, text=canvas.data["gameOverMessage"],
                           font=("Helvetica", 32, "bold"),fill=color)

def drawBoard(canvas):
    board = canvas.data["board"]
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, board, row, col)

def drawWinningLine(canvas):
    if (canvas.data["winningLineCell1"] != None):
        (row1, col1) = canvas.data["winningLineCell1"]
        (row2, col2) = canvas.data["winningLineCell2"]
        (left1, top1, right1, bottom1) = cellBounds(canvas, row1, col1)
        (left2, top2, right2, bottom2) = cellBounds(canvas, row2, col2)
        cx1 = (left1 + right1)/2
        cy1 = (top1 + bottom1)/2
        cx2 = (left2 + right2)/2
        cy2 = (top2 + bottom2)/2
        canvas.create_line(cx1, cy1, cx2, cy2, width=5)

def cellBounds(canvas, row, col):
    margin = canvas.data["margin"]
    cellSize = canvas.data["cellSize"]
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    return (left, top, right, bottom)

def drawCell(canvas, board, row, col):
    (left, top, right, bottom) = cellBounds(canvas, row, col)
    canvas.create_rectangle(left, top, right, bottom, fill="green")
    if (board[row][col] > 0):
        # draw the piece
        if (board[row][col] == 1):
            color = "red"
        else:
            color = "blue"
        canvas.create_oval(left, top, right, bottom, fill=color)

def loadBoard(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    board = [ ]
    for row in range(rows): board += [[0] * cols]
    canvas.data["board"] = board

def printInstructions():
    print "Tic Tac Toe!"

def switchPlayers(canvas):
    player = canvas.data["currentPlayer"]
    if (player == 1):
        canvas.data["currentPlayer"] = 2
    else:
        canvas.data["currentPlayer"] = 1

def isTie(board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                return False
    return True

def isGameOver(canvas):
    return canvas.data["gameOverMessage"] != None

def init(canvas):
    printInstructions()
    loadBoard(canvas)
    canvas.data["inDebugMode"] = False
    canvas.data["gameOverMessage"] = None
    canvas.data["currentPlayer"] = 1
    canvas.data["winningLineCell1"] = None
    canvas.data["winningLineCell2"] = None
    redrawAll(canvas)

########### copy-paste below here ###########

def run(rows, cols):
    # create the root and the canvas
    root = Tk()
    margin = 5
    cellSize = 40
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    canvas.data["margin"] = margin
    canvas.data["cellSize"] = cellSize
    canvas.data["canvasWidth"] = canvasWidth
    canvas.data["canvasHeight"] = canvasHeight
    canvas.data["rows"] = rows
    canvas.data["cols"] = cols
    init(canvas)
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run(8,16)