#Find sum of factor of all loc of consonant
fact = lambda n: 1 if n <= 1 else n*fact(n-1)
v = 'aeiouAEIOU'
s = []
a = [i for i in input().strip()]
for i in range(len(a)):
    if a[i] not in v:
        s.append(fact(i))
print(s)
print(sum(s))