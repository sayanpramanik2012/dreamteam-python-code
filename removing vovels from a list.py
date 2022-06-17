#removing vovels from a list of words
z=[]
v='aeiou'
blank=''
for i in range (int(input("no. of string"))):
    a=input("enter elements: ")
    for j in a:
        if j not in v:
            blank+=j
    z.append(blank)
    blank=""
print(z)