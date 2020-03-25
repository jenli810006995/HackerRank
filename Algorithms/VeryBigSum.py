def aVeryBigSum(ar):
    total_sum=0
    for i in range(0, len(str(ar).strip().split(' '))):
        total_sum+=int(str(ar).strip().split(' ')[i])
    return total_sum

n=input().strip()
ar=input().strip()

result=aVeryBigSum(ar)
print(result)