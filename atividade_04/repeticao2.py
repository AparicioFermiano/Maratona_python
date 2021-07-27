import math
resultado = list()
for x in resultado:
    try:
        aux = input().split (' ')
        n1 = int(aux[0])
        n2 = int(aux[1])
        x = math.pow(n1, n2)
        x = round(resultado,None)
        x += 1
        if resultado > 0:
            print(resultado)
    except EOFError:
        break

    #print(resultado[0:len[resultado]-1])