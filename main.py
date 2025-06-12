import typer
import json

todo_list = typer.Typer()

tasks = {}

@todo_list.command()
def add_task(task: str):
    tasks_split = task.split(", ")
    if len(tasks_split) == 1:
        tasks.update({task: False})
    else:
        for i in tasks_split:
            tasks.update({i: False})

    with open("tasks.json", mode="w", encoding="utf-8") as write_file:
        json.dump(tasks, write_file, indent=4)

@todo_list.command()
def list_tasks():
    for index, value in enumerate(tasks):
        print(f"{index + 1} - {value}")

if __name__ == "__main__":
    todo_list()