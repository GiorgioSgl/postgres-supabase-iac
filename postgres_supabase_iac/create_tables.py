from sqlmodel import Session, SQLModel, create_engine, text

from .schemas.users import *  # noqa
from .schemas.schemas import SchemaName


def create_postgres(postgres_uri: str):
    engine = create_engine(postgres_uri)

    with Session(engine) as session:
        session.exec(text(f"CREATE SCHEMA {SchemaName.users.value}"))
        session.commit()

    SQLModel.metadata.create_all(engine)