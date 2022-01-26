from unittest import result


class Human:
    def __init__(self, name, age, weight, height, vaccine_selection, hospital_selection):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.vaccine_selection = vaccine_selection
        self.hospital_selection = hospital_selection


class Hospital:
    def __init__(self, Moderna_vaccine, Pfizer_vaccine):
        self.Moderna_vaccine = Moderna_vaccine
        self.Pfizer_vaccine = Pfizer_vaccine
        self.records = []
# True pfizer false modern


def vaccine_stock(hospital_selection):
    if hospital_selection == 1:
        print(
            f"Hospital A has Moderna {Hospital_A.Moderna_vaccine} Pfizer {Hospital_A.Pfizer_vaccine}")
    elif hospital_selection == 2:
        print(
            f"Hospital B has Moderna {Hospital_B.Moderna_vaccine} Pfizer {Hospital_B.Pfizer_vaccine}")
    elif hospital_selection == 3:
        print(
            f"Hospital C has Moderna {Hospital_C.Moderna_vaccine} Pfizer {Hospital_C.Pfizer_vaccine}")


def used_vaccine(vaccine_selection, hospital_selection):
    if not vaccine_selection:
        if hospital_selection == 1:
            Hospital_A.Moderna_vaccine -= 1
            result = Hospital_A.Moderna_vaccine
        elif hospital_selection == 2:
            Hospital_B.Moderna_vaccine -= 1
            result = Hospital_B.Moderna_vaccine
        elif hospital_selection == 3:
            Hospital_C.Moderna_vaccine -= 1
            result = Hospital_C.Moderna_vaccine
    else:
        if hospital_selection == 1:
            Hospital_A.Pfizer_vaccine -= 1
            result = Hospital_A.Pfizer_vaccine
        elif hospital_selection == 2:
            Hospital_B.Pfizer_vaccine -= 1
            result = Hospital_B.Pfizer_vaccine
        elif hospital_selection == 3:
            Hospital_C.Pfizer_vaccine -= 1
            result = Hospital_C.Pfizer_vaccine

    if result < 0:
        print("Stock is empty Please select another hospital")
    else:
        print(f"Hospital has {result} vaccines left")\



def recordData(human):
    if human.hospital_selection == 1:
        Hospital_A.records.append(human)
    elif human.hospital_selection == 2:
        Hospital_B.records.append(human)
    elif human.hospital_selection == 3:
        Hospital_C.records.append(human)


Hospital_A = Hospital(3, 3)
Hospital_B = Hospital(2, 0)
Hospital_C = Hospital(0, 3)


Human_A = Human("A", 20, 64, 170, True, 1)
vaccine_stock(Human_A.hospital_selection)
used_vaccine(Human_A.vaccine_selection, Human_A.hospital_selection)
recordData(Human_A)
Human_B = Human("B", 30, 76, 175, False, 2)
vaccine_stock(Human_B.hospital_selection)
used_vaccine(Human_B.vaccine_selection, Human_B.hospital_selection)
recordData(Human_B)
Human_C = Human("C", 26, 91, 180, True, 3)
vaccine_stock(Human_C.hospital_selection)
used_vaccine(Human_C.vaccine_selection, Human_C.hospital_selection)
recordData(Human_C)
Human_D = Human("D", 18, 82, 177, False, 2)
vaccine_stock(Human_D.hospital_selection)
used_vaccine(Human_D.vaccine_selection, Human_D.hospital_selection)
recordData(Human_D)
Human_E = Human("E", 45, 53, 163, False, 2)
vaccine_stock(Human_E.hospital_selection)
used_vaccine(Human_E.vaccine_selection, Human_E.hospital_selection)
recordData(Human_E)

for i in range(len(Hospital_A.records)):
    print(Hospital_A.records[i].name, end=" ")
    print(Hospital_A.records[i].age, end=" ")
    print(Hospital_A.records[i].weight, end=" ")
    print(Hospital_A.records[i].height, end=" ")
    print(Hospital_A.records[i].vaccine_selection, end=" ")
    print(Hospital_A.records[i].hospital_selection, end=" ")
    print("")
for i in range(len(Hospital_B.records)):
    print(Hospital_B.records[i].name, end=" ")
    print(Hospital_B.records[i].age, end=" ")
    print(Hospital_B.records[i].weight, end=" ")
    print(Hospital_B.records[i].height, end=" ")
    print(Hospital_B.records[i].vaccine_selection, end=" ")
    print(Hospital_B.records[i].hospital_selection, end=" ")
    print("")
for i in range(len(Hospital_C.records)):
    print(Hospital_C.records[i].name, end=" ")
    print(Hospital_C.records[i].age, end=" ")
    print(Hospital_C.records[i].weight, end=" ")
    print(Hospital_C.records[i].height, end=" ")
    print(Hospital_C.records[i].vaccine_selection, end=" ")
    print(Hospital_C.records[i].hospital_selection, end=" ")
    print("")
