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
        return False
    else:
        print(f"Hospital has {result} vaccines left...")
        print("You can go to the hospital")
        return True


def recordData(human, status):
    if status:
        if human.hospital_selection == 1:
            Hospital_A.records.append(human)
        elif human.hospital_selection == 2:
            Hospital_B.records.append(human)
        elif human.hospital_selection == 3:
            Hospital_C.records.append(human)


def check(Human):
    print("\n")
    vaccine_stock(Human.hospital_selection)
    status = used_vaccine(Human.vaccine_selection, Human.hospital_selection)
    recordData(Human, status)


def readrecord():
    print("\n")
    print("Hospital A")
    for record in Hospital_A.records:
        print(f"{record.name} {record.age} {record.weight} {record.height} {record.vaccine_selection} {record.hospital_selection}")
    print("\n")
    print("Hospital B")
    for record in Hospital_B.records:
        print(f"{record.name} {record.age} {record.weight} {record.height} {record.vaccine_selection} {record.hospital_selection}")
    print("\n")
    print("Hospital C")
    for record in Hospital_C.records:
        print(f"{record.name} {record.age} {record.weight} {record.height} {record.vaccine_selection} {record.hospital_selection}")


Hospital_A = Hospital(3, 3)
Hospital_B = Hospital(2, 0)
Hospital_C = Hospital(0, 3)


Human_A = Human("A", 20, 64, 170, True, 1)
check(Human_A)
Human_B = Human("B", 30, 76, 175, False, 2)
check(Human_B)
Human_C = Human("C", 26, 91, 180, True, 3)
check(Human_C)
Human_D = Human("D", 18, 82, 177, False, 2)
check(Human_D)
Human_E = Human("E", 45, 53, 163, False, 2)
check(Human_E)
Human_E = Human("E", 45, 53, 163, False, 1)
check(Human_E)

readrecord()
