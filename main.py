import typer
import json

todo_list = typer.Typer()

@todo_list.command()
def add_task(task: str):
    tasks = {}
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
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
        tasks_to_list = json.load(read_file)

    for i, v in enumerate(tasks_to_list):
        print(f"{i + 1} - {v}")

if __name__ == "__main__":
    todo_list()