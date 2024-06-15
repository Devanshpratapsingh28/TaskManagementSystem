class Task:
    def __init__(self,title,description,priority,deadline):#Priority=Urgent>High>Low
        self.title=title
        self.description=description
        self.priority=priority
        self.deadline=deadline
        self.status="Incomplete" #Incomplete/Completed

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

    def task_Incomplete(self):
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

    def get_tasks(self, status=None):
        if status:
            tasks_with_status = []
            for task in self.tasks:
                if task.status == status:
                    tasks_with_status.append(task)
            return tasks_with_status
        return self.tasks

#Task Management Functions

class TaskManager(Task,User):
    def __init__(self,name):
        super(User).__init__(name)
        


