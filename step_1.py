# имя
# дата рождения
# адрес
# класс учебной группы
# * название
# * студенты
# * методы для добавления, удаления, и просмотра студента группы

class Student:

    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address


class Group:

    def __init__(self, name):
        self.name = name
        self.students = []

    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls)

    def __del__(self):
        return Group(self.name)

    def views(self):
        pass


student_1 = Student('Иван', '15.05.2005', 'ул.Ленина 113')
student_2 = Student('Андрей', '21.07.2005', 'ул.Пушкина 102')

group_1 = Group('ИСиП-33')
group_1.__add__(student_1)
group_1.__del__()
