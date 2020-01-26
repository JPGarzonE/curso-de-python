# como vamos a usar python3 no ponemos el encabezado de utf-8
# otra cosa en python3 se usa { nombreVariable = input('Texto De Pregunta') } a diferencia de python 2.7 que usa raw_input

# funciones

import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)
    turtle.mainloop()

def make_square(dave):
    length = int(input("Tamaño de cuadrado: "))

    for i in range(4):
        make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)

if __name__ == '__main__':
    main()
