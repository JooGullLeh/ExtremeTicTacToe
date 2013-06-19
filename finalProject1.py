#Brian Han
#ITP115
#Final Project
#Professor Parke
#Tickytackytoe
#Running on Python 2.7
import random
from Tkinter import *
import ImageTk
import finalProjectPieces

import tkMessageBox

##Opens box that gives instructions for tictactoe, clicking it opens gameboard
window = Tk()
window.geometry("5x5")
tkMessageBox.showinfo(title="Instructions",message=
            """Tic Tac Toe!
            \nThis ain't no ordinary game of 'toe!
            \nRather than 3 pieces in a row,
            \nyou have to get 5 in a row!
            \nFirst to 5 wins!"""" "
             , parent=window)

#Prints instructions to console
def instructions():
    print """\t\tTic Tac Toe!
            \nThis ain't no ordinary game of 'toe!
            \nRather than 3 pieces in a row,
            \nyou have to get 5!
            \nFirst to 5 wins!"""

#Gameboard
def gameBoard(canvas):
    gameBoard = canvas.data["gameBoard"]
    hors = len(gameBoard)
    vers = len(gameBoard[0])
    for hor in range(hors):
        for ver in range(vers):
            playerPiece(canvas, gameBoard, hor, ver)

#Creates cell for gameboard
def cellArea(canvas, hor, ver):
    margins = canvas.data["margins"]
    cellSizes = canvas.data["cellSizes"]
    left = margins + ver * cellSizes
    right = left + cellSizes
    top = margins + hor * cellSizes
    bottom = top + cellSizes
    return (left, top, right, bottom)

#Creates each piece using class from finalProjectPieces
def playerPiece(canvas, gameBoard, hor, ver):
    (left, top, right, bottom) = cellArea(canvas, hor, ver)
    canvas.create_rectangle(left, top, right, bottom, fill="green")
    if (gameBoard[hor][ver] > 0):
        if (gameBoard[hor][ver] == 1):
            color="red"
            finalProjectPieces.Circle(left, top, right, bottom, color)
        else:
            color="blue"
            finalProjectPieces.Circle(left, top, right, bottom, color)
        canvas.create_oval(left, top, right, bottom, fill=color )

#Checks horizontally and vertically
def checkRows(grid, tictactoe):
    hors = len(grid)
    vers = len(grid[0])
    for sHor in range(hors):
        for sVer in range(vers):
            foundPiece = checkRows1(grid, tictactoe, sHor, sVer)
            if (foundPiece != None):
                return foundPiece
    return None

#Nested check rows functions
def checkRows1(grid, tictactoe, sHor, sVer):
    for newHor in range(-2,2):
        for newVer in range(-2,2):
            if ((newHor != 0) or (newVer != 0)):
                foundPiece = checkRows2(grid, tictactoe, sHor, sVer, newHor, newVer)
                if (foundPiece != None):
                    return foundPiece
    return None
#Nested check rows functions
def checkRows2(grid, tictactoe, sHor, sVer, newHor, newVer):
    hors = len(grid)
    vers = len(grid[0])
    for i in range(len(tictactoe)):
        hor = sHor + i*newHor
        ver = sVer + i*newVer
        if ((hor < 0) or (hor >= hors) or (ver < 0) or (ver >= vers) or grid[hor][ver] != tictactoe[i]):
            return None
    return (sHor, sVer, (newHor, newVer))

##Checks for move placement on the board
def playerMove(event):
    canvas = event.widget.canvas
    #checks if game is over
    if (gameBlouses(canvas) == False):
        gameBoard = canvas.data["gameBoard"]
        cell = getCell(canvas, event.x, event.y)
        #if cell space not valid, prints to screen and console
        if (cell != None):
            (hor, ver) = cell
            if (gameBoard[hor][ver] != 0):
                xX = canvas.data["canvasW"]/2
                yY = canvas.data["canvasH"]*1.1
                print "Invalid move! Place your piece on an unoccupied spot!"
                canvas.create_text(xX, yY-30, text="Invalid move! Place your piece on an unoccupied spot!",
                           font=("Helvetica", 40, "bold"),fill="purple")
            #if function declareWinner evaluates as true, print to screen
            else:
                gameBoard[hor][ver] = canvas.data["player"]
                if (declareWinner(canvas) == True):
                    canvas.data["endOfGameString"] = "Player " + str(canvas.data["player"]) + " wins!!!"
                elif (catsGame(gameBoard)):
                    canvas.data["endOfGameString"] = "Cat's game"
                else:
                    tradeTurn(canvas)
        resetAll(canvas)


