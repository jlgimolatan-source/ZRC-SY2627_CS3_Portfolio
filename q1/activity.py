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
        if grade > 0:
            print("Graded.")
        else:
            print("Not Graded.")

    def __check_submittion_status(self):
        if len(self._AssignmentSubmission__submitted_files) == 0:
            is_submitted = False
        else:
            status = len(self._AssignmentSubmission__submitted_files)
            return(f"Submitted {status} files")
        

    def __is_duplicate(self, filename):
        if len(submitted_files) != len(set(submitted_files)):
            print("Your submitted files has duplicates, please remove the duplicate.")
        else:
            print("Your submission does not have duplicates, please proceed.")

    def add_file(self, filename):
        self.__submitted_files.append(filename)
        

    def remove_file(self, filename):
        self.__submitted_files.remove(filename)

    def assign_grade(self, score):
        self.grade = score
        
    def get_grade(self):
        print(grade)
        
    def view_files(self):
        files = submitted_files
        print(files)

    def get_status_report(self):
        status = self._AssignmentSubmission__check_submittion_status()
        list = [self.student_id, self.student_name, status, self.grade]
        return("ID:", list[0], "| Name:", list[1], "| Status:", list[2], "| Grade:", self.grade)

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", "2026-10-01")
student3 = AssignmentSubmission("Juan dela Cruz", "pshs-1968-x", "CS-104", "2026-10-01")
student2 = AssignmentSubmission("Maria Santos", "pshs-1967-x", "CS-105", "2026-10-01")
student2 = AssignmentSubmission("Jose Reyes", "pshs-1978-x", "CS-106", "2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print ("--- TEST SCENARIO 2: Removing Files from the List ---") 
student2.add file("wrong homework.docx") 
student2.remove file ("wrong homework. docx") 
student2.assign grade (88) 
print(f"Adelle's Files: {student2.view filesOn") 

print ("--- TEST SCENARIO 3: Preventing Duplicate Files---") 
student3.addfile("script.py") 
student3.add file("script.py")
print (E"Juan's Files: {student3.view files (n") 

print("-- TEST SCENARIO 4: Removing file after being graded--") 
student4.add file ("exam answers.pdf") 
student4.assign grade ("75") 
student4.remove file ("exam answers.pdf")
print()

print ("--- TEST SCENARIO 5: Empty List Handling ---") 
student5.add file("draft.txt") 
student5.remove file("draft.txt") 
student5.assign grade (100)

print("--- FINAL SYSTEM REPORT---") 
print(studentl.get status report())
print(student2.get status_report())
print (student3.get_ status_report())
print (student4.get status_report())
print (student5.get status report())