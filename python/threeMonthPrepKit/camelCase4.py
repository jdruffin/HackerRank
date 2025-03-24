# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

lines = sys.stdin.readlines()

for line in lines:
    Input = line.strip().split(";")
    operation = Input[0]
    Type = Input[1]
    word = Input[2]
    if operation=="S":
        res=""
        for i in word:
            if i.isupper() and not res:
                res+=i.lower()
            elif i.isupper() and res:
                res+=" "+i.lower()
            elif i=="("or i==")":
                continue
            else:
                res+=i
        print(res)
    elif operation=="C":
        String=word.split()
        res=String[0].lower()
        if Type=="C":
            res=res.capitalize()
        for i in String[1:]:
            res+=i.capitalize()
        if Type=="M":
            res+="()"
        print(res)