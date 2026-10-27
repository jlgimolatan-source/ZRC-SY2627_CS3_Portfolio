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








class Senior(Patient):

    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.80









class PhilHealth(Patient):

    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.85







patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = Senior("Maria Santos", 15000)
patient3 = PhilHealth("Pedro Reyes", 15000)

patients = [
    ("Regular Patient", patient1),
    ("Senior Patient", patient2),
    ("PhilHealth Patient", patient3)
]

print("Hospital Billing System")
print("-----------------------")

for patient_type, patient in patients:
    print(f"{patient_type}: {patient.get_name()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
    print()