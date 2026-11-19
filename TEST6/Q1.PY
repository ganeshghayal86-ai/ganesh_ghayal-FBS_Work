# Write a program which calculates toll calculation on some location following
# is data provided:
# Many vehicles goes through the toll every vehicle has to pay the basic
# toll + extra charges if any.
# two wheelers have to pay basic toll Rs 20 three wheelers have to pay
# 30 and four wheelers have to pay 40
# heavy veheicles i.e. Vehicles having wheels more than four, have to
# pay 60 Rs as basic toll
# extra charges :
# for two wheelers if no. of persons are more than two extra charge
# =10/person
# for three wheelers if no. of persons are more than 3 extra charge
# =20/person
# for four wheelers if no. of persons are more than 4 extra charge
# =40/person
# for heavy vehicle if no. of person are more than 6 extra charges
# =100/person.
# Show polymorphic behaviour in main. Main module should be
# designed in such way that toll should easily operate it through
# interactive menu driven program .
# Object of vehicle class should not be possible.

from abc import ABC, abstractmethod



class Vehicle(ABC):

    def __init__(self, vehicle_no, no_of_persons):
        self.vehicle_no = vehicle_no
        self.no_of_persons = no_of_persons

    @abstractmethod
    def calculate_toll(self):
        pass



class TwoWheeler(Vehicle):

    def __init__(self, vehicle_no, no_of_persons):
        super().__init__(vehicle_no, no_of_persons)

    def calculate_toll(self):
        toll = 20

        if self.no_of_persons > 2:
            extra = self.no_of_persons - 2
            toll += extra * 10

        return toll



class ThreeWheeler(Vehicle):

    def __init__(self, vehicle_no, no_of_persons):
        super().__init__(vehicle_no, no_of_persons)

    def calculate_toll(self):
        toll = 30

        if self.no_of_persons > 3:
            extra = self.no_of_persons - 3
            toll += extra * 20

        return toll


class FourWheeler(Vehicle):

    def __init__(self, vehicle_no, no_of_persons):
        super().__init__(vehicle_no, no_of_persons)

    def calculate_toll(self):
        toll = 40

        if self.no_of_persons > 4:
            extra = self.no_of_persons - 4
            toll += extra * 40

        return toll



class HeavyVehicle(Vehicle):

    def __init__(self, vehicle_no, no_of_persons):
        super().__init__(vehicle_no, no_of_persons)

    def calculate_toll(self):
        toll = 60

        if self.no_of_persons > 6:
            extra = self.no_of_persons - 6
            toll += extra * 100

        return toll



while True:

    print("\n----- TOLL PLAZA -----")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you for visiting Toll Plaza")
        break

    elif choice in (1, 2, 3, 4):

        vehicle_no = input("Enter Vehicle Number: ")
        persons = int(input("Enter Number of Persons: "))

        if choice == 1:
            obj = TwoWheeler(vehicle_no, persons)

        elif choice == 2:
            obj = ThreeWheeler(vehicle_no, persons)

        elif choice == 3:
            obj = FourWheeler(vehicle_no, persons)

        elif choice == 4:
            obj = HeavyVehicle(vehicle_no, persons)

        print("\nVehicle Number:", obj.vehicle_no)
        print("Number of Persons:", obj.no_of_persons)
        print("Total Toll: Rs.", obj.calculate_toll())

    else:
        print("Invalid Choice")
