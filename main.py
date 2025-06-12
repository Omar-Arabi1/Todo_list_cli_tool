import typer

app = typer.Typer()

@app.command()
def hello(name):
    print(f"Hello {name}")


@app.command()
def goodbye(name, formal = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()