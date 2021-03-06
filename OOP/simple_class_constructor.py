class Person:
    count = 0

    def __init__(self, name, surname, birth_place, birth_year=0):
        self.name = name
        self.surname = surname
        self.birth_place = birth_place
        self.birth_year = birth_year
        Person.count += 1  # если нет атрибута объекта, то он берется из поля класса
        print(f'Hello, {name}!!!\nYou are the {Person.count} user!')

    def get_age(self, year):
        return year - self.birth_year

    def print_info(self, n=1, year=2022):
        for i in range(n):
            print(
                f'name: {self.name}, second name: {self.surname}, from: {self.birth_place}, age: {self.get_age(year)}')


vadim = Person('Vadim', 'Makarov', 'Saldus', 1988)
nadya = Person('Nadya', 'Makarova', 'Karamishevo', 1993)
greg = Person('Grigory', 'Spirin', 'Karamishevo', 1996)
nastya = Person('Nastya', 'Ogievich', 'Ozersk', 1999)

# Person.quantity(self=Person)
# nadya.print_info(3, year=2005)
