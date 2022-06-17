#repeated even&odd replace them by 0&1
a=input()
for i in a:
    if (a.count(i)%2==0):
        a=a.replace(i,'1')
    else:
        a=a.replace(i,'0')
print(a)