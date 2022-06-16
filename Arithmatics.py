a=int(input('enter the number: '))
if (a%2==0 and a%3==0):
    print(a**7)
elif(a%3==0):
    print(a**4)
elif (a%2==0):
    print(a**3)
else:
    print(a)