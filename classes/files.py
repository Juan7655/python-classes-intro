# leer e iterar sobre un archivo. Uso mas comun
def read():
    f = open('myText.txt', mode='rt', encoding='utf-8')

    for i in f:
        print(i)

    f.close()


# modo escritura. Saca error al no ser de lectura
def writeNotRead():
    f = open('myText.txt', mode='wt', encoding='utf-8')

    for i in f:
        print(i)

    f.close()


# Modo escribir. Sobrescribe lo que haya
def overwrite():
    f = open('myText.txt', mode='wt', encoding='utf-8')

    f.write("texto para escribir")
    f.close()


# Modo append. Inserta el texto al final de lo existente
def appendText():
    f = open('myText.txt', mode='at', encoding='utf-8')

    f.write("texto para escribir")

    f.close()


# Modo de sólo lectura
def readOnly():
    # f.read()
    # f.readline()

    with open('myText.txt', mode='rt', encoding='utf-8') as f:
        for i in f:
            print(i)

    f.close()


readOnly()
# appendText()
# overwrite()
# writeNotRead()
# read()


# fh.read()
# fh.readlines()
# fh.readline()
