def gameOfStones(n):
    if n == 1:
        print("Second")
    elif n <= 6: # First Win!
        print("First")
    else:
        print("Second" if n % 7 == 0 or n % 7 == 1 else "First")

t = int(input())

for _ in range(t):
    n = int(input())
    result = gameOfStones(n)
    result
