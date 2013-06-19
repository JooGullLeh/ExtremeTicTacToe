from Tkinter import*


class rectangle(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def setX(self,x):
		self.x += x
	def setY(self,y):
		self.y += y

#collision detector checks at a certain boundary, so it doesn't have
#to be exactly over it to detect collison
def collisionCheck(player,enemy):
	if (player.getX() + 50 >=enemy.getX()):
		if (player.getY() <= enemy.getY()+50 and player.getY() + 50 >= enemy.getY()):
			return True
	return False
def key(event):
	if event.keysym =="Up":
		canvas.move(gui_rect, 0,-10)
	if event.keysym =="Down":
		canvas.move(gui_rect, 0, 10)
	if event.keysym == "Left":
		canvas.move(gui_rect,-10,0)
	if event.keysym =="Right":
		canvas.move(gui_rect,10,0)
	canvas.update()
root = Tk()
root.title("Title")
root.geometry("1000x700")

canvas = Canvas (width =1000, height = 700, bg ="red")
canvas.grid()

playerRect = rectangle(0,0)
player_rect = canvas.create_rectangle(700,0,750,50, fill = "yellow")

enemyRect = rectangle(700,0)
enemy_rect = canvas.create_rectangle(700,0, 750, 50, fill ="blue")

canvas.bind("<Key>", key)
canvas.focus_set()
#timer moves things (automated)
def timer():
	playerRect.setX(10)
	canvas.move(player_rect,10,0)

	if (collisionCheck(playerRect,enemyRect) == True):
		canvas.create_rectangle(30,30,600,600,fill ="white")
	root.after(20,timer)
timer()

root.mainloop()
