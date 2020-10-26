inputList=[1,9,8,4,7,5,3,6,77,405,541,6464,874984321,97456498751,50]

for i in range(len(inputList)):
    minPos=i
    for j in range(i,len(inputList)):
        if(inputList[j]<inputList[minPos]):
            minPos=j
    temp= inputList[i]
    inputList[i]=inputList[minPos]
    inputList[minPos]=temp
print(inputList)
