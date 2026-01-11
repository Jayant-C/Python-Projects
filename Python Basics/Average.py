Num1 = int(input("Enter Num1"))
Num2 = int(input("Enter Num2"))
Num3 = int(input("Enter Num3"))
NumList = (Num1, Num2, Num3)
def Average():
    Sum = Num1 + Num2 + Num3
    Average = Sum / len(NumList)
    print (Average)

Average()
    
