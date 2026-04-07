num = int(input("Enter A Number:"))

bin = []

while num > 0:
     r = num % 2
     bin.append(r)
     num = num // 2

bin.reverse()

print(bin)

