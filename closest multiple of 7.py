#Number is multiple of 5 and odd print he closest multiple of 7
a=(int(input('Enter the value: ')))
b=a-(a//7)*7
if(a%2 != 0 and a%5==0):
    if(b<4):
        print((a//7)*7)
    else:
        print(((a//7)+1)*7)
else:
    print("try again")