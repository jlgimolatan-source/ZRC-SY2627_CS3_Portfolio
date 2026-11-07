class Patient:

    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

    def display_patient_type(self):
        return("Regular Patient")




class Senior(Patient):

    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.80

    def display_patient_type(self):
        return("Senior Patient")




class PhilHealth(Patient):

    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.85

    def display_patient_type(self):
        return("PhilHealth Patient")





patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = Senior("Maria Santos", 15000)
patient3 = PhilHealth("Pedro Reyes", 15000)

patients = [patient1, patient2, patient3]

print("Hospital Billing System")
print("-----------------------")

for patient in patients:
    print(f"Patient Name: {patient.get_name()}")
    print(f"Patient Type: {patient.display_patient_type()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
    print()