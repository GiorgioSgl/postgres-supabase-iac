import datetime as dt
import uuid

from sqlmodel import Field, SQLModel, text

from ..schemas import SchemaName


class User(SQLModel, table=True):
    __table_args__ = ({"schema": SchemaName.users.value},)

    __tablename__ = "Users"  # type: ignore

    id_user: uuid.UUID = Field(
        default=uuid.uuid4(),
        primary_key=True,
        sa_column_kwargs={
            "server_default": text("gen_random_uuid()"),
        },
    )
    username: str = Field(
        primary_key=True,
    )
    created_at: dt.datetime = Field(
        default=dt.datetime.utcnow(),
        sa_column_kwargs={
            "server_default": text("NOW()"),
        },
    )