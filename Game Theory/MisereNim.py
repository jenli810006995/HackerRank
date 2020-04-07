import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the misereNim function below.
def misereNim(s):
    nimSum=0
    outcome=1
    for n in s:
        if n > 1:
            outcome=0
        nimSum^=n
    if nimSum == outcome:
        return "Second"
    return "First"

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().rstrip().split()))
    result = misereNim(s)
    print(result)