from scripts import control as c
import turtle
s=c.mo
wn=turtle.getscreen()
wn.bgcolor("Beige")
s.shape("turtle")
s.color("Green")
s.pensize(3)
wn.onkey(c.forward,'Up')
wn.onkey(c.backward, 'Down')
wn.onkey(c.right, 'Right')
wn.onkey(c.left, 'Left')
wn.listen()

wn.exitonclick()