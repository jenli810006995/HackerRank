def whetherWeird(n):
    if n%2 !=0:
        print("Weird")
    elif (n%2==0) & (n>=2) & (n<=5):
        print("Not Weird")
    elif (n%2==0) &(n>=6) & (n<=20):
        print("Weird")
    elif (n%2==0) & (n>20):
        print("Not Weird") 
    
n=int(input().strip())
whetherWeird(n)
