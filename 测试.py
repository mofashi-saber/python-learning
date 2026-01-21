class Student:
    def __init__(self, name, age, socre):
        self.name = name
        self.age = age
        self.score = socre
    def print_date(self):
        print(f"{self.name}, {self.age}, {self.score}")

student1 = Student("saber", 18, 80)
student1.print_date()
student2 = Student("hide", 20, 80)
student2.print_date()
