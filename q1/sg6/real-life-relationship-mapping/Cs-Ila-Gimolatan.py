
class Student:
    def __init__(self, full_name, student_number):
        self.full_name = full_name
        self.student_number = student_number


class Course:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.enrolled_students = []

    def add_student(self, new_student):
        self.enrolled_students.append(new_student)



science = Course("General Science")


pupil_a = Student("Jane", 101)
pupil_b = Student("Shin", 102)
pupil_c = Student("Nicki Enaj", 103)


science.add_student(pupil_a)
science.add_student(pupil_b)
science.add_student(pupil_c)


print("Subject Name:", science.subject_name)
print("Number of Enrolled Students:", len(science.enrolled_students))
print("\nEnrolled Student List:")

for pupil in science.enrolled_students:
    print(f"Name: {pupil.full_name} | ID: {pupil.student_number}")