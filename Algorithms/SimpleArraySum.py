def simpleArraySum(ar):
    return sum(ar)

n=input().strip()
ar=list(map(int,input().split()))
result=simpleArraySum(ar)
print(result)