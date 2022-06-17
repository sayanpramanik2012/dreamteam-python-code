from dataclasses import replace
from re import I


#replace max count in str
a=input()
s=1
c=''
for i in a:
    if s<=a.count(i):
        s=a.count(i)
for j in a:
    if a.count(j)==s:
        c=j
        a=a.replace(c,'z')
print(a)