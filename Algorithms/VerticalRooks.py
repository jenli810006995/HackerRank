def verticalRooks(r1, r2):
    nim=0 # Game of Nim
    for i in range(n):
        nim^=abs(int(r1[i][0])-int(r2[i][0]))-1
    print('player-2' if nim !=0 else 'player-1')   
        
t=int(input().strip())
n=int(input().strip())
r1=[]
r2=[]
for _ in range(n):
    r1.append(list(map(int, str(input()).strip().split())))
for _ in range(n):
    r2.append(list(map(int, str(input()).strip().split())))
result=verticalRooks(r1, r2)
result