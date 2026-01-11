Num = int(input("Enter A number to find Even or Odd"))

def GetEven(Num):
    if Num % 2 == 0:
        return Num,"Is Even"
       
    else:
        return Num,"Is Odd"

print(GetEven(Num))



def createBorder(side):
    for i in range(side):
        if i == 0 or i == side - 1:
            print("# " * side)
        else:
            print("# " + "  " * (side - 2) + "#")

def createFloor(side):
    for i in range(side):
        print("# " * side)


createFloor(5)
print(" ")
createBorder(5)
                                                     
