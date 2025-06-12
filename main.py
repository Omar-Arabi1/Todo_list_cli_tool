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

# we make the first command add to add a task
@todo_list.command()
def add(task: str):
    tasks = {}
    tasks_split = task.split(", ")

    # we check if the length of the split list is more than one so there is more than one task we loop through it until all of them are added
    # to the dictionary "tasks"
    if len(tasks_split) == 1:
        tasks.update({task: False})
    else:
        for i in tasks_split:
            tasks.update({i: False})

    # we finally save the dictionary "tasks" into the tasks.json file 
    with open("tasks.json", mode="w", encoding="utf-8") as write_file:
        json.dump(tasks, write_file, indent=4)

# we make the second command list
@todo_list.command()
def list():
    # we open the file for reading 
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
        tasks_to_list = json.load(read_file)

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
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
        tasks_to_mark = json.load(read_file)

    # we mark the task done by checking the given index subracted by one because the user will enter a one index number not 0 indexed
    for i, v in enumerate(tasks_to_mark):
        if index - 1 == i:
            tasks_to_mark[v] = True

    with open("tasks.json", mode="w", encoding="utf-8") as write_file:
        json.dump(tasks_to_mark, write_file, indent=4)

# we make the fourth command task remove 
@todo_list.command()
# both these are now options one to remove a certain index default one the other to remove all default False
def remove(index: int = 1, remove_all: bool = False):
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
        tasks_to_remove = json.load(read_file)
    
    if not remove_all: # we check if the user made the option to true 
        for i, v in enumerate(tasks_to_remove):
            if index - 1 == i:
                # we check the index remove it and break out of the loop we break because we can't change the size of the iterable during the loop
                tasks_to_remove.pop(v)
                break
        
        with open("tasks.json", mode="w", encoding="utf-8") as write_file:
            json.dump(tasks_to_remove, write_file, indent=4)
    else:
        with open("tasks.json", mode="w", encoding="utf-8") as write_file:
            json.dump({}, write_file, indent=4)

# runs the program as a python script
if __name__ == "__main__":
    todo_list()