##Find where piece is placed
def getCell(canvas, x, y):
    gameBoard = canvas.data["gameBoard"]
    hors = len(gameBoard)
    vers = len(gameBoard[0])
    for hor in range(hors):
        for ver in range(vers):
            (left, top, right, bottom) = cellArea(canvas, hor, ver)
            if ((left <= x) and (x <= right) and
                (top <= y) and (y <= bottom)):
                return (hor, ver)
    return None

#Trades turns
def tradeTurn(canvas):
    player = canvas.data["player"]
    if (player == 1):
        canvas.data["player"] = 2
    else:
        canvas.data["player"] = 1
#if game is a tie
def catsGame(gameBoard):
    hors = len(gameBoard)
    vers = len(gameBoard[0])
    for hor in range(hors):
        for ver in range(vers):
            if gameBoard[hor][ver] == 0:
                return False
    return True

#Key Pressed function, also checks for if you want a new game
def resetNewGame(event):
    canvas = event.widget.canvas
    if (event.char == "n"):
        init(canvas)
    resetAll(canvas)

#pass the timer because there is none besides victory
def timer(canvas):
    pass
#reset all objects
def resetAll(canvas):
    canvas.delete(ALL)
    gameBoard(canvas)
    gameOverText(canvas)
    WinLine(canvas)
#Text that goes at bottom of screen when you lose
def gameOverText(canvas):
    if (gameBlouses(canvas) == True):
        #coordinates for text placement
        xX = canvas.data["canvasW"]/2
        yY = canvas.data["canvasH"]*1.2
        color = "purple"
        canvas.create_text(xX, yY-30, text="Game Over!",
                           font=("Helvetica", 40, "bold"),fill=color)
        canvas.create_text(xX, yY+30, text=canvas.data["endOfGameString"],
                           font=("Helvetica", 40, "bold"),fill=color)


##Draws the winning line through the winning pieces
##The xX and yY coordinates direct
def WinLine(canvas):
    if (canvas.data["winLineCell1"] != None):
        (row1, col1) = canvas.data["winLineCell1"]
        (row2, col2) = canvas.data["winLineCell2"]
        (left1, top1, right1, bottom1) = cellArea(canvas, row1, col1)
        (left2, top2, right2, bottom2) = cellArea(canvas, row2, col2)
        xX1 = (left1 + right1)/2
        yY1 = (top1 + bottom1)/2
        xX2 = (left2 + right2)/2
        yY2 = (top2 + bottom2)/2
        canvas.create_line(xX1, yY1, xX2, yY2, width=6)


#renews board
def renewGameBoard(canvas):
    hors = canvas.data["hors"]
    vers = canvas.data["vers"]
    gameBoard = [ ]
    for hor in range(hors): gameBoard += [[0] * vers]
    canvas.data["gameBoard"] = gameBoard

#Game Over Message when someone wins
def gameBlouses(canvas):
    return canvas.data["endOfGameString"] != None

#declares winner by using checkRows function
def declareWinner(canvas):
    gameBoard = canvas.data["gameBoard"]
    player = canvas.data["player"]
    tictactoe = [ player ] * 5 #tictactoe is 5 player pieces next to each other
    victory = checkRows(gameBoard, tictactoe)
    if (victory == None):
        return False
    else:
        (ogHor, ogCol, (newHor, newVer)) = victory
        checkAllRow = ogHor + 4*newHor
        checkAllColumn = ogCol + 4*newVer
        canvas.data["winLineCell1"] = (ogHor, ogCol)
        canvas.data["winLineCell2"] = (checkAllRow, checkAllColumn)
        return True
#initialize functionw
def init(canvas):
    instructions()
    renewGameBoard(canvas)
    canvas.data["endOfGameString"] = None
    canvas.data["player"] = 1
    canvas.data["winLineCell1"] = None
    canvas.data["winLineCell2"] = None
    resetAll(canvas)


def main(hors, vers):
    root = Tk()
    root.title("EXTREME TICTACTOE")
    margins = 10
    cellSizes = 50
    canvasW = 2*margins + vers*cellSizes
    canvasH = 2*margins + hors*cellSizes
    canvas = Canvas(root, width=canvasW, height=canvasH+160)
    canvas.configure(background='black')
    canvas.pack()

    root.resizable(width=0, height=0)
    ##setting root to canvas
    root.canvas = canvas.canvas = canvas
    canvas.data = {}

    canvas.data["margins"] = margins
    canvas.data["cellSizes"] = cellSizes
    canvas.data["canvasW"] = canvasW
    canvas.data["canvasH"] = canvasH
    canvas.data["hors"] = hors
    canvas.data["vers"] = vers
    init(canvas)
    #bind to left-click
    root.bind("<Button-1>", playerMove)
    root.bind("<Key>", resetNewGame)

    timer(canvas)

    root.mainloop()

main(10,10)




