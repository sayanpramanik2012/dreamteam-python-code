#roating list at a pos
a=int(input('enter the size: '))
z=[]
for i in range (0,a):
    z.append(input("enter element"))
b=int(input('integer input'))
for i in range (b):
    z=z[-1:]+z[:-1]
    print(z)
