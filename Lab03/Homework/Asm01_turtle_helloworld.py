from turtle import *
def print_hello_word():
    color("green")
    for i in range (3):
        write("Hello world")
        penup()
        right(90)
        forward(10)
        left(90)

print_hello_word()
mainloop()