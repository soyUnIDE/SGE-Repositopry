numero=int(input())
if numero%2==0:
    numero-=1
for i in range(numero,1-1,-2):
    if i%2!=0:
        print(i)