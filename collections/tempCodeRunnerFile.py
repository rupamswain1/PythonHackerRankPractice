from collections import Counter
entry=int(input())
shoe_collection=input().split()
counters=Counter(shoe_collection)
customers=int(input())
amount=int(0)
for i in range(customers):
    customer_input=input().split()
    if(int(shoe_collection[int(customer_input[0])])>0):
    
        shoe_collection[int(customer_input[0])]=int(shoe_collection[int(customer_input[0])])-1
        amount=amount+int(customer_input[1])
    
print(amount)



