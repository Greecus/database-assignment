from faker import Faker
from random import randint, shuffle
from databese_func import create_tables, insert_data_to_db

def gen_fake_data():
    example_subjects = ["Polski", "Matematyka", "Biologia", "Chemia", "Historia", "WOS", "Fizyka", "WF"]

    fake = Faker("pl_PL")

    n_students = randint(30, 50)
    n_subjects = randint(5, 8)
    n_teacher = randint(3, 5)
    groups_per_subject = 3
    max_marks_per_student = 20

    students_data = [(id, fake.first_name(), fake.last_name()) for id in range(1,n_students+1)]

    teachers_data = [(id, fake.first_name(), fake.last_name()) for id in range(1,n_teacher+1)]

    teacher_ids_list = list(range(1,n_teacher+1))
    shuffle(teacher_ids_list)
    shuffle(example_subjects)
    teacher_ids_list = teacher_ids_list * 3
    subjects_data = [(id, subject, teacher_id) 
                     for id, subject, teacher_id 
                     in zip(
                         range(1,n_subjects+1),
                         example_subjects[:n_subjects], 
                         teacher_ids_list)]
    
    groups_data = []
    group_index = 1
    for subject_id in range(1,n_subjects+1):
        for _ in range(groups_per_subject):
            groups_data.append((group_index,subject_id))
            group_index += 1
    
    marks_data = []
    mark_index = 1
    for n in range(1,n_students+1):
        for _ in range(randint(4,max_marks_per_student)):
            marks_data.append((mark_index, randint(1,6), randint(1,n_subjects), n, fake.date()))
            mark_index += 1

    students_in_groups_data = []
    for student_id in range(1,n_students+1):
        for subject_id in range(n_subjects):
            group_id = subject_id * groups_per_subject + student_id%groups_per_subject+1
            students_in_groups_data.append((group_id,student_id))


    return students_data, teachers_data, subjects_data, groups_data, marks_data, students_in_groups_data

if __name__ == "__main__":
    create_tables()

    students_data, teachers_data, subjects_data, groups_data, marks_data, students_in_groups_data = gen_fake_data()
    insert_data_to_db(students_data, teachers_data, subjects_data, groups_data, marks_data, students_in_groups_data)
    