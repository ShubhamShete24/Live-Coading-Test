class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return print(self.num1 + self.num2)

    def subtract(self):
        if self.num1 < self.num2:
            self.num1, self.num2 = self.num2, self.num1
        return print(self.num1 - self.num2)

    def multiply(self):
        return print(self.num1 * self.num2)

    def divide(self):
        return print(float(self.num1 / self.num2))


a = Calculator(10, 94)
a.add()
a.subtract()
a.multiply()
a.divide()
