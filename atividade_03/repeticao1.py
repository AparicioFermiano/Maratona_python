t = input()
s = ''
v = 1
while True:
    try:
        aux = input().split (' ')
        n1 = int(aux[0])
        n2 = int(aux[1])
        resultado = max(n1, n2)
        s += f'Caso de Teste {v}: {resultado}\n'
        v += 1
    except EOFError:
        break
print(s[0:len[s]-1], end='')