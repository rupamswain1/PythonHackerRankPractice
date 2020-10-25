inputList=[1,7,8,6,5,2,3,4]
inputList.sort()
print(inputList)
user=int(input())
start=0
end=len(inputList)-1

mid=(end+start)//2
found=False
iteration=0
while(start<=end and found==False):
    mid = (start + end) // 2
    iteration+=1
    if (inputList[mid] == user):
        found = True
        print("Number found at sorted index: ", mid)
        print("Total iteration: ",iteration)
    if (inputList[mid] < user):
        start = mid+1
    elif(inputList[mid]>user):
        end=mid-1



