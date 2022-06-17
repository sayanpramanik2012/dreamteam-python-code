#vovel pos factorial
a=(input())
b=(input())
c=(input())
d=(input())
e= a+" "+b +" "+c+" "+ d
print(e)
vow ="aeiou"
for i in range(len(e)):
    if e[i] in vow:
        fact=1
        for j in range(1,i+1):
            fact=fact*j
        print(fact,end=" ")