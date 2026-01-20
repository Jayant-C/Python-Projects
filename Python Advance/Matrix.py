import random

mSize = int(input("Enter Matrix Size: "))
mSF = int(input("Matrix starts from: "))
mEF = int(input("Matrix ends to: "))
arr = [mSF, mEF]

def createMatrix(mSize, mSF, mEF):
    matrix = []
    for i in range(mSize):
        row = []
        for j in range(mSize):
            num = random.randint(arr[0], arr[1])
            row.append(num)
            print(num, " ", end="")
        matrix.append(row)
        print()
    return matrix

def searchElement(matrix, row, col):
    return matrix[row-1][col-1]

matrix = createMatrix(mSize, mSF, mEF)

# Search part
row = int(input("Enter row to search: "))
col = int(input("Enter column to search: "))

print(f"Value at row {row} column {col} is: {searchElement(matrix, row, col)}")

