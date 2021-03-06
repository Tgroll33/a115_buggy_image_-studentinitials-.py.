import turtle as trtl

# make the spider's body

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

# configure legs

legs = 8
leg_length = 70
leg_direction = 360 / legs
spider.pensize(5)
limit = 0

# make the spider's legs

while (limit < legs):
  spider.goto(0,20)
  spider.setheading(leg_direction*limit)
  spider.forward(leg_length)
  limit = limit + 1
spider.hideturtle()
wn = trtl.Screen()
