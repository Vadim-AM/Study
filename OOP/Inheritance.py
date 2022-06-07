class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f'{self.name} is barking!')


class Cat(Animal):
    def meow(self):
        print(f'{self.name} says Meow!')


class Frog(Animal):
    def eat(self):
        print(f'Frog with name {self.name} is eating!')


d1 = Dog('Achey', 'Huskey')
c1 = Cat('Bars')
f1 = Frog('Kwa')
d1.bark()
print(d1.breed)
d1.eat()
c1.meow()
f1.eat()
