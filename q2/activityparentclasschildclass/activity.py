
class CampusDirector:

    def __init__(self, announcement):
        self.announcement = announcement

    def announce(self):
        return(f"Announcement from CD: '{self.announcement}'")

    def talk(self):
        return(f"Hello PISAY ZRC!!!")



class CuriculumInsDiv(CampusDirector):

    def __init__(self, announcement, school_year, event, request):
        super().__init__(announcement)
        self.school_year = school_year
        self.event = event
        self.request = request

    def calendar(self):
        return(f"SY: {self.school_year} | Event: {self.event}")

    def implement(self):
        return(f"Your request '{self.request}' has been implemented.")


class StudentSerDiv(CampusDirector):

    def __init__(self, announcement, service_availed):
        super().__init__(announcement)
        self.service_availed = service_availed

    def avail_service(self):
        return(f"You have successfully availed {self.service_availed}")

    def services(self):
        return(f"Services Menu: Report, Feedback, Suggestions")


class SsdSecretary(StudentSerDiv):

    def __init__(self, announcement, service_availed, help):
        super().__init__(announcement, service_availed)
        self.help = help

    def secretary_status(self):
        return(self.help)



class CurriculumInsDivSecretary(CuriculumInsDiv):

    def __init__(self, announcement, school_year, event, request, duties):
        super().__init__(announcement, school_year, event, request)
        self.duties = duties

    def cid_secretary_duties(self):
        return(self.duties)

class GieLord(CuriculumInsDiv):

    def __init__(self, announcement, school_year, event, request, activities):
        super().__init__(announcement, school_year, event, request)
        self.activities = activities

    def do_activity(self):
        return(self.activities)

class JohnBonJuvi(CuriculumInsDiv):

    def __init__(self, announcement, school_year, event, request, laboratory_sched):
        super().__init__(announcement, school_year, event, request)
        self.laboratory_sched = laboratory_sched

    def status_laboratory(self):
        return(self.laboratory_sched)

class JaneGimolatan(JohnBonJuvi):

    def __init__(self, announcement, school_year, event, request, laboratory_sched, seating_arrangement):
        super().__init__(announcement, school_year, event, request, laboratory_sched)
        self.seating_arrangement = seating_arrangement
    
    def view_seat(self):
        return(self.seating_arrangement)


jane = JaneGimolatan(announcement="Exam week is coming!", school_year="2026-2027", event="Panagsangka", request="I hope naay Sabayang Pagbigkas", laboratory_sched="Monday 9:00 AM", seating_arrangement="Row 1")

print(jane.view_seat())        

print(jane.status_laboratory()) 

print(jane.calendar())         

print(jane.talk())             

