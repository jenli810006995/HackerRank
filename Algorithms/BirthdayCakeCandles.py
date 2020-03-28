def birthdayCakeCandles(ar):
    # get the tallest numbers
    tallest=0
    max_value=max(ar)
    for i in range(0, n):
        if int(ar[i])==max_value:
            tallest+=1
        else:
            tallest+=0
    return tallest    
    
n=int(input().strip()) # number of candles
ar=list(map(int, input().split())) # array of numbers
result=birthdayCakeCandles(ar)
print(result)