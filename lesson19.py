class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.name)

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Aziret", "J")
print(s.name, s.grade)
