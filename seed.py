from main import gen_fake_data
from sqlalchemy import create_engine, MetaData, ForeignKey, Column, String, Integer, Table, Date, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Studenci(Base):
    __tablename__ = "Studenci"
    student_id = Column("student_id",Integer,primary_key=True)
    imie = Column("imie",String)
    nazwisko = Column("nazwisko",String)

    def __init__(self, student_id, imie, nazwisko):
        self.student_id = student_id
        self.imie = imie
        self.nazwisko = nazwisko


class Wykladowcy(Base):
    __tablename__ = "Wykladowcy"
    wykladowca_id = Column("wykladowca_id",Integer,primary_key=True)
    imie = Column("imie",String)
    nazwisko = Column("nazwisko",String)

    def __init__(self, wykladowca_id, imie, nazwisko):
        self.wykladowca_id = wykladowca_id
        self.imie = imie
        self.nazwisko = nazwisko


class Przedmioty(Base):
    __tablename__ = "Przedmioty"
    przedmiot_id = Column("przedmiot_id",Integer,primary_key=True)
    przedmiot_nazwa = Column("przedmiot_nazwa",String)
    wykladowca = Column("wykladowca",Integer, ForeignKey("Wykladowcy.wykladowca_id",ondelete="CASCADE"))

    def __init__(self, przedmiot_id, przedmiot_nazwa, wykladowca):
        self.przedmiot_id = przedmiot_id
        self.przedmiot_nazwa = przedmiot_nazwa
        self.wykladowca = wykladowca


class Oceny(Base):
    __tablename__ = "Oceny"
    ocena_id = Column("ocena_id",Integer,primary_key=True)
    ocena = Column("ocena",Integer)
    przedmiot_id = Column("przedmiot_id",Integer, ForeignKey("Przedmioty.przedmiot_id",ondelete="CASCADE"))
    student = Column("student",Integer, ForeignKey("Studenci.student_id",ondelete="CASCADE"))
    data = Column("data",Date)

    def __init__(self, ocena_id, ocena, przedmiot_id, student, data):
        self.ocena_id = ocena_id
        self.ocena = ocena
        self.przedmiot_id = przedmiot_id
        self.student = student
        self.data = data 

class Grupy(Base):
    __tablename__ = "Grupy"
    grupa_id = Column("grupa_id",Integer,primary_key=True)
    przedmiot_id = Column("przedmiot_id",Integer, ForeignKey("Przedmioty.przedmiot_id",ondelete="CASCADE"))

    def __init__(self, grupa_id, przedmiot_id):
        self.grupa_id = grupa_id
        self.przedmiot_id = przedmiot_id

class StudenciWGrupach(Base):
    __tablename__ = "StudenciWGrupach"
    grupa_id = Column("grupa_id",Integer, ForeignKey("Grupy.grupa_id",ondelete="CASCADE"))
    student_id = Column("student_id",Integer, ForeignKey("Studenci.student_id",ondelete="CASCADE"))
    column_not_exist_in_db = Column(Integer, primary_key=True)

    def __init__(self, grupa_id, student_id):
        self.grupa_id = grupa_id
        self.student_id = student_id

def insert_data_to_db(*data):
    engine = create_engine("postgresql://postgres:password@localhost:5432/postgres", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    

    with engine.begin() as conn: 
        for table,table_data in zip([Studenci,Wykladowcy,Przedmioty,Grupy,Oceny,StudenciWGrupach],data):
            temp = insert(table).values(table_data)            
            conn.execute(temp)

if __name__=='__main__':

    students_data, teachers_data, subjects_data, groups_data, marks_data, students_in_groups_data = gen_fake_data()
    insert_data_to_db(students_data, teachers_data, subjects_data, groups_data, marks_data, students_in_groups_data)