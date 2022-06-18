#reversing phone number
z=list(map(int,input().strip('')))
b=int(input('integer input'))
for i in range (b):
    z=z[-1:]+z[:-1]
    print(z)
