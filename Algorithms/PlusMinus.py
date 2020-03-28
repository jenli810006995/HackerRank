import os

def plusMinus(arr):
    pos=0
    neg=0
    zero=0
    for i in range(0, n):
        if int(arr.split(' ')[i]) >0: # positive
            pos+=1
        elif int(arr.split(' ')[i])==0: # zero
            zero+=1
        elif int(arr.split(' ')[i])<0:
            neg+=1
    return str(round(pos/n,6))+'\r\n'+str(round(neg/n,6))+'\r\n'+str(round(zero/n,6))

n=int(input().strip())
arr=str(input().strip())
result=plusMinus(arr)
print(result)