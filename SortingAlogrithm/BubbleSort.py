inputList=[1,9,8,4,7,5,3,6,77,405,541,6464,874984321,97456498751,50]

for i in range(len(inputList), 0, -1):
    for j in range(0 ,i-1):
        if(inputList[j+1]<inputList[j]):
            temp=inputList[j]
            inputList[j]=inputList[j+1]
            inputList[j+1]=temp
print(inputList)