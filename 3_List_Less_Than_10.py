givenList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

newList=list()
newStr=""

for element in givenList:
    if(element > 5):
        newList.append(element)


for x in newList:
    newStr = newStr+str(x)+", "

print(newStr)

