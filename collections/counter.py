#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

from collections import Counter
entry=int(input())
shoe_collection=input().split()
counters=Counter(shoe_collection)
counters=dict(counters)
customers=int(input())
amount=int(0)
for i in range(customers):
    customer_input=input().split()
    #print( customer_input) 
    #print(counters.get(customer_input[0]))
    if customer_input[0] in counters.keys() and int(counters[str(customer_input[0])])>0:
        counters[str(customer_input[0])]=int(counters[str(customer_input[0])])-1
        amount=amount+int(customer_input[1])
    
print(amount)



