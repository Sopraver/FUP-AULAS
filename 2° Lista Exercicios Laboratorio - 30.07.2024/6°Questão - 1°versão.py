vi = int(input("Valor Inicial do somatorio:"))
vf = int(input("Valor Final do somatorio:"))

pares = 0
impares = 0
lista = []

for i in range(vi,vf+2):
   lista.append(i)

   if (i%2) == 0:
      pares = pares + 1
   else:
      impares = impares+1

print("Valores da Sequencia:")
print(lista)
print("\nMedia Pares:", pares)
print("Media Impares:", impares)
somalista = sum(lista)
print("Somatorio:",somalista)