EvenNums = []
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

def get_even_number(num):
    num = int(num)
    if num % 2 == 0:
        EvenNums.append(num)

# Write numbers to file
file = open("NumbersFile.txt", "w")
for i in numbers:
    file.write(i + "\n")
    get_even_number(i)
file.close()

print("File Written Successfully")

# Read file
file = open("NumbersFile.txt", "r")
content1 = file.read()
print("Here Are The Numbers:\n", content1)
file.close()

print("Here Are The Even Numbers:", EvenNums)

# Copy content
file = open("NumbersFile2.txt", "w")
file.write(content1)
file.close()
