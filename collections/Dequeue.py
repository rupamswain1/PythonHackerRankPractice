from collections import deque


inp=int(input())
d=deque()
for i in range(0,inp):
    inst=input().split()
    queInst=inst[0]
    if(len(inst)>1):
        data=inst[1]
    if(queInst == 'append'):
        d.append(data)
    elif(queInst == 'pop'):
        d.pop()
    elif (queInst == 'pop'):
        d.pop(data)
    elif(queInst == 'appendleft'):
        d.appendleft(data)
    elif(queInst == 'clear'):
        d.clear()
    elif(queInst == 'extend'):
        d.extend(data)
    elif(queInst == 'extendleft'):
        d.extendleft(data)
    elif(queInst == 'remove'):
        d.remove(data)
    elif(queInst == 'reverse'):
        d.reverse()
    elif(queInst == 'rotate'):
        d.rotate(data)
    elif (queInst == 'popleft'):
        d.popleft()
for n in d:
    print(n,end=" ")

