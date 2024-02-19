from main import gen_fake_data
from sqlalchemy import create_engine, MetaData, ForeignKey, Column, String, Integer, Table, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

m = MetaData()
Studenci = Table("Studenci",m,
    Column("student_id",Integer,primary_key=True),
    Column("imie",String),
    Column("nazwisko",String))


Wykladowcy = Table("Wykladowcy",m,
    wykladowca_id = Column("wykladowca_id",Integer,primary_key=True),
    imie = Column("imie",String),
    nazwisko = Column("nazwisko",String))

Przedmioty = Table("Przedmioty",m,
    przedmiot_id = Column("przedmiot_id",Integer,primary_key=True),
    przedmiot_nazwa = Column("przedmiot_nazwa",String),
    wykladowca = Column("wykladowca",Integer, ForeignKey("Wykladowcy.wykladowca_id",ondelete="CASCADE")))

Oceny = Table("Oceny",m,
    ocena_id = Column("ocena_id",Integer,primary_key=True),
    ocena = Column("ocena",Integer),
    przedmiot_id = Column("przedmiot_id",Integer, ForeignKey("Przedmioty.przedmiot_id",ondelete="CASCADE")),
    student = Column("student",Integer, ForeignKey("Studenci.student_id",ondelete="CASCADE")),
    data = Column("data",Integer))


Grupy = Table("Grupy",m,
    grupa_id = Column("grupa_id",Integer,primary_key=True),
    przedmiot_id = Column("przedmiot_id",Integer, ForeignKey("Przedmioty.przedmiot_id",ondelete="CASCADE")))

StudenciWGrupach = Table("StudenciWGrupach",m,
    grupa_id = Column("grupa_id",Integer, ForeignKey("Grupy.grupa_id",ondelete="CASCADE")),
    student_id = Column("student_id",Integer, ForeignKey("Studenci.student_id",ondelete="CASCADE")))

def insert_data_to_db(*data):
    engine = create_engine("postgres://postgres:password@localhost:5432/postgres", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    prepared_data = []
    for table,table_data in zip(data,[Studenci,Wykladowcy,Przedmioty,Grupy,Oceny,StudenciWGrupach]):
        prepared_data.append(insert(table).values(table_data))

    with engine.begin() as conn: 
        for command in prepared_data:
            conn.execute(command)

if __name__=='__main__':

    students_data, teachers_data, subjects_data, groups_data, marks_data, students_in_groups_data = gen_fake_data()
    insert_data_to_db(students_data, teachers_data, subjects_data, groups_data, marks_data, students_in_groups_data)