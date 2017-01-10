import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen+5)

def drawSquare(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(100)
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.right(90)
        myTurtle.forward(100)        
        


#drawSpiral(myTurtle, 100)
drawSquare(myTurtle, 100)
myWin.exitonclick()
