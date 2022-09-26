import turtle

# Dimenzije i naslov aplikacije
screen = turtle.Screen()
screen.setup(width = 750, height = 750)
screen.title("Slaganje oblika")

# Velicina i ugao oblika
size = 1
rotation = 0

# Oblik
changed_shapes = 0
changed_shapes_arr = ["arrow", "circle", "square", "triangle", "classic", "turtle"]

# Boja i lista boje
color = 0
color_arr = ['#000000',
             '#C0C0C0', '#808080', '#FFFFFF', 
             '#800000', '#FF0000', '#800080', 
             '#FF00FF', '#008000', '#00FF00', 
             '#808000', '#FFFF00', '#000080', 
             '#0000FF', '#008080', '#00FFFF']

# Niz postavljenih oblika
shapes = []

# Text u uglu
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.speed(0)
text.color('red')
text.setposition(-370, 320)
mess = 'Uputstvo:\n Strelice - Pomeranje Z, X -> Rotiranje; C -> Menjanje boje;\n Space -> Menjanje oblika; Enter -> Postavi blok; +, - -> Menjanje velicine'
text.write(mess, False, align="left", font=("Arial", 11, "normal"))

# Oblik koji moze da se pomera
player = turtle.Turtle()
player.penup()
player.shape(changed_shapes_arr[0])
player.color(color_arr[color])

# Pomeranje
def left():
  x = player.xcor() - 1
  player.setposition(x, player.ycor())

def right():
  x = player.xcor() + 1
  player.setposition(x, player.ycor())

def up():
  y = player.ycor() + 1
  player.setposition(player.xcor(), y)

def down():
  y = player.ycor() - 1
  player.setposition(player.xcor(), y)

def change_shape():
  global changed_shapes
  changed_shapes += 1
  if(changed_shapes == len(changed_shapes_arr)):
    changed_shapes = 0
  player.shape(changed_shapes_arr[changed_shapes])

# Menjanje velicine
def size_up():
  global size
  if(size < 5):
    size += 0.05
  player.shapesize(size, size)

def size_down():
  global size
  if(size > 0.10):
    size -= 0.05
  player.shapesize(size, size)
  
# Rotiranje  
def rotate_left():
  global rotation
  if(rotation + 5 == 360):
    rotation = 0
  rotation += 5
  player.setheading(rotation)

def rotate_right():
  global rotation
  if(rotation - 5 == 0):
    rotation = 365
  rotation -= 5
  player.setheading(rotation)

# Menjanje boje
def change_color():
  global color
  color += 1
  if(color == len(color_arr)):
    color = 0
  player.color(color_arr[color])

# Postavljanje oblika
def submit():
  # Dodavanje postavljenih oblika
  shapes.append(turtle.Turtle())

  # Podesavanje zadnjeg oblika
  shapes[-1].speed(0)
  shapes[-1].penup()
  shapes[-1].setposition(player.xcor(), player.ycor())
  shapes[-1].color(color_arr[color])
  shapes[-1].shapesize(size)
  shapes[-1].setheading(rotation)
  shapes[-1].shape(changed_shapes_arr[changed_shapes])

# Komande sa tastature
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(change_shape, "space")
screen.onkeypress(size_up, "plus")
screen.onkeypress(size_down, "minus")
screen.onkeypress(rotate_left, "z")
screen.onkeypress(rotate_right, "x")
screen.onkeypress(change_color, "c")
screen.onkeypress(submit, "Return")

screen.listen()
screen.mainloop()