"""-----

Desenhando um gato

Comentar: CTRL + K, CTRL + C
Descomentar: CTRL + K, CTRL + U
Ambos (toggle): CTRL + ;

-----"""

# pip install pythonTurtle

import turtle

gato = turtle.Turtle()
gato.speed(0)
# gato.speed(3)
gato.pensize(8) # Pincel nº 8
# gato.pensize(2)
# gato.pencolor('red')
# gato.fillcolor('red')

gato.penup() # Levanta a caneta
gato.goto(0, -100) # Move a caneta
gato.pendown() # Abaixa a caneta
for i in range(36):
    gato.forward(30)
    gato.left(10)

gato.penup()
gato.goto(-80, 90)
gato.pendown()
gato.left(90) # Virando a caneta
for i in range(45):
    gato.forward(2)
    gato.right(4)

gato.penup()
gato.goto(50, 90)
gato.pendown()
gato.left(-180) # Virando a caneta
for i in range(45):
    gato.forward(2)
    gato.right(4)

gato.penup()
gato.goto(0, 50)
gato.pendown()
gato.setheading(0) # via a caneta para todos os lados (0) direita
for i in range(5):
    gato.forward(25)
    gato.right(120)

starting_nose_x = gato.xcor() # posição da caneta em x cordenada
starting_nose_y = gato.ycor()  # posição da caneta em y cordenada

gato.left(120)
gato.forward(10)
for i in range(4):
    gato.right(16)
    gato.forward(17)

gato.penup()
gato.goto(starting_nose_x, starting_nose_y)
gato.pendown()
gato.setheading(-60)
gato.forward(10)
for i in range(4):
    gato.left(16)
    gato.forward(17)

gato.penup()
gato.goto(-19, -10)
gato.pendown()
gato.right(100)
for i in range(10):
    gato.forward(12)
    gato.left(21)

gato.penup()
gato.goto(114, 212)
gato.pendown()
gato.forward(100)
gato.left(120)
gato.forward(75)

gato.penup()
gato.goto(-107, 193)
gato.pendown()
gato.setheading(75)
gato.forward(100)
gato.right(120)
gato.forward(75)
# gato.ht()
turtle.done()





