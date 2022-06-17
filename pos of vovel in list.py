#print pos of vovel in list under a constrain
z=[]
v='aeiou'
for i in range (int(input("no. of string"))):
    a=input("enter elements: ")
    if len(a)>3:
        print("enter upto 3 char")
        break
    else:
        for j in a:
            if j in v:
                z.append(a.index(j))
                a=a.replace(j,'2',1)
print(z)