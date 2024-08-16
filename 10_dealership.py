class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.brand} {self.model} car has been sold")
        else:
            print(f"{self.brand} {self.model} car is not available")

    def check_availability(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    

class Customer:
    def __init__(self, name):
        self.name = name
        self.cars_purchased = []

    def buy_car(self, car):
        if car.check_availability():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"We are sorry, {self.brand} {self.model} car is not available")
    
    def inquire_car(self, car):
        availability = "Avaialble" if car.check_availability() else "not available"
        print(f"{car.brand} {car.model} is {availability} and its price is {car.price}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"{car.brand} {car.model} car has been added in inventory")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} has been registered in dealership")

    def show_available_cars(self):
        print(f"Cars availables in dealership")
        for car in self.inventory:
            if car.check_availability():
                print(f"- {car.brand} {car.model} by {car.get_price()}")


car1 = Car(brand='Toyota', model='4Runner', price=70000)
car2 = Car(brand='Jeep', model='Wrangler', price=80000)
car3 = Car(brand='Audi', model='Q8', price=50000)

customer1 = Customer(name="Jason")

dealership = Dealership()
dealership.add_car(car=car1)
dealership.add_car(car=car2)
dealership.add_car(car=car3)
dealership.register_customer(customer=customer1)

dealership.show_available_cars()

customer1.inquire_car(car=car1)

customer1.buy_car(car=car1)

dealership.show_available_cars()


