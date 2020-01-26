# Decoradores en Python
# Un decoradores una función que recibe otra función y regresa una tercera función.
# Para reconocer un decorador, puedes ver que tienes un arroba sobre la declaración de una función.

# IMPORTANTE:
# Los decoradores se utilizan para extender la funcionalidad de una función

# Por ejemplo aquí hay una función en la que se despliega un mensaje (protected_func)
# y es llamada en el main del programa, a dicha funcion se le agrega un decorador
# con el nombre propio de la función decoradora (protected), dicha funcion decoradora lo que hace es
# crear una funcion (wrapper) que le agrega código a la primera funcion (protected_func).
# En este caso lo que hace es validar un parametro ingresado por el usuario para poder
# ejecutar la funcion (protected_func)
def protected(func):

    def wrapper(password):

        if password == 'platzi':
            return func() # funcion principal que llega por param
        else:
            print('La contraseña es incorrecta')

    return wrapper


@protected
def protected_func():
    print('Tu contraseña es correcta.')

# SEGUNDO EJEMPLO:
def decorador(funcion):
    def nueva_funcion():
        print("La función se va a ejecutar") # Código que se va a realizar antes de la llamada a la funcion por param
        funcion()
        print("Se ejecutó la funcion") # Código que se va a ejecutar despues de la llamada la funcion principal por param

    return nueva_funcion # retorna la funcion que le agrego código a otra

@decorador # decorador que llama a la funcion decoradora previamente creada a partir de su nombre
def saludo():
    print("Hola mundoooooo")


# cuando el programa en algun punto llama a las funciones "decoradas" se ejecuta el código completo:
# tanto el agregado por el decorador como el principal que se llama en el decorador
if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))
    protected_func(password)

    input('Enter para el segundo ejemplo: ')
    saludo()
