from Tkinter import *
import shapes


def collisionCheck(player,enemy):
    if (player.getX() + 50 >= enemy.getX()):
        if (player.getY() <= enemy.getY()+50 and player.getY() + 50 >= enemy.getY()):
            return True
    return False

root = Tk()
root.title("Game_Example")
root.geometry("1000x700")

canvas = Canvas (width = 1000, height = 700, bg = "black")
canvas.grid()

guiRect = canvas.create_rectangle(0,350,50,400, outline = "black", fill = "white")
playerRect = shapes.rectangle(400,350)

enemyGuiRect = canvas.create_rectangle(0,250,150,400, outline = "black", fill = "red")
enemyRect = shapes.rectangle (400,250)

fartGuiCircle =canvas.create_oval(0, 600, 100,500, outline="green", fill="yellow")
fartCircle = shapes.Circle(100,100)

def timer():

    # playerRect.setX(10)
    # playerRect.setY(10)
    # canvas.move(guiRect,10,0)

    fartCircle.setX(50)
    fartCircle.setY(50)
    canvas.move(fartGuiCircle,20,0)

    if (collisionCheck(playerRect,enemyRect)):
        canvas.move(guiRect,100,5)


    root.after(90,timer)

timer()

help(shapes)
root.mainloop()