__author__ = 'BYH'


class Rectangle(object):
    def __init__(self,x,y):

        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):

        self.x+=x
    def setY(self,y):
        self.y+=y

class Circle(object):

    def __init__(self, x, y, x2, y2, color):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.color = color
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):

        self.x+=x
    def setY(self,y):
        self.y+=y

