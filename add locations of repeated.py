#add locations of repeated num
a=input()
s=1
z=0
c=''
for i in a:
    if s<=a.count(i):
        s=a.count(i)
for j in a:
    if a.count(j)==s:
        c=j
for g in a:
    if g==c:
        z+=a.index(c)
        a=a.replace(c,'2',1)
print(z)