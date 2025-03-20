class Car:
    def __init__(self, fuel, mileage, fuel_consumption_rate):
        self.__fuel = fuel
        self.mileage = mileage
        self.fuel_consumption_rate = fuel_consumption_rate

    def travel(self, distance):
        max_possible = self.get_remaining_range()
        actual_distance = min(distance, max_possible)
        fuel_needed = actual_distance * self.fuel_consumption_rate
        self.__fuel -= fuel_needed
        self.mileage += actual_distance
        print(f"You have traveled {actual_distance}, your fuel is now {self.__fuel:.2f}.")
        if actual_distance < distance:
            print(f"Warning: Only {actual_distance} traveled due to insufficient fuel.")

    def refuel(self, ammount):
        self.__fuel = self.__fuel + ammount
        print(f"You have refilled {ammount}, your fuel is now {self.__fuel}")

    def get_remaning_range(self):
         return self.__fuel / self.fuel_consumption_rate

    def get_fuel(self):
        return self.__fuel
    def set_fuel(self, fuel):
        self.__fuel = fuel