##Number closest multiple of 6 and 8
a=int(input())
b=a-(a//6)*6
c=a-(a//8)*8
if(b<3):
    print((a//6)*6)
else:
    print(((a//6)+1)*6)
if(c<4):
    print((a//8)*8)
else:
    print(((a//8)+1)*8)