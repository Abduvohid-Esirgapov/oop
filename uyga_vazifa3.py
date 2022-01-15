'''
import  math

class Calculate:

    @staticmethod
    def add(num1, num2):
        return num1+num2

    @staticmethod
    def kvadrat(son):
        return son ** 2

    @staticmethod
    def qoldiqli_bulish(son):
        return  son % 2
    @staticmethod
    def ildiz(son):
        return math.sqrt(son)
print(Calculate.add(2,3))
print(Calculate.kvadrat(4))
print(Calculate.qoldiqli_bulish(15))
print(Calculate.ildiz(36))
'''

# Yuqorida student classiga yunalish va kurs abtributlarini qushing va bularni ma’lumot sifatida olish uchun metod yozing
# Teacher classiga mutaxasislik va daraja atributlarini qo’shing va buni ham ma’lumotlarni olish uchun metod ham yozing.

class User:
    def __init__(self, username, email, password ):
        self.username = username
        self.email = email
        self.password = password
    def login(self):
        return  f"{self.username} login"

    def logout(self):
        return f"{self.username} logout"

class Student(User):
     def __init__(self, username, email, password):
         super(). __init__(username, email, password)

     def task_send(self):
         return  f"{self.username} topshiriq yuborish send task"


class Teacher(User):
    def __init__(self username, email, password):
    super().__init__(username, email,password )

    def task_check(self):
        return  f"{self.username}  vazivfani tekshirish task check"


