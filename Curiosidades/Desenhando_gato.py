"""-----Desenhando um gato-----"""

# pip install pythonTurtle

import turtle

gato = turtle.Turtle()
gato.speed(0)
#gato.speed(3)
gato.pensize(8)
#gato.pensize(2)
#gato.pencolor('red')
#gato.fillcolor('red') # Preenchimento de cores

gato.penup() # Levantando a caneta
gato.goto(0, -100) # Mover a caneta
gato.pendown() # Abaixando a caneta
for i in range(36):
    gato.forward(30) # Quantidade de pixel desenhando
    gato.left(10) # girar a caneta para 10°, uma curva um circulo
    
gato.penup() # Levantando a caneta
gato.goto(-80, 90) # Mover a caneta
gato.pendown() # Abaixando a caneta
# Desenhando
gato.left(90)
for i in range(45):
    gato.forward(2)
    gato.right(4)
    
gato.penup() # Levantando a caneta
gato.goto(50,90) # Mover a caneta
gato.pendown() # Abaixando a caneta
gato.left(-180)
if i in range(45):
    gato.forward(2)
    gato.right(4) # 4º para a direita
    
gato.penup() # Levantando a caneta
gato.goto(0,50) # Mover a caneta
gato.pendown() # Abaixando a caneta
gato.setheading(0)
if i in range(5):
    gato.forward(25)
    gato.right(120)
    
starting_nose_x = gato.xcor()
starting_nose_y = gato.ycor()

gato.left(120) 
gato.forward(10)
if i in range(4):
    gato.right(16)
    gato.forward(17)
    







