#strong number
a=input()
sum=0
for i in a:
    fac=1
    for j in range (1,int(i)+1):
        fac=fac*j
    sum=sum+fac
print(sum==int(a))