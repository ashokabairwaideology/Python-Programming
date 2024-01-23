class Student:
    def __init__(self, first, last, age, major):
        self.first = first
        self.last = last
        self.age = age
        self.major = major
        self.courses = []

    def profile(self):
        print(f"Student name {self.first + ' ' + self.last}")
        print(f"Student age: {self.age}")
        print(f"Major: {self.major}")


    def enrol(self, course):
        self.courses.append(course)
        print(f"enrolled {self.first} in {course}")


    def show_courses(self):
        print(f"{self.first + ''  + self.last} is taking the following courses")
        for course in self.courses:
            print(course)


s = Student('Sally' , 'Harris', 20, 'Biology')

s.enrol('Biochemistry I')
# enrolled Sally in Biochemistry I

s.enrol('Literature')
# enrolled Sally in Literature

s.enrol('Mathematics')
# enrolled Sally in Mathematics

s.show_courses()
# SallyHarris is taking the following courses
# Biochemistry I
# Literature
# Mathematics
