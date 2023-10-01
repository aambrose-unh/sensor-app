from sqlalchemy import create_engine
import pymysql
import os
import typer

from sensor_app_db.models import Base

app = typer.Typer()

DB_USER = os.getenv("DB_USER")
DB_PASSWD = os.getenv("DB_PASSWD")


@app.command()
def init_db(self, db_name: str):
    connection_uri = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWD}@localhost/{db_name}[?<options>]"
    )
    engine = create_engine(connection_uri)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    app()
