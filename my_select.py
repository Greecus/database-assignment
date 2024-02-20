from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker
from seed import Studenci, Wykladowcy, Przedmioty, Oceny, Grupy, StudenciWGrupach


def query_1(session):
    query = session.query(select(func.avg(Oceny.ocena).label('avg_ocena'),Oceny.student.label('student_id'))
    .group_by(Oceny.student).order_by(func.avg(Oceny.ocena).desc()).limit(5).subquery()).all()
    return query


def query_2(session):
    query = session.query(
        select(func.avg(Oceny.ocena).label('avg_ocena'),Oceny.student.label('student_id'))
        .group_by(Oceny.student,Oceny.przedmiot_id)
        .order_by(func.avg(Oceny.ocena).desc()).subquery()).first()
    return query


def query_3(session):
    query = session.query(select(func.avg(Oceny.ocena),Przedmioty.przedmiot_nazwa,StudenciWGrupach.grupa_id)
                          .select_from(Oceny)
                          .outerjoin(Studenci).outerjoin(StudenciWGrupach).outerjoin(Grupy).outerjoin(Przedmioty)
                          .group_by(StudenciWGrupach.grupa_id,Przedmioty.przedmiot_nazwa)
                          .where(Przedmioty.przedmiot_nazwa=="Biologia")
                          .order_by(func.avg(Oceny.ocena).desc()).subquery()).all()
    return query


def query_4(session):
    query = session.query(select(func.avg(Oceny.ocena), Oceny.ocena_id, Oceny.student, StudenciWGrupach.grupa_id, Przedmioty.przedmiot_nazwa)
                          .select_from(Oceny).outerjoin(Studenci).outerjoin(StudenciWGrupach).outerjoin(Przedmioty).outerjoin(Grupy)
                          .group_by(StudenciWGrupach.grupa_id,Oceny.ocena_id,Przedmioty.przedmiot_nazwa)
                          .order_by(func.avg(Oceny.ocena)).subquery()).all()
    return query


def query_5(session):
    query = session.query(select(Przedmioty.przedmiot_nazwa,Wykladowcy.nazwisko,Wykladowcy.wykladowca_id)
                          .outerjoin(Przedmioty)
                          .group_by(Przedmioty.przedmiot_nazwa,Wykladowcy.nazwisko,Wykladowcy)
                          .where(Wykladowcy.nazwisko=='Kuboń').subquery()).all()
    return query


def query_6(session):
    query = session.query(select(Studenci.imie,Studenci.nazwisko,StudenciWGrupach.grupa_id)
                          .outerjoin(StudenciWGrupach)
                          .group_by(Studenci.imie,Studenci.nazwisko,StudenciWGrupach.grupa_id)
                          .where(StudenciWGrupach.grupa_id==5).subquery()).all()
    return query


def query_7(session):
    query = session.query(select(Studenci.imie,Studenci.nazwisko,Oceny.ocena)
                          .outerjoin(Oceny)
                          .outerjoin(StudenciWGrupach)
                          .outerjoin(Grupy)
                          .outerjoin(Przedmioty)
                          .group_by(Oceny.ocena,Studenci.nazwisko,Studenci.imie)
                          .where(Grupy.grupa_id==17,Przedmioty.przedmiot_nazwa=='Chemia').subquery()).all()
    return query


def query_8(session):
    query = session.query(select(Wykladowcy.imie,Wykladowcy.nazwisko,func.avg(Oceny.ocena))
                          .select_from(Wykladowcy)
                          .outerjoin(Przedmioty)
                          .outerjoin(Oceny)
                          .group_by(Wykladowcy.imie,Wykladowcy.nazwisko)
                          .where(Wykladowcy.nazwisko=="Kuboń",Przedmioty.przedmiot_nazwa=="WOS").subquery()).all()
    return query



def query_9(session):
    query = session.query(select(Studenci.imie,Studenci.nazwisko,Przedmioty.przedmiot_nazwa)
                          .select_from(Studenci)
                          .outerjoin(Oceny)
                          .outerjoin(Przedmioty)
                          .group_by(Studenci.imie,Studenci.nazwisko,Przedmioty.przedmiot_nazwa)
                          .where(Studenci.nazwisko=="Ciepła",Studenci.imie=="Karol").subquery()).all()
    return query


def query_10(session):
    query = session.query(select(Studenci.imie,Studenci.nazwisko,Przedmioty.przedmiot_nazwa)
                          .select_from(Studenci)
                          .outerjoin(Oceny)
                          .outerjoin(Przedmioty)
                          .outerjoin(Wykladowcy)
                          .group_by(Studenci.imie,Studenci.nazwisko,Przedmioty.przedmiot_nazwa)
                          .where(Studenci.nazwisko=="Ciepła",Studenci.imie=="Karol",Wykladowcy.nazwisko=='Kuboń').subquery()).all()
    return query

def main():
    engine = create_engine("postgresql://postgres:password@localhost:5432/postgres", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = query_10(session)
    print(results)

if __name__=='__main__':
    main()