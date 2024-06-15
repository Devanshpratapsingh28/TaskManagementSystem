class Task:
    def __init__(self,title,description,priority,deadline):#Priority=Urgent>High>Low
        self.title=title
        self.description=description
        self.priority=priority
        self.deadline=deadline
        self.status="Incomplete" #Incomplete/Completed

    def updateTask(self, title=None, description=None, priority=None, deadline=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if priority:
            self.priority = priority
        if deadline:
            self.deadline = deadline

    def taskCompleted(self,completionDate):
        self.status="Completed" 
        self.completionDate= completionDate 

    def taskIncomplete(self):
        self.status="Incomplete"   



class User:
    def __init__(self,name):
        self.name=name
        self.taskList=[]

    def addTask(self,task):
        self.taskList.append(task) 
        print("Task added successfully") 

    def removeTask(self,task):
        self.taskList.remove(task)
        print("Task removed successfully") 

    def getTasks(self, status=None):
        if status:
            tasks_with_status = []
            for task in self.taskList:
                if task.status == status:
                    tasks_with_status.append(task)
            return tasks_with_status
        return self.taskList


class TaskManager(User):
    def __init__(self, name):
        super().__init__(name)
        print(f"Hi, {name} Your task manager is created successfully, now you can manage your tasks smoothly")

    def addTask(self, task):
        super().addTask(task)

    def removeTask(self, task):
        super().removeTask(task)

#Examples for testing
task1 = Task("Task 1", "Description 1", "High", "2024-06-30")
task2 = Task("Task 2", "Description 2", "Low", "2024-07-15")

user = TaskManager("Alice")
user.addTask(task1)
user.addTask(task2)

# List all tasks
for task in user.getTasks():
    print(task.title, task.status)

# Mark task1 as completed
task1.taskCompleted("2024-06-20")

# List completed tasks
completed_tasks = user.getTasks(status="Completed")
for task in completed_tasks:
    print(task.title, task.status)        
        


