def birthdayCakeCandles(ar):
    # get the tallest numbers
    tallest=0
    max_value=max(ar)
    for i in range(0, n):
        if ar.split(' ')[i]==max_value:
            tallest+=1
        else:
            tallest+=0
    return tallest    
    
n=int(input().strip()) # number of candles
ar=input().strip() # array of numbers
result=birthdayCakeCandles(ar)
print(result)