tasks = []

def Add_Task():
    task = input("Enter your task: ")

    task_details = {
        "task": task,
        "status": "pending"
    }

    tasks.append(task_details)

    print("Task added successfully!")
def view_Task():
	counter=1
	if not tasks:
		print("no tasks available")
	else:
		for i in tasks:
			print(str(counter)+" "+i["task"],i["status"])
			counter+=1
def complete_Task():
	name=input("enter task  to completed:")
	for i in tasks:
		if i["task"]==name:
			i["status"]="complete"
			print(i["task"]+":"+i["status"])
			print("task completed")
			break
	else:
			print("not found")
	  
	
def del_Task():
	delete=input("enter your deleted item:")
	for i in tasks:
		if i["task"]==delete:
			tasks.remove(i)
			print("deleted succussfully")
			break
	else:
		print("task is not found")
	
while True:
	print("1.Add")
	print("2.View")
	print("3.Complete")
	print("4.Delete")
	print("5.Exit")
	choice = input("Enter your choice: ")
	if choice == "1":
		Add_Task()
	elif choice=="2":
		view_Task()
	elif choice=="3":
		complete_Task()
	elif choice=="4":
		del_Task()
	elif choice=="5":
		if choice=="5":
			print("thankyou for using To Do application!!")
			break
	else:
		print("you can enter between 1 and 5")