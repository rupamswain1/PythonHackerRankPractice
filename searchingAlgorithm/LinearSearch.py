inputList=[2,4,5,8,9,10,88,99,50,414,45,11,45,5,4,5,74,1,55,141,44,55,44,41,11,44,77,88,565,22,1]
input=int(input("Enter the number to be searched"))
flag=False
for i in range(0,len(inputList)):
    if inputList[i]==input:
        
        print("Number found at index: ",i)
        flag=True
if(flag==False):
    print("Number not found")
