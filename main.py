#   a123_apple_1.py
import turtle as trtl
t = trtl.Turtle()
drawer = trtl.Turtle()
drop = trtl.Turtle()
apple = trtl.Turtle()
#-----setup-----
wn = trtl.Screen()

apple_image = "apple.gif" # Store the file name of your shape

wn.setup(width=1.0, height=1.0)

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

  drawer.color("white")
  drawer.write("A", font=("Arial", 74, "bold"))

def drop_apple():
  apple.penup()
  apple.goto(0, -150)
  apple.hideturtle()

wn.onkeypress(drop_apple)
wn.listen()
wn = trtl.Screen()
wn.bgpic("background.gif")
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
#-----function calls-----
draw_apple(apple)

apple.clear()
wn.mainloop()