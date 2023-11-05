class Student:
    def __init__(self, full_name: str, agerage_mark: float):
        self.full_name = full_name
        self.agerage_mark = agerage_mark

    def get_scholarship(self):
        if self.agerage_mark < 6:
            return 60
        elif self.agerage_mark < 8:
            return 80
        else:
            return 100

    def is_excellent(self):
        if self.agerage_mark >= 9:
            return True
        else:
            return False

#student = Student('Dmitry Latokhin', 6.8)

#print(student.get_scholarship())
#print(student.is_excellent())
