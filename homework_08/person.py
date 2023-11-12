import datetime

class Person:
    def __init__(self, full_name: str, age: int, gender: str):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f'{self.full_name} ({self.gender}), {self.age} years old')

    def get_birth_year(self):
        # return 2023 - self.age
        date_now = datetime.datetime.now().year
        return date_now - self.age

person = Person('Dmitry Latokhin', 36, 'M')

#person.print_person_info()

#print(person.get_birth_year())
