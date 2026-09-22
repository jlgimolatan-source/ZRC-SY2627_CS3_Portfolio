class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = 0
        self.__submitted_files = []

    def __validate_grade(self, score):
        if score > 0 and len(self.__submitted_files) > 0:
            return True
        else:
            return False

    def __check_submission_status(self):
        if len(self._AssignmentSubmission__submitted_files) == 0:
            is_submitted = False
            return("Missing")
        else:
            status = len(self._AssignmentSubmission__submitted_files)
            return(f"Submitted ( {status} files )")
        

    def __is_duplicate(self, filename):
        if filename in self.__submitted_files:
            print(f"--> [Warning] '{filename}' is already attached!")
            return True


    def add_file(self, filename):
        if self.__is_duplicate(filename):
            return
        else:
            self.__submitted_files.append(filename)
            print(f"--> [Success] {self.student_name} attached '{filename}'. Total files: {len(self.__submitted_files)}")
        

    def remove_file(self, filename):
        if self.__grade > 0:
            print(f"--> [Warning] {self.student_name} cannot remove files. Assignment already graded.")
            return
        elif filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            print(f"--> [Success] {self.student_name} removed '{filename}'.")

    def assign_grade(self, score):
        if self.__validate_grade(score):
            self.__grade = score
            print(f"--> [Success] Grade {score} officially assigned to {self.student_name}.")
            return score
        else:
            print(f"--> [Error] Cannot grade. No files submitted for {self.student_name}.")
        
    def get_grade(self):
        print(self._AssignmentSubmission__grade)
        
    def view_files(self):
        if not self.__submitted_files:
            return "No files submitted"
        return ", ".join(self.__submitted_files)

    def get_status_report(self):
        status = self._AssignmentSubmission__check_submission_status()
        if self.__grade == 0:
            display = "Not Graded"
        else:
            display = self.__grade
        return(f"ID: {self.student_id} | Name: {self.student_name} | Status: {status} | Grade: {display}")

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", "2026-10-01")
student3 = AssignmentSubmission("Juan dela Cruz", "pshs-1033-x", "CS-104", "2026-10-01")
student4 = AssignmentSubmission("Maria Santos", "pshs-1044-x", "CS-105", "2026-10-01")
student5 = AssignmentSubmission("Jose Reyes", "pshs-1055-x", "CS-106", "2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print ("--- TEST SCENARIO 2: Removing Files from the List ---") 
student2.add_file("wrong_homework.docx") 
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88) 
print(f"Adelle's Files: {student2.view_files()}\n") 

print ("--- TEST SCENARIO 3: Preventing Duplicate Files---") 
student3.add_file("script.py") 
student3.add_file("script.py")
print (f"Juan's Files: {student3.view_files()}\n") 

print("--- TEST SCENARIO 4: Removing file after being graded ---") 
student4.add_file("exam answers.pdf") 
student4.assign_grade(75) 
student4.remove_file("exam answers.pdf")
print()

print ("--- TEST SCENARIO 5: Empty List Handling ---") 
student5.add_file("draft.txt") 
student5.remove_file("draft.txt") 
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---") 
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())