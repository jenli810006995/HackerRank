def diagonalDifference(arr):
    prim=0
    second=0
    length=len(arr[0]) # arr is an array of n lists with n elements
    for count in range(0, length):
        prim+=arr[count][count]
        second+=arr[count][(length-1)-count]
    return abs(prim-second)

n=int(input().strip())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))
result=diagonalDifference(arr)
print(result)