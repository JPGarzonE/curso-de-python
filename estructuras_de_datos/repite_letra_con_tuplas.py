# Vamos a construir un programa que nos permita encontrar el primer carácter que no se repite en un string.
# Por ejemplo si tenemos el string mimamameama el primer carácter que no se repite es la i.

# Mi reto
def first_not_repeating_char_my_method(char_sequence):
    sequence_tuple = tuple(char_sequence)
    not_repeating_char = '_*'
    for idx in range( len(sequence_tuple) ):
        if sequence_tuple.count( sequence_tuple[idx] ) == 1:
            not_repeating_char = sequence_tuple[idx]
            break

    return not_repeating_char

# Metodo hecho por el profe
def first_not_repeating_char_teachers_method(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for key, value in seen_letters.iteritems():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char_my_method(char_sequence)

    if result == '_*':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))
