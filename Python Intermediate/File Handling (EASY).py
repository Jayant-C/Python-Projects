

file = open("Hello.txt", "w")
file.write("Hello Python")
file.close()



file = open("Hello.txt", "a")
file.write("\nI am learning file handling")
file.close()

file = open("Hello.txt", "r")
content = file.read()
file.close()            
            
