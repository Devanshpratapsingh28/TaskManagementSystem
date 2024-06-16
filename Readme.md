# Task Management System and To-Do List

This project is my first Python endeavor aimed at familiarizing myself with Python syntax and concepts. The system consists of two main classes: **Task** and **TaskManager**.

## Task Class

### Attributes
1. Title
2. Description
3. Priority
4. Deadline
5. Status
6. Completion Date

### Methods
1. **\_\_init\_\_()**: Constructor for initializing a task.
2. **updateTask()**: Updates or modifies an existing task.
3. **taskCompleted()**: Marks a task as completed.
4. **taskIncomplete()**: Marks a task as incomplete.

## TaskManager Class

### Attributes
1. Name
2. taskList
3. task
4. status
5. priority

### Methods
1. **\_\_init\_\_()**: Constructor for initializing the TaskManager.
2. **addTask()**: Adds a valid task to the taskList.
3. **removeTask()**: Removes a specified task from the taskList.
4. **getTasksStatus()**: Retrieves a list of tasks based on their status.
5. **getTasksPriority()**: Retrieves a list of tasks based on their priority.

## Features
1. Task Manager functionality.
2. Ability to Add/Update/Remove tasks.
3. Prioritizes tasks based on priority levels.
