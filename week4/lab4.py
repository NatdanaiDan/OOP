list_yes = ["yes", "y", "ye", "ok", "have"]
list_no = ["no", "n", "nah", "nope", "not", "never"]


class Agent:
    def __init__(self):
        self._property_list = []

    def add_property(self):
        type_map = {("house", "rental"): HouseRental,
                    ("house", "purchase"): HousePurchase,
                    ("apartment", "rental"): ApartmentRental,
                    ("apartment", "purchase"): ApartmentPurchase}
        property_type = input("Enter property type: ")
        property_status = input("Enter property status: ")
        type_selection = type_map[(property_type, property_status)]
        dict_final = type_selection.prompt_init()
        print(dict_final)
        self._property_list.append(type_selection(**dict_final))

    def list_properties(self, show_all=False):
        if show_all:
            for property in self._property_list:
                print(property)
        else:
            id = int(input("Enter property ID: "))
            for property in self._property_list:
                if property.ID == id:
                    property.display()

    @staticmethod
    def yn_convertor(choice):
        if choice.lower() in list_yes:
            return True
        elif choice.lower() in list_no:
            return False
        else:
            raise ValueError("Please enter yes or no")


class Property:
    property_id = 1

    def __init__(self, square_Metres, num_bedrooms, num_bathrooms, **kwargs):
        self.square_Metres = square_Metres
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self._property_id = Property.property_id
        Property.property_id += 1

    @property
    def ID(self):
        return self._property_id

    def display(self):
        print("ID property"+str(self.ID))
        print("square_Metres:", self.square_Metres)
        print("num_bedrooms:", self.num_bedrooms)
        print("num_bathrooms:", self.num_bathrooms)

    def prompt_init():
        while True:
            try:
                return dict(square_Metres=float(input("Enter the square metres: ")),
                            num_bedrooms=int(input(
                                "Enter the number of bedrooms: ")),
                            num_bathrooms=int(input("Enter the number of bathrooms: ")))

            except ValueError:
                print("Invalid input, try again")


class House(Property):
    def __init__(self, garages, ferced_yard, **kwargs):
        super().__init__(**kwargs)
        self.garages = garages
        self.ferced_yard = ferced_yard

    def display(self):
        super().display()
        print("garages:", self.garages)
        print("ferced_yard:", self.ferced_yard)

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        while True:
            try:
                parent_init.update(garages=int(input("Enter the number of garages: ")),
                                   ferced_yard=Agent.yn_convertor(
                    input("Enter the number of ferced yard(Y/n): ")))
                return parent_init
            except ValueError:
                print("Invalid input, try again")


class Apartment(Property):
    def __init__(self, balcony, laundry_room, **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry_room = laundry_room

    def display(self):
        super().display()
        print(f"balcony: {self.balcony}")
        print(f"laundry_room: {self.laundry_room}")

    @ staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        while True:
            try:
                parent_init.update(balcony=Agent.yn_convertor(input("Have a balcony?(Y/n): ")),
                                   laundry_room=Agent.yn_convertor(input("Have a laundry room?(Y/n): ")))
                return parent_init
            except ValueError:
                print("Invalid input, try again")


class Rental:
    def __init__(self, furnished, rent, **kwargs):
        self.furnished = furnished
        self.rent = rent

    @ staticmethod
    def prompt_init():
        while True:
            try:
                return dict(furnished=Agent.yn_convertor(input("Have a furniture?(Y/n): ")),
                            rent=int(input("Enter the rental Price: ")))
            except ValueError:
                print("Invalid input, try again")

    def display(self):
        print(f"furnished: {self.furnished}")
        print(f"rent: {self.rent}")


class Purchase:
    def __init__(self, price, taxes, **kwargs):
        self.price = price
        self.taxes = taxes

    @ staticmethod
    def prompt_init():
        while True:
            try:
                return dict(price=int(input("Enter the price: ")),
                            taxes=int(input("Enter the taxes: ")))
            except ValueError:
                print("Invalid input, try again")

    def display(self):
        print(f"price: {self.price}")
        print(f"taxes: {self.taxes}")


class HouseRental(House, Rental):
    def __init__(self, **kwargs):
        House.__init__(self, **kwargs)
        Rental.__init__(self, **kwargs)

    @ staticmethod
    def prompt_init():
        return (House.prompt_init() | Rental.prompt_init())

    def display(self):
        House.display(self)
        Rental.display(self)


class HousePurchase(House, Purchase):

    def __init__(self, **kwargs):
        House.__init__(self, **kwargs)
        Purchase.__init__(self, **kwargs)

    @ staticmethod
    def prompt_init():
        return (House.prompt_init()) | (Purchase.prompt_init())

    def display(self):
        House.display(self)
        Purchase.display(self)


class ApartmentRental(Apartment, Rental):
    def __init__(self, **kwargs):
        Apartment.__init__(self, **kwargs)
        Rental.__init__(self, **kwargs)

    @ staticmethod
    def prompt_init():
        return (Apartment.prompt_init()) | (Rental.prompt_init())

    def display(self):
        Apartment.display(self)
        Rental.display(self)


class ApartmentPurchase(Apartment, Purchase):
    def __init__(self, **kwargs):
        Apartment.__init__(self, **kwargs)
        Purchase.__init__(self, **kwargs)

    @ staticmethod
    def prompt_init():
        return (Apartment.prompt_init()) | (Purchase.prompt_init())

    def display(self):
        Apartment.display(self)
        Purchase.display(self)


A1 = Agent()
A1.add_property()
A1.list_properties()
