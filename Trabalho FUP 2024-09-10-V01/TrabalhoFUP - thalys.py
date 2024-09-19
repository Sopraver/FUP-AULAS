mm = int(input("Digite seu mês de nascimento: "))
dd = int(input("Digite o dia do seu nascimento: "))
aa = int(input("Digite o ano do seu nascimento: "))

if mm > 9:
    id = 2024-aa-1
    mm = 9
    if dd > 15:
        dd = 15

    else:
        dd = 15 - dd

else:
    if dd>15:
        id = 2024 - aa - 1
        mm = 9 - mm - 1
        dd = 15
    else:
        id = 2024 - aa
        mm = mm-9
        dd = 15 - dd

id = id * 365 + mm * 30 + dd
print(id)