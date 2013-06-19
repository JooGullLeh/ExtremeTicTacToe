'''
    shapes.py Stores the data for simple shapes for our collision game
'''

class rectangle(object):
    '''
    rectangle class store X and Y position
    '''
    def __init__(self,x,y):
        '''
        This is the constructor which takes X and Y position arguments
        '''
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        '''
        This Function moves the X position by adding or subtracting
        '''
        self.x+=x
    def setY(self,y):
        '''
        This Function moves the Y position by adding or subtracting
        '''
        self.y+=y

class Circle(object):
    '''
    Stores X and Y position for a Circle
    '''
    def __init__(self, x, y):
        '''constructor for circle class
        '''
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        '''
        This Function moves the X position by adding or subtracting
        '''
        self.x+=x
    def setY(self,y):
        '''
        This Function moves the Y position by adding or subtracting
        '''
        self.y+=y

def main():
    print("Creating a rectangle at (10, 20)")
    r1 = rectangle(10,20)
    print("Change rectangle position to (20,15)")
    r1.setX(10)
    r1.setY(-5)
    print("Current rectangle position is ({}, {}".format(r1.getX(), r1.getY()))
    print("Creating a circle at 5,5")
    c1= Circle(5,5)
    print("Current Circle position is ({}, {}".format(c1.getX(), c1.getY()))
if __name__ == "__main__":
    main()