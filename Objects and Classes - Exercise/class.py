class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, student_name, grade):
        if len(self.students) <= self.__students_count:
            self.students.append(student_name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = f"{(sum(self.grades) / len(self.students)):.2f}"
        return float(average_grade)

    def __repr__(self):
        average_grade = f"{(sum(self.grades) / len(self.students)):.2f}"
        students = ", ".join(self.students)
        return f"The students in {self.name}: {students}. Average grade: {average_grade}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)