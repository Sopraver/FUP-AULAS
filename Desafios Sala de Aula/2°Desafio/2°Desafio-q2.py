thalysA = str(input("Digite o valor da string A: "))
thalysB = str(input("Digite o valor da string B: "))

s = list(thalysA)
d = list(thalysB)
c= []
n = 0

while True:
    if n< len(s):
        c.append(s[n])

    if n< len(d):
        c.append(d[n])
    
    n = n+1
    if n > len(s) + len(d):
        break


thalysC = "".join(c)
print(thalysC)