def task():
    tasks = []
    task_no = int(input("Enter number of tasks = "))
    for i in range(1, task_no+1):
        task_name = input(f"Enter the task {i}:")
        tasks.append(task_name)
        print(tasks)

    while True:
        try:
            opt = int(input("1-enter\n2-delete\n3-update\n4-view\n5-stop"))
            if opt == 1:
                task_name = input("Enter the task = ")
                tasks.append(task_name)
                print(tasks)
            elif opt == 2:
                del_task = input("Enter the task you want to delete = ")
                if del_task in tasks:
                    del1 = tasks.index(del_task)
                    del tasks[del1]
                    print(f"Your task is been deleted......\n")
            elif opt == 3:
                old_task = input("Enter the task you want to update = ")
                if old_task in tasks:
                    update = input("Enter the new task = ")
                    old = tasks.index(old_task)
                    tasks[old] = update
                    print(f"Your task is updated {tasks}")            
            elif opt == 4:
                print(f"Your tasks are {tasks}")            
            elif opt == 5:
                for i in tasks:
                    print(f"Your tasks are {i}")
                break            
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")

task()
