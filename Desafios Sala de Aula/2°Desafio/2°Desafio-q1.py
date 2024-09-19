import math

somatorio = []

print("UFC - Programação - 2024.1")
print("2°Desafio q1:")
n = int(input("\nDigite um numero: "))
while n>0:
    print("\nValor de n:",n)
    if n<5 :
        print("n é menor que 5: Sim")
    if n>5 :
        print("n é menor que 5: Não")
    raiz_quadrada = math.sqrt(n)
    print("raiz quadrada de n: ",raiz_quadrada)
    elevado_cubo = pow(n,3)
    print("Valor de n ao cubo: ",elevado_cubo)
    resto2 = n%2
    resto3 = n%3
    print("Resto da divisão de n por 2: ",resto2)
    print("Resto da divisão de n por 3: ",resto3)

    somatorio.append(n)

    n = int(input("\nDigite um numero: "))
print("\nSomatório dos n’s = ", sum(somatorio))
print("Quantidade de n’s = ", len(somatorio))