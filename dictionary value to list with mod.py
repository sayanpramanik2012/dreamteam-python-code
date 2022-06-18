#dic value to listwith modification
m= {}
l=[]
for i in range(int(input('enter size'))):
    number = int(input("Enter number: "))
    name = int(input("Enter name: "))
    m[number]=name
print(m)
a=m.get(int(input("enter the key")))
for i in m:
    if int(m[i])%2==0:
        l.append(int(m[i])**5)
    else:
        l.append(int(m[i])**3)
print(l)