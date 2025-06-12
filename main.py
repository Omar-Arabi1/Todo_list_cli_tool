import typer
import json
from rich import print as pr

"""
Author: Omar Arabi

Date: June 12 2025

Description:
this is a todo list CLI tool which allows the user to add, list, mark-done and remove tasks
and all will be saved in a .json file
"""

# we make the app run as a python script not as a typer script
todo_list = typer.Typer()

# put the repeated commands into these functions
def write_json(dict_to_json):
    with open("tasks.json", mode="w", encoding="utf-8") as write_file:
        json.dump(dict_to_json, write_file, indent=4)

def read_json():
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
            return json.load(read_file)
    
def empty_error():
    pr("[red]You don't have any tasks in the list yet,[/red]")
    pr("[red]use the 'add' command to add tasks to your list [/red]")

# we make the first command add to add a task
@todo_list.command()
def add(task: str):
    tasks = read_json() # we read the json file first before updating it to not remove the old user data
    tasks_split = task.split(", ")

    # we check if the length of the split list is more than one so there is more than one task we loop through it until all of them are added
    # to the dictionary "tasks"
    if len(tasks_split) == 1:
        tasks.update({task: False})
        pr("[green]task added successfully[/green]")
    else:
        for i in tasks_split:
            tasks.update({i: False})
        
        pr("[green]tasks added successfully[/green]")

    # we finally save the dictionary "tasks" into the tasks.json file 
    write_json(tasks)

# we make the second command list
@todo_list.command()
def list():
    # we open the file for reading 
    tasks_to_list = read_json()
    if len(tasks_to_list) == 0: # we check if its empty and print and error message else we continue
        empty_error()
    else:
        # we loop through it adding the index plus 1 to be one indexed not zero indexed and we put the key next to it
        # and we also check if its done or not so we show the user a message
        for i, v in enumerate(tasks_to_list):
            if tasks_to_list[v] == False:
                pr(f"{i + 1} - {v} - [red]not done[/red]")
            else:
                pr(f"{i + 1} - {v} - [green]done[/green]")

# we make the third command mark-done
@todo_list.command()
def mark_done(index: int):
    tasks_to_mark = read_json()
    if len(tasks_to_mark) == 0: # same error checking as list
        empty_error()
    else:
        # we mark the task done by checking the given index subracted by one because the user will enter a one index number not 0 indexed
        for i, v in enumerate(tasks_to_mark):
            if index - 1 == i:
                # we check wether or not the task is already marked true so that we tell the user it is already marked done
                if tasks_to_mark[v] == False:
                    tasks_to_mark[v] = True
                    pr(f"[green]{v} marked done[/green]")
                    write_json(tasks_to_mark)
                    return
                else:
                    pr("[red]The task is already marked as true[/red]")
                    return

        pr("[red]The index you entered isn't in the tasks[/red]") # if all fails we tell the user that the intered index is out of range

# we make the fourth command task remove 
@todo_list.command()
# both these are now options one to remove a certain index default one the other to remove all default False
def remove(index: int = 1, all: bool = False):
    tasks_to_remove = read_json()
    if len(tasks_to_remove) == 0: # same error cheking as list
        empty_error()
    else:
        if not all: # we check if the user made the option to true 
            for i, v in enumerate(tasks_to_remove):
                if index - 1 == i:
                    # we check the index remove it and break out of the loop we break because we can't change the size of the iterable during the loop
                    confirmation = input(f"are you sure you want to remove {v} (y/N): ") # confirmation on wheter or not to delete the task
                    if confirmation == "y":
                        tasks_to_remove.pop(v)
                        pr(f"[green]Task {v} removed[/green]")
                        write_json(tasks_to_remove)
                        return
                    else:
                        pr(f"[green]Task {v} not removed[/green]")
                        return

            pr("[red]The index you entered is out of range[/red]") # if all fails we tell the user that the intered index is out of range
        else:
            confirmation = input(f"are you sure you want to remove the entire list (y/N): ")
            if confirmation == "y":
                write_json({})
                pr("[green]all tasks are removed successfully[/green]")
            else:
                pr("[green]The list was not removed[/green]")

# runs the program as a python script
if __name__ == "__main__":
    todo_list()