import typer
from decouple import config

from .create_tables import create_postgres

app = typer.Typer()


@app.command()
def create_tables(
    postgres_uri: str = typer.Option(
        default=config("POSTGRES_URI", cast=str, default=None),
        help="Postgres URI",
    ),
    # verbose: bool = typer.Option(
    #     default=config("VERBOSE", cast=bool, default=True),
    #     help="Verbose",
    # ),
):
    create_postgres(postgres_uri=postgres_uri)


@app.callback()
def callback():
    """
    Bienvenido a la aplicación de generación de tablas de Postgres para Menhir.
    """
    pass


if __name__ == "__main__":
    app()