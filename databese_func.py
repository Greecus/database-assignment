import psycopg2

DATABASE = """
CREATE table Studenci(
student_id int not null primary key,
imie varchar(20),
nazwisko varchar(20));

CREATE table Wykladowcy(
wykladowca_id int not null primary key,
imie varchar(20),
nazwisko varchar(20));

create table Przedmioty(
przedmiot_id int not null primary key,
przedmiot_nazwa varchar(20) not null,
wykladowca int not null,
FOREIGN key (wykladowca) REFERENCES Wykladowcy(wykladowca_id) on delete cascade on update cascade);

create table Grupy(
grupa_id int not null primary key,
przedmiot_id int,
FOREIGN KEY (przedmiot_id) REFERENCES Przedmioty(przedmiot_id)
	on delete cascade
	on update cascade);

create table Oceny(
ocena_id int not null primary key,
ocena INT CHECK (ocena BETWEEN 1 AND 6),
przedmiot_id int,
student int,
data DATE not null,
FOREIGN KEY (przedmiot_id) REFERENCES Przedmioty(przedmiot_id)
	on delete cascade
	on update cascade,
foreign key (student) references Studenci(student_id)
	on delete cascade
	on update cascade);
	
create table StudenciWGrupach(
grupa_id int,
student_id int,
FOREIGN KEY (student_id) REFERENCES Studenci(student_id)
	on delete cascade
	on update cascade,
FOREIGN KEY (grupa_id) REFERENCES Grupy(grupa_id)
	on delete cascade
	on update cascade);
"""

connection_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'password',
        'host': 'localhost',
        'port': '5432'}

def delete_all_tables():
    delete_tables_sql = """
        drop table StudenciWGrupach;

        drop table Oceny;

        drop table Grupy;

        drop table Przedmioty;

        drop table Wykladowcy;

        drop table Studenci;"""
    
    
    
    with psycopg2.connect(**connection_params) as conn:
        cur = conn.cursor()
        try:
            cur.execute(delete_tables_sql)
        except psycopg2.errors.UndefinedTable:
            pass


def create_tables():
    with psycopg2.connect(**connection_params) as conn:
        cur = conn.cursor()
        cur.execute(DATABASE)

def insert_data_to_db(students_data, teachers_data, subjects_data, groups_data, marks_data, students_in_groups_data):
    with psycopg2.connect(**connection_params) as conn:
        cur = conn.cursor()
        
        cur.executemany("INSERT INTO Studenci (student_id, imie, nazwisko) VALUES (%s, %s, %s)", students_data)

        cur.executemany("INSERT INTO Wykladowcy (wykladowca_id, imie, nazwisko) VALUES (%s, %s, %s)", teachers_data)

        cur.executemany("INSERT INTO Przedmioty (przedmiot_id, przedmiot_nazwa, wykladowca) VALUES (%s, %s, %s)", subjects_data)

        cur.executemany("INSERT INTO Grupy (grupa_id, przedmiot_id) VALUES (%s, %s)", groups_data)

        cur.executemany("INSERT INTO Oceny (ocena_id, ocena, przedmiot_id, student, data) VALUES (%s, %s, %s, %s, %s)", marks_data)

        cur.executemany("INSERT INTO StudenciWGrupach (grupa_id, student_id) VALUES (%s, %s)", students_in_groups_data)