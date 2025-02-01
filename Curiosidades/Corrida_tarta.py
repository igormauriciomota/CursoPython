"""-----Corrida de tartarugas-----"""

# # Corrida de Tartarugas
#
# # pip install PythonTurtle
# import turtle
# from turtle import *
# from random import *
#
# penup()
# goto(-140,140)
#
# for linha in range(16):
#     if linha == 15:
#         pencolor('red')
#     speed(0)
#     write(linha)
#     right(90)
#     forward(10)
#     pendown()
#     forward(150)
#     penup()
#     backward(160)
#     left(90)
#     forward(20)
#
#
# rafael = Turtle()
# rafael.color('red')
# rafael.shape('turtle')
# rafael.penup()
# rafael.goto(-160,100)
# rafael.pendown()
#
# michelangelo = Turtle()
# michelangelo.color('purple')
# michelangelo.shape('turtle')
# michelangelo.penup()
# michelangelo.goto(-160,75)
# michelangelo.pendown()
#
# donatello = Turtle()
# donatello.color('orange')
# donatello.shape('turtle')
# donatello.penup()
# donatello.goto(-160,50)
# donatello.pendown()
#
# leonardo = Turtle()
# leonardo.color('blue')
# leonardo.shape('turtle')
# leonardo.penup()
# leonardo.goto(-160,25)
# leonardo.pendown()
#
# for rodada in range(200):
#     rafael.forward(randint(1, 5))
#     michelangelo.forward(randint(1, 5))
#     donatello.forward(randint(1, 5))
#     leonardo.forward(randint(1, 5))
#     if rafael.xcor() >= 170:
#         print('Rafael venceu!')
#         break
#     elif michelangelo.xcor() >= 170:
#         print('Michelangelo venceu!')
#         break
#     elif donatello.xcor() >= 170:
#         print('Donatello venceu!')
#         break
#     elif leonardo.xcor() >= 170:
#         print('Leonardo venceu!')
#         break
#
# turtle.done()
