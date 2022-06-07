class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, average_grade):
        self.average_grade = average_grade
        super().__init__(name, age)
        print("Student created!")

    def study(self):
        print(f'{self.name} studies')

    def say_hello(self):
        print(f'Student with name {self.name} says hello!')


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        print('Teacher created!')

    def teach(self):
        print(f'{self.name} teaches')

    def say_hello(self):
        print(f'Teacher with name {self.name} says hello!')


def introduce(person):
    person.say_hello()


people_arr = [Student('Tom', 18, 3.5), Teacher('Katy', 35), Student('Bob', 26, 4.8)]
for person in people_arr:
    introduce(person)
