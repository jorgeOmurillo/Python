from random import randint
import turtle

def tree(branchLen, t, width):

    if branchLen > 5:
        t.forward(branchLen)
        t.right(randint(15, 45))
        #t.color(randint(0,255), randint(0,255), randint(0,255))
        t.width(width-3)

        if branchLen > 25:
            t.color("brown")

        if branchLen < 25:
            t.color("green")        

        tree(branchLen-15, t, width-3)
        t.left(randint(15,45))        
        #t.color(randint(0,255), randint(0,255), randint(0,255))
        t.width(width-3)
        tree(branchLen-15, t, width-3)
        t.right(randint(15,45))
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    turtle.colormode(255)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(95, t, 20)
    myWin.exitonclick()

main()

#print randint(0,255), randint(0,255), randint(0,255)
