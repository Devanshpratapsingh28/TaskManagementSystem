class Task:
    def __init__(self,title,description,priority,deadline):#Priority=Urgent>High>Low
        self.title=title
        self.description=description
        self.priority=priority
        self.deadline=deadline
        self.status="Pending" #Pending/In-Progress/Completed

    def update_task(self, title=None, description=None, priority=None, deadline=None):
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

    def task_In_progress(self):
        self.status="In-Progress"   

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

    def get_Tasks(self):
        return self.taskList  
    
      


