import turtle as trtl

# make the spider's body

spider = trtl.Turtle()
spider.pensize(40)
spider.color("black")
spider.circle(20)

# configure legs

legs = 4
leg_length = 70
leg_direction = 120 / legs
spider.pensize(5)
limit = 0

# make the spider's legs

while (limit < legs):
  spider.goto(0,20)
  spider.setheading(leg_direction*limit+45)
  spider.forward(leg_length)
  limit = limit + 1
limit = 0
leg_direction = -120 / legs
while (limit < legs):
  spider.goto(0,20)
  spider.setheading(leg_direction*limit-45)
  spider.forward(leg_length)
  limit = limit + 1
spider.hideturtle()
wn = trtl.Screen()

# make the lil eyes

spider.penup()
spider.color("red")
spider.goto(10,40)
spider.pensize(10)
spider.pendown()
spider.circle(5)

spider.penup()
spider.goto(10,5)
spider.pensize(10)
spider.pendown()
spider.circle(5)
