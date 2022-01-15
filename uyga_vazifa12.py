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