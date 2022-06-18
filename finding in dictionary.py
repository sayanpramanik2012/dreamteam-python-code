#finding in dic
m= {}
for i in range(int(input('enter size'))):
    number = input("Enter number: ")
    name = input("Enter name: ")
    m[number]=name
print(m)
print(m.get(input("enter the key"),'Not found'))