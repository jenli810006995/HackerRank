#credit to Bigjin

def game(x , y):
    # return win or lose in boolean
    if 1 <= x <= 15 and 1 <= y <= 15:
        return not game(x-2, y+1) or not game(x-2, y-1) or not game(x+1, y-2) or not game(x-1, y-2)
    else:
        return True
    
def main():
    t=int(input().strip())
    for _ in range(t):
        x, y = map(int, input().split())
        if game(x,y) is True:
            print("First")
        else:
            print("Second")
main()