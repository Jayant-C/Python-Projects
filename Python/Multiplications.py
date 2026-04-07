import random
user = int(input("[1]Normal [2]Random:"))
score = 0

if user == 1:
    a = int(input("Enter Number:"))
    lst1 = []
    for i in range(10):
        print(f"{a}x{i+1}=")
        ans = int(input())
        c = a * (i+1)
        if ans == c:
            print("Correct")
            score += 1
        else:
            print(f"Incorrect | {a}x{i+1}={c}")     
            lst1.append(f"{a}x{i+1}={c}")
    print(f"Your Score is {score}/10")
    print(f"Learn {lst1}")

elif user == 2:
    a, b = map(int, input ("Enter Table Range: ").split())
    lst2 = []
    x = random.randint(a, b)
    for i in range(8, 0, -1):
        print(f"{x}x{i}=")
        ans = int(input())
        c = x * i
        if ans == c:
            print("Correct")
            score += 1
        else:
            print(f"Incorrect | {x}x{i}={c}")    
            lst2.append(f"{x}x{i}={c}")
        x = random.randint(a, b)
    print(f"Your Score is {score}/8")    
    print(f"Learn {lst1}")


