import typer

todo_list = typer.Typer()

tasks = []

@todo_list.command()
def add_task(task: str):
    tasks.append(task)

@todo_list.command()
def list_tasks():
    for index, value in enumerate(tasks):
        print(f"{index + 1} - {value}")

if __name__ == "__main__":
    todo_list()