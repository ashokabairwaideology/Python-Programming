class Student:
    def __init__(self, first, last, age, major):
        self.first = first
        self.last = last
        self.age = age
        self.major = major

    def profile(self):
        print(f"Student name {self.first + ' ' + self.last}")
        print(f"Student age: {self.age}")
        print(f"Major: {self.major}")



s = Student('Ashoka' , 'Bairwa', 22, 'software engineer')

s.profile()
