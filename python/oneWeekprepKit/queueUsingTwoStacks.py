# Enter your code here. Read input from STDIN. Print output to STDOUT

numOfqueries = int(input())
commands = []
for _ in range(numOfqueries):
    commands.append(list(map(int, input().split())))
    
# print(commands)

inputStack = []
outputStack = []
for command in commands:
    if len(command) == 2:
        inputStack.append(command[1])
    elif command[0] == 2:
        if (len(outputStack)==0):
            while inputStack:
                outputStack.append(inputStack.pop())
        outputStack.pop()
    else:
        if (len(outputStack)==0):
            while inputStack:
                outputStack.append(inputStack.pop())
        print(outputStack[len(outputStack)-1])