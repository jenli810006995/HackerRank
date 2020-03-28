import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr): # there are five combination of index orders
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    p1+=int(arr.split(' ')[0])+int(arr.split(' ')[1])\
+int(arr.split(' ')[2])+int(arr.split(' ')[3])
    p2+=int(arr.split(' ')[0])+int(arr.split(' ')[2])+int(arr.split(' ')[3])+int(arr.split(' ')[4])
    p3+=int(arr.split(' ')[1])+int(arr.split(' ')[2])+int(arr.split(' ')[3])+int(arr.split(' ')[4])
    p4+=int(arr.split(' ')[0])+int(arr.split(' ')[1])+int(arr.split(' ')[3])+int(arr.split(' ')[4])
    p5+=int(arr.split(' ')[0])+int(arr.split(' ')[1])+int(arr.split(' ')[2])+int(arr.split(' ')[4])
    return str(min(p1,p2,p3,p4,p5))+' '+str(max(p1,p2,p3,p4,p5))

arr=input().strip() # an 5 element array
result=miniMaxSum(arr)
print(result)