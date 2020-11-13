#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

legs = 6
leg_length = 70
leg_direction = 380 / legs
spider.pensize(5)
limit = 0
# this iteration shows how many legs are made before the program is terminated.
while (limit < legs):
  spider.goto(0,0)
  spider.setheading(leg_direction*limit)
  spider.forward(leg_length)
  limit = limit + 1
spider.hideturtle()
wn = trtl.Screen()
