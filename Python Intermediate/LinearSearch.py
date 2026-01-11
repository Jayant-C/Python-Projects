import random
status = "running"
user = input("[1]Start [2]End")
if user == "1":
    status = "running"

elif user == "2":
    status = "stop"

    
def search(data):
    for i in range(len(array)):
        index = array[i]
        if index == data:
            print(data,"is at index", i)



while status == "running":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(array)
    print(array)
    data = int(input("Enter A Number to search or type"))
    search(data)
    user = input("[1]Start [2]End")
    if user == "2":
        status = "stop"
    if status == "stop":
        print("Program Has Ended")

     

    
