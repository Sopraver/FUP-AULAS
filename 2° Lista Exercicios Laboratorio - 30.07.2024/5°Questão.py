nota1 = float(input("digite o valor da 1° avaliação:"))
nota2 = float(input("digite o valor da 2° avaliação:"))

soma = nota2+nota1
media = soma/2
print("Sua media é:",media)
if media >= 7:
    print("Aprovado")
if media >= 4 and media< 7 :
    print("Realizar a Prova Final")
if media<4:
    print("Reprovado")