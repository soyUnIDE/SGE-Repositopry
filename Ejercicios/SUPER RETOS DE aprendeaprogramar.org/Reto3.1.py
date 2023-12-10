numero=int(input())
if numero%2!=0:
    numero-=1
for i in range(1,numero+1):
    if i%2==0:
        print(i)