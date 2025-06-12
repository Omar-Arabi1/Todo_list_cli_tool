import typer
import json

"""
Author: Omar Arabi

Date: June 12 2025

Description:
this is a todo list CLI tool which allows the user to add, list, mark-done and remove tasks
and all will be saved in a .json file
"""

# we make the app run as a python script not as a typer script
todo_list = typer.Typer()

def write_json(dict_to_json):
    with open("tasks.json", mode="w", encoding="utf-8") as write_file:
        json.dump(dict_to_json, write_file, indent=4)

def read_json():
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
            return json.load(read_file)
    
def empty_error():
    print("You don't have any tasks in the list yet,")
    print("use the 'add' command to add tasks to your list")

# we make the first command add to add a task
@todo_list.command()
def add(task: str):
    tasks = read_json()
    tasks_split = task.split(", ")

    # we check if the length of the split list is more than one so there is more than one task we loop through it until all of them are added
    # to the dictionary "tasks"
    if len(tasks_split) == 1:
        tasks.update({task: False})
        print("task added successfully")
    else:
        for i in tasks_split:
            tasks.update({i: False})
        
        print("tasks added successfully")

    # we finally save the dictionary "tasks" into the tasks.json file 
    write_json(tasks)

# we make the second command list
@todo_list.command()
def list():
    # we open the file for reading 
    tasks_to_list = read_json()
    if len(tasks_to_list) == 0:
        empty_error()
    else:
        # we loop through it adding the index plus 1 to be one indexed not zero indexed and we put the key next to it
        # and we also check if its done or not so we show the user a message
        for i, v in enumerate(tasks_to_list):
            if tasks_to_list[v] == False:
                print(f"{i + 1} - {v} - not done")
            else:
                print(f"{i + 1} - {v} - done")

# we make the third command mark-done
@todo_list.command()
def mark_done(index: int):
    tasks_to_mark = read_json()
    if len(tasks_to_mark) == 0:
        empty_error()
    else:
        # we mark the task done by checking the given index subracted by one because the user will enter a one index number not 0 indexed
        for i, v in enumerate(tasks_to_mark):
            if index - 1 == i:
                if tasks_to_mark[v] == False:
                    tasks_to_mark[v] = True
                    print(f"{v} marked done")
                    write_json(tasks_to_mark)
                    return
                else:
                    print("The task is already marked as true")
                    return

        print("The index you entered isn't in the tasks")

# we make the fourth command task remove 
@todo_list.command()
# both these are now options one to remove a certain index default one the other to remove all default False
def remove(index: int = 1, all: bool = False):
    tasks_to_remove = read_json()
    if len(tasks_to_remove) == 0:
        empty_error()
    else:
        if not all: # we check if the user made the option to true 
            for i, v in enumerate(tasks_to_remove):
                if index - 1 == i:
                    # we check the index remove it and break out of the loop we break because we can't change the size of the iterable during the loop
                    confirmation = input(f"are you sure you want to remove {v} (y/N): ")
                    if confirmation == "y":
                        tasks_to_remove.pop(v)
                        print(f"Task {v} removed")
                        break
                    else:
                        print(f"Task {v} not removed")
                        break
            
            write_json(tasks_to_remove)
        else:
            confirmation = input(f"are you sure you want to remove the entire list (y/N): ")
            if confirmation == "y":
                write_json({})
                print("all tasks are removed successfully")
            else:
                print("The list was not removed")

# runs the program as a python script
if __name__ == "__main__":
    todo_list()