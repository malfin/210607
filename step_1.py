# имя
# дата рождения
# адрес

class Student:
    name = 'Алексей'

    dob = '19.03.2002'

    address = 'ул. Ленина, 113'

    def display_info(self):
        print('Привет, ', self.name)
        print('Дата рождения:', self.dob)
        print('Адресс: ', self.address)


student_1 = Student()
student_1.display_info()
