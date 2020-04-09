def nimbleGame(s):
    a=[]
    for i in range(n):
        a+=[i]*(s[i]%2) # if the number is even, a would be zero
    if a==[]:
        return "Second"
    else:
        return "First" if reduce((lambda x, y : x^y) ,a) else "Second"

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().rstrip().split()))
    result=nimbleGame(s)
    print(result)