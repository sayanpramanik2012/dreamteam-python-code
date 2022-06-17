#Armstrong number
e =input("Enter a number: ")
sum = 0
for i in e:
    sum+=int(i)**len(e)
print(sum==int(e))