from random import randint
import turtle

def tree(branchLen,t,width):
    if branchLen <= 10:
        t.color("brown")

    if branchLen > 5:
        t.width(width-4)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t,width-4)
        t.left(40)
        tree(branchLen-15,t,width-4)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.width(20)
    t.color("green")
    tree(75,t,20)
    myWin.exitonclick()

main()

