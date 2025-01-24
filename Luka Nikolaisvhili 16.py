class Student:
    def __init__(self, name, surname, personal_id, birth_year, grades):
        self.name = name
        self.surname = surname
        self.personal_id = personal_id
        self.birth_year = birth_year
        self.grades = grades

    def __str__(self):
        grades_str = ", ".join(f"{subject}: {grade}" for subject, grade in self.grades.items())
        return (f"Student Name: {self.name} {self.surname}\n"
                f"Personal ID: {self.personal_id}\n"
                f"Birth Year: {self.birth_year}\n"
                f"Grades: {grades_str}")

    def years_until_18(self):
        current_year = 2025
        age = current_year - self.birth_year
        return max(0, 18 - age)



student1 = Student("Dwayne", "Johnson", "01010112345", 1972, {"math": 85, "programming": 84})
student2 = Student("Luka", "Nikolaishvili", "01452003907", 2010, {"math": 69, "programming": 100})
student3 = Student("Lionel", "Messi", "03030398765", 1987, {"math": 95, "programming": 70})


print(student1)
print(f"Years until {student1.name} turns 18: {student1.years_until_18()}\n")

print(student2)
print(f"Years until {student2.name} turns 18: {student2.years_until_18()}\n")

print(student3)
print(f"Years until {student3.name} turns 18: {student3.years_until_18()}")
