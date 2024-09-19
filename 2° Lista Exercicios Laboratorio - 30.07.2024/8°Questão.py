N = int(input("digite N:"))
lista = []
multiplicador = 1

while N > 0:
    lista.append(N)
    N= N-1

for x in lista:
    multiplicador *= x

print("\n",lista)
print("fatorial: ",multiplicador)