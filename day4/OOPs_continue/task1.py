'''
Hospital
Patient
HospitalStaff
Pharmacy
'''
class Hospital:
    h_name = input("Enter Hospital name : ")
    h_address = input("Enter Hospital address : ")

class Pharmacy:
    p_med = input("Enter name of suppliments for the patient : ").split()

class HospitalStaff(Hospital):
    hs_name = input("Enter staff name : ")
    hs_designation = input("Enter staff designation : ")

class Patient(Pharmacy, HospitalStaff):
    p_name = input("Enter patient name : ")
    p_address = input("Enter patient address : ")
    p_mobo = int(input("Enter patient mobile number : "))

    def display_details(self):
        print("Hospital             :",self.h_name)
        print("Hospital address     :",self.h_address)
        print("Staff name           :",self.hs_name)
        print("Staff designation    :",self.hs_designation)
        print("Patient name         :",self.p_name)
        print("Patient address      :",self.p_address)
        print("Patient mobile no    :",self.p_mobo)
        print("Patient supplements  :",self.p_med)

obj = Patient()
obj.display_details()

