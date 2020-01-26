import math

def binarySearch(numbers, numberToSearch, idxBottom, idxTop):
    if idxBottom > idxTop:
        return False

    idxMiddle = math.floor( (idxTop + idxBottom) / 2 )
    
    if numbers[idxMiddle] == numberToSearch:
        return True
    elif numbers[idxMiddle] > numberToSearch:
        return binarySearch( numbers, numberToSearch, idxBottom, idxMiddle - 1 )
    else:
        return binarySearch( numbers, numberToSearch, idxMiddle + 1, idxTop )

def main():
    numbers = [2,4,8,13,14,15,19,20,22,23,24,28]
    numberToSearch = int( input("Ingresa un número: ") )

    result = binarySearch( numbers, numberToSearch, 0, len( numbers ) - 1 )

    if result is True:
        print('El numero si está en la lista')
    else:
        print('El numero NO se encuentra')

if __name__ == '__main__':
    main()
