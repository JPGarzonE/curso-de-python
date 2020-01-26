def main():
    for i in range(100):
        printFizzBuzzNumber( i+1 )

def printFizzBuzzNumber( number ):
    valorImprimir = number

    if (number % 3) == 0:
        valorImprimir = 'Fizz'

    if (number % 5) == 0:
        if valorImprimir == 'Fizz':
            valorImprimir += 'Buzz'
        else:
            valorImprimir = 'Buzz'

    print(valorImprimir)

if __name__ == '__main__':
    main()
