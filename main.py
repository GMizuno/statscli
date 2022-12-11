import typer

app = typer.Typer(name="StatsCli CLI")

def hello_world():
    print(hello_world)

app.registered_commands.append(hello_world)

if __name__ == "__main__":
    app()