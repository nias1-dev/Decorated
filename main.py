import time

"""
Program intended to constantly run on server.
Logic helps an end user to track a security task.
User must take digital action and confirm action has been taken with phone call to decision maker.

By A.S III 1/4/2026
"""



class DigitalAction:
    """handles boolean with polymorphism"""
    def __init__(self, task1, task2, completed):
        self.task1 = task1
        self.task2 = task2
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def reset_completed(self):
        self.completed = False


def flipper():
    """Intended to be called by server at midnight"""
    pass
    

def director():
    # task1 = "Update Pending"
    # task2 = "Redisigning program flow"
    # 
    t1 = DigitalAction("delete cache", "call director to confirm tasks completed", False)
    reminder = "Call team and remind them to complete task."
    # return task1, task2
    return t1
    

def controller(task):
    """Intended to be called by server. Controls program's functionality"""
    t1 = director()
    while True:
        print(f'{t1.task1} & {t1.task2}')
        status = input("Confirm personal execution of tasks.")
    
        if status.lower() == "ok":
            t1.mark_completed()
            print(f"employee has set the task to {t1.completed}")
            print("see you in 24 hours")
            
            break
        else:
            #if false remind user of task
            print("you have not completed the tasks")
    


controller(director())
