#missing number in phone number
a=list(map(int,input().strip('')))
i=[0,1,2,3,4,5,6,7,8,9]
for z in i:
    if z not in a:
        print(z, end=' ')