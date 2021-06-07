# имя
# дата рождения
# адрес
# класс учебной группы
# * название
# * студенты

class Student:

    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address

    def display_info(self):
        print('Студент: ', self.name)


class Group:

    def __init__(self, name):
        self.name = name
        self.student = Student
