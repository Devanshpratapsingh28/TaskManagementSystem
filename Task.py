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
        # print("Task added successfully") 

    def removeTask(self,task):
        self.taskList.remove(task)
        print("Task removed successfully") 
    
    #Track based on status
    def getTasksStatus(self, status=None):
        if status:
            tasks_with_status = []
            for task in self.taskList:
                if task.status == status:
                    tasks_with_status.append(task)
            return tasks_with_status
        return self.taskList
    
    #Track based on priority
    def getTasksPriority(self, priority=None):
        if priority:
            tasks_with_priority = []
            for task in self.taskList:
                if task.priority == priority:
                    tasks_with_priority.append(task)
            return tasks_with_priority
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

taskList=(("Task 1", "Go to market", "Low", "2024-06-30"),("Task 2", "Meeting on Friday", "High", "2024-06-21"),("Task 3", "Call Milkman", "Low", "2024-06-16"),Task("Task 4", "Book Ticket", "High", "2024-06-30"),("Task 5", "Schedule meeting with Virat", "High", "2024-06-18"))

user = TaskManager("Alice")
for i in taskList:
    user.addTask(i)

# Give List all tasks Priority wise
for task in user.getTasksPriority("High"):
    print(task.title, task.priority)

# Mark task1 as completed
taskList[0].taskCompleted("2024-06-20")

# List completed tasks
completed_tasks = user.getTasksStatus(status="Completed")
for task in completed_tasks:
    print(task.title, task.status)        
        


