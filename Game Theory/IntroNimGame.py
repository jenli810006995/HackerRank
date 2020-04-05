import math
import os
import random
import re
import sys
from functools import reduce

def nimGame(pile):
    res=reduce((lambda x,y: x^y), pile)
    if res == 0:
        return "Second"
    else:
        return "First"

g = int(input())

for _ in range(g):
    n = int(input())
    pile = list(map(int, input().rstrip().split()))
    result = nimGame(pile)
    print(result)
