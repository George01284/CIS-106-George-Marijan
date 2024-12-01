class Car:
    def __init__(vehicle, make, model, sticker_price):
        vehicle.make = make
        vehicle.model = model
        vehicle.sticker_price = sticker_price
    
    def get_discount_price(vehicle):
        return vehicle.sticker_price * 0.9

    def display_info(vehicle):
        info = (f"Make: {vehicle.make}, Model: {vehicle.model}, Sticker Price: ${vehicle.sticker_price:.2f}, "
                f"Discount Price: ${vehicle.get_discount_price():.2f}")
        print(info)

class SportCar(Car):
    def __init__(vehicle, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        vehicle.options = {
            'SportWheels': 1000.00,
            'SportEngine': 3000.00,
            'SportInterior': 2000.00
        }
        vehicle.selected_options = {
            'SportWheels': 'N',
            'SportEngine': 'N',
            'SportInterior': 'N'
        }
    
    def set_option(vehicle, option, value):
        if option in vehicle.selected_options:
            vehicle.selected_options[option] = value
    
    def get_updated_price(vehicle):
        updated_price = vehicle.get_discount_price()
        for option, value in vehicle.selected_options.items():
            if value == 'Y':
                updated_price += vehicle.options[option]
        return updated_price

    def display_info(vehicle):
        super().display_info()
        print(f"Updated Price with Options: ${vehicle.get_updated_price():.2f}")

car1 = Car("Toyota", "Camry", 24000)
car2 = Car("Honda", "Civic", 20000)

sportcar1 = SportCar("Ferrari", "488", 280000)
sportcar2 = SportCar("Porsche", "911", 150000)

sportcar1.set_option('SportWheels', 'Y')
sportcar1.set_option('SportEngine', 'Y')
sportcar2.set_option('SportInterior', 'Y')

print(f"Car 1 Info:")
car1.display_info()
print()

print(f"Car 2 Info:")
car2.display_info()
print()

print(f"SportCar 1 Info:")
sportcar1.display_info()
print()

print(f"SportCar 2 Info:")
sportcar2.display_info()
