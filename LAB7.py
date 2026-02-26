try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Result =", c)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Fatimah", 22)
p.age = p.age + 1
print("Name:", p.name)
print("Age:", p.age)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def add_bonus(self, bonus):
        self.salary += bonus

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

m = Manager("Fatimah", 5000)
m.add_bonus(1000)
m.display()


class Student:
    def __init__(self):
        try:
            self.name = "Fatimah"
            age = 22
            if age < 0:
                print("Age cannot be negative")
                self.age = None
            else:
                self.age = age + 1
        except ValueError:
            print("Invalid age")
            self.age = None

    def show(self):
        if self.age != None:
            print("Name:", self.name)
            print("Age:", self.age)

s = Student()
s.show()