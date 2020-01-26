import random

def run():
    number_found = False
    topRange = int( input("¿Hasta que numero quieres adivinar?") )
    random_number = random.randint(0, topRange)

    while not number_found:
        number = int(input('Intenta un número:'))

        if number == random_number:
            print('Felicidades. Encontraste el número')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')


if __name__ == '__main__':
    run()
