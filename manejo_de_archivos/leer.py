def run():
    wordToFound = str( input("¿De cuál palabra quieres saber la cantidad de veces que aparece en el texto?") )
    counter = 0
    with open("aleph.txt", encoding="utf-8") as alephFile:
        for line in alephFile:
            counter += line.count(wordToFound)

    print( "La palabra {} se encuentra {} veces en el texto".format(wordToFound, counter) )

if __name__ == "__main__":
    run()
