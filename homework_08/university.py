from student import Student

students = [Student('Nicolas', 7.5),
            Student('Dan', 4.6),
            Student('Maria', 8),
            Student('Bred', 9.9),
            Student('Katrin', 8.2)]


def calc_sum_scholarship(students):
    summ_scholarship = 0
    for student in students:
        summ_scholarship += student.get_scholarship()
    return f'{summ_scholarship} рублей.'


def get_excellent_student_count(students):
    count = 0
    for student in students:
        if student.is_excellent():
            count += 1
    return f'Количество отличников: {count}'

# print(calc_sum_scholarship(students))
# print(get_excellent_student_count(students))
