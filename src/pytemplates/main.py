import typer

from pytemplates.core.module1 import greet
from pytemplates.core.module2 import wish_farewell

app = typer.Typer()


@app.command()
def hello(user: str):
    typer.echo(greet(user=user))


@app.command()
def goodbye(user: str):
    typer.echo(wish_farewell(user=user))


@app.command()
def whoami():
    typer.echo("Socket stuff")


if __name__ == "__main__":
    app()