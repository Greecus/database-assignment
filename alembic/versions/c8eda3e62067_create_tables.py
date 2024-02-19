"""create tables

Revision ID: c8eda3e62067
Revises: 
Create Date: 2024-02-19 20:43:25.206062

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import ForeignKeyConstraint

# revision identifiers, used by Alembic.
revision: str = 'c8eda3e62067'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Studenci",
        Column("student_id",Integer,primary_key=True),
        Column("imie",String),
        Column("nazwisko",String)
    )
    op.create_table(
        "Wykladowcy",
        Column("wykladowca_id",Integer,primary_key=True),
        Column("imie",String),
        Column("nazwisko",String)
    )
    op.create_table(
        "Przedmioty",
        Column("przedmiot_id",Integer,primary_key=True),
        Column("przedmiot_nazwa",String),
        Column("wykladowca",Integer),
        ForeignKeyConstraint(["wykladowca"],["Wykladowcy.wykladowca_id"],ondelete="CASCADE")
    )
    op.create_table(
        "Oceny",
        Column("ocena_id",Integer,primary_key=True),
        Column("ocena",Integer),
        Column("przedmiot_id",Integer),
        Column("student",Integer),
        Column("data",Integer),
        ForeignKeyConstraint(["przedmiot_id"],["Przedmioty.przedmiot_id"],ondelete="CASCADE"),
        ForeignKeyConstraint(["student"],["Studenci.student_id"],ondelete="CASCADE")
    )
    op.create_table(
        "Grupy",
        Column("grupa_id",Integer,primary_key=True),
        Column("przedmiot_id",Integer),
        ForeignKeyConstraint(["przedmiot_id"],["Przedmioty.przedmiot_id"],ondelete="CASCADE")
    )
    op.create_table(
        "StudenciWGrupach",
        Column("grupa_id",Integer),
        Column("student_id",Integer),
        ForeignKeyConstraint(["student_id"],["Studenci.student_id"],ondelete="CASCADE"),
        ForeignKeyConstraint(["grupa_id"],["Grupy.grupa_id"],ondelete="CASCADE")
    )



def downgrade() -> None:
    op.drop_table("StudenciWGrupach")
    op.drop_table("Grupy")
    op.drop_table("Oceny")
    op.drop_table("Przedmioty")
    op.drop_table("Wykladowcy")
    op.drop_table("Studenci")
