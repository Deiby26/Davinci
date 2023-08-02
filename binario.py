def binary(numero, lista):
    if numero // 2 == 1:
        lista.append(int(numero%2))
        lista.append(1)
        return lista
    else:
        lista.append(int(numero%2))
        return binary(numero= numero/2, lista=lista)
newlist = []
for i in reversed(binary(numero=int(input("Ingrese un numero: ")), lista=[])):
    newlist.append(i)
print(newlist)