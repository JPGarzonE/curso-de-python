def main():
    print("C A L C U L A D O R A   D E   F A C T O R I A L")
    numero = int( input("¿Cuál es tu numero? ") )
    resultado = factorial(numero)
    print("El factorial de {} es {}".format(numero, resultado))

def factorial(numero):
    if numero == 1 :
        return 1
    else:
        return numero * factorial(numero-1)

if __name__ == "__main__":
    main()
