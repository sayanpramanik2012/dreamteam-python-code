#get the vovel pos and multiply by 5
str="python"
vow="aeiou"
for i in range (0,len(str)):
    if str[i] in vow:
        a=i**5
        print(a,end="")
    else:
        print(str[i],end="")