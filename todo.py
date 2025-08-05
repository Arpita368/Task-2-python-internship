to_do_list=[]
while True:
    print("\nMENU \n1. Add Task \n2. Remove Task \n3. View Tasks \n4. Save tasks and Close the app")
    choice = int(input("Enter a number: "))
    if choice==1:
        to_do_list.append(input("Enter your task: "))
        print("Task added in the list")
    elif choice==2:
        if not to_do_list:
            print("Task list is empty.")
            continue
        task = int(input("Enter the task number: "))
        if task>0 and task<=len(to_do_list):
            to_do_list.remove(to_do_list[task-1])
            print("Task removed from the list")
        else:
            print("Invalid task number.")
        
    elif choice==3:
        print("\n----------------------------")
        print("Tasks:")
        for i in range(0, len(to_do_list)):
            print(f"{i+1}. {to_do_list[i]}")
        print("----------------------------")
    elif choice==4:
        with open("to_do_list.txt","w") as file:
            for i in range(0, len(to_do_list)):
                file.write(f"{i+1}. {to_do_list[i]}\n")
        print("Tasks saved to 'to_do_list.txt'. Closing the application.")
        break;
    else:
        print("Invalid choice. Try again.")
