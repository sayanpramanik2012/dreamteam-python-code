# Roatate the list and check condition
import math
l=[]
for i in range (int(input('No. of elements'))):
    l.append(int(input('Enter Elements: ')))
print(l)
for j in range(int(input('enter the number of line'))):
    if (l[-1]%2)==0:
        l.insert(0,math.factorial(l[-1]))
        l.pop()
        print(l)
    else:
        l.insert(0,l[-1]**(1/2))
        l.pop()
        print(l)