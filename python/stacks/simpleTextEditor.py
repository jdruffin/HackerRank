# Enter your code here. Read input from STDIN. Print output to STDOUT

numberOfQueries = int(input())

stackOfWriteOperations = []
text = ''

for query in range(numberOfQueries):
    inputList = list(input().split(' '))
    if(len(inputList) == 2):
        if (inputList[0] == '1'):
            stackOfWriteOperations.append([1,inputList[1]])
            text += str(inputList[1])
        elif (inputList[0] == '2'):
            deletedText = text[-int(inputList[1]):]
            text = text[:-int(inputList[1])]
            stackOfWriteOperations.append([2, deletedText])
        else:
            print(text[int(inputList[1])-1])
    else:
        operation, value = stackOfWriteOperations.pop()
        if(operation == 1):
            text = text[:-int(len(value))]
        else:
            text+= value