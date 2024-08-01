i = int(input("Valor de M = "))
n = int(input("Valor de N = "))
list = []
pares = 0
impares = 0

while i <= n:
    list.append(i)
    if (i % 2) == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    i = i+1

print("Valores da Sequencia:")
print(list)
print("\nMedia Pares:", pares)
print("Media Impares:", impares)
somalista = sum(list)
print("Somatorio:",somalista)