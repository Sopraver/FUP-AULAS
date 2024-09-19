N = int(input("Digite Valor N-final: "))

print  ("UFC - Programação - 2024.1")
print("\nNome: xxxxxx xxxxxxxx")
print ("Sequencia de Fibonacci: \n")

list = [0,1]
print(list)
i = 1
list.append(i)
print(list)




while i < N:
    if i > 0:
        i = i + list[-2]
        list.append(i)
    print(list)

