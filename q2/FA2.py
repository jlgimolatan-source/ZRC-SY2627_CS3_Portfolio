
class Patient():

    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = 0

    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name = name  

    def get_bil_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount





class Senior(Patient):

    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill(self) * 0.80

    def get_name(self):
        pass

    




    
class PhilHealth(Patient):

    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill(self) * 0.85

    def get_name(self):
        pass

patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = Senior("Maria Santos", 15000)
patient3 = PhilHealth("Pedro Reyes", 15000)

# patients = [("Regular Patient", patient1), 
#             ("Senior Patient", patient2), 
#             ("PhilHealth Patient", patient3)
# ]

for patient_type, patient in patients:
    print(f"{patient_type}: {patient_type.get_name()}")
    print(f"Original Bill: {patient_type.bill_amount():.,2f}")
    print(f"Final Bill: {patient_type.calculate_bill():.,2f}")