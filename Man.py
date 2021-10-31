class Man:
    def __init__(self, name, surname, ege):
        self.name = name
        self.surname = surname
        self.ege = ege

    def __str__(self):
        return f'Name - {self.name} {self.surname} \nege - {self.ege}'


man_1 = Man('Ivan', 'Ivanov', 18)
print(man_1)