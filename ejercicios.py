def search(elementos, término):
    for i in range(elementos):
        if elementos[i] == término:
            print("(0) se encontró en la lista.".format(término))
        else:
            print("(0) no se encontró en la lista.".format(término))
        break

search(2,4)