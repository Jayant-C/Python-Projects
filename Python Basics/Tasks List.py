User = input("Select - [1] Add Task, [2] View Task, [3] Delete Task")
list = ["Work"]
if User == "1":
    useraddtask = input("Add Your Task")
    list.append(useraddtask)

if User == "2":
    print(list)

if User == "3":
    print(list)
    RemoveTask = input("Enter The Name of The Task That You Want to Remove")
    list.remove(RemoveTask)
    
    
