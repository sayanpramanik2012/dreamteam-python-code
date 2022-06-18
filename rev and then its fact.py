#reverse and then its factorial
z=[]
for i in range (int(input("enter the size: "))):
    a=(input('Enter the enter the number: '))
    if len(a)==2:
        z.append(a)
    else:
        print("Try 2 digit number")
for i in z:
    fact=1
    for k in range(1,int(i[::-1])+1):
        fact=fact*k
    print (fact)