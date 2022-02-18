class Agent:
    def __init__(self):
        self.property_list = []

    def add_property(self):
        type_map = {("house", "rental"): HouseRental,
                    ("house", "purcahse"): HousePurchase,
                    ("apartment", "rental"): ApartmentRental,
                    ("apartment", "purcahse"): ApartmentPurchase}
        property_type = input("Enter property type: ")
        property_status = input("Enter property status: ")
        type_selection = type_map[(property_type, property_status)]
        dict_final = type_selection.prompt_init()
        print(dict_final)
        self.property_list.append(type_selection(**dict_final))

    def list_properties(self, show_all=False):
        if show_all:
            for property in self.property_list:
                print(property)
        else:
            id = int(input("Enter property ID: "))
            self.property_list[id].display()


class Property:
    def __init__(self, square_Metres, num_bedrooms, num_bathrooms, **kwargs):
        self.square_Metres = square_Metres
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms

    def display(self):
        print("square_Metres:", self.square_Metres)
        print("num_bedrooms:", self.num_bedrooms)
        print("num_bathrooms:", self.num_bathrooms)

    def prompt_init():
        return dict(square_Metres=input("Enter the square metres: "),
                    num_bedrooms=input("Enter the number of bedrooms: "),
                    num_bathrooms=input("Enter the number of bathrooms: "))


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
        parent_init.update(garages=input("Enter the number of garages: "),
                           ferced_yard=input("Enter the number of ferced yard: "))
        return parent_init


class Apartment(Property):
    def __init__(self, balcony, laundry_room, **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry_room = laundry_room

    def display(self):
        super().display()
        print(f"balcony: {self.balcony}")
        print(f"laundry_room: {self.laundry_room}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        parent_init.update(balcony=input("Have a balcony?: "),
                           laundry_room=input("Have a laundry room?: "))
        return parent_init


class Rental:
    def __init__(self, furnished, rent, **kwargs):
        self.furnished = furnished
        self.rent = rent

    @staticmethod
    def prompt_init():
        return dict(furnished=input("Have a furniture?: "),
                    rent=input("Enter the rental Price: "))

    def display(self):
        print(f"furnished: {self.furnished}")
        print(f"rent: {self.rent}")


class Purchase:
    def __init__(self, price, taxes, **kwargs):
        self.price = price
        self.taxes = taxes

    @staticmethod
    def prompt_init():
        return dict(price=input("Enter the price: "),
                    taxes=input("Enter the taxes: "))

    def display(self):
        print(f"price: {self.price}")
        print(f"taxes: {self.taxes}")


class HouseRental(House, Rental):
    def __init__(self, **kwargs):
        House.__init__(self, **kwargs)
        Rental.__init__(self, **kwargs)

    @staticmethod
    def prompt_init():
        return (House.prompt_init() | Rental.prompt_init())

    def display(self):
        House.display(self)
        Rental.display(self)


class HousePurchase(House, Purchase):

    def __init__(self, **kwargs):
        House.__init__(self, **kwargs)
        Purchase.__init__(self, **kwargs)

    @staticmethod
    def prompt_init():
        return (House.prompt_init()) | (Purchase.prompt_init())

    def display(self):
        House.display(self)
        Purchase.display(self)


class ApartmentRental(Apartment, Rental):
    def __init__(self, **kwargs):
        Apartment.__init__(self, **kwargs)
        Rental.__init__(self, **kwargs)

    @staticmethod
    def prompt_init():
        return (Apartment.prompt_init()) | (Rental.prompt_init())

    def display(self):
        Apartment.display(self)
        Rental.display(self)


class ApartmentPurchase(Apartment, Purchase):
    def __init__(self, **kwargs):
        Apartment.__init__(self, **kwargs)
        Purchase.__init__(self, **kwargs)

    @staticmethod
    def prompt_init():
        return (Apartment.prompt_init()) | (Purchase.prompt_init())

    def display(self):
        Apartment.display(self)
        Purchase.display(self)


A1 = Agent()
A1.add_property()
A1.list_properties()
