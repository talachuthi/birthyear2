# Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("\n----- Vehicle Information -----")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")
        print("--------------------------------\n")


# Main app
def main():
    print("Enter vehicle information below:\n")

    vehicle_type = "car"  # required by assignment

    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")

    # validate doors input
    while True:
        doors = input("Enter number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        print("Please enter either 2 or 4.")

    # validate roof input
    while True:
        roof = input("Enter type of roof (solid or sun roof): ").lower()
        if roof in ["solid", "sun roof"]:
            break
        print("Please enter 'solid' or 'sun roof'.")

    # create object
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # display results
    car.display_info()


# Run program
if __name__ == "__main__":
    main()
    