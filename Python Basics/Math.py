Name = input("Enter Your Name:")
print("Hello", Name)
A = int(input("Enter The First Number:"))
B = int(input("Enter The Second Number:"))
Question = input("Select An Operation - Sum, Difference, Product (Type END to end this program)")
Sum = A + B
Difference = A - B
Product = A * B
if Question == "Sum":
    print("The Sum of", A, "and", B, "is", Sum)
    Question = input("Select An Operation - Sum, Difference, Product (Type END to end this program)")

if Question == "Difference":
    print("The Difference of", A, "and", B, "is", Difference)
    Question = input("Select An Operation - Sum, Difference, Product (Type END to end this program)")

if Question == "Product":
    print("The Product of", A, "and", B, "is", Product)
    Question = input("Select An Operation - Sum, Difference, Product (Type END to end this program)")

if Question == "END":
    print("The Program Has Ended")
    
