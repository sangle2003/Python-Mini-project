class MobilePhone:
    def __init__(self, brand, model, battery_percentage):
        self.__brand = brand
        self.__model = model
        self.__battery_percentage = battery_percentage

    # Getter
    def get_battery_percentage(self):
        return self.__battery_percentage

    # Setter
    def set_battery_percentage(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Battery percentage must be between 0 and 100.")

    # Charge phone
    def charge_phone(self, percentage):
        new_battery = self.__battery_percentage + percentage

        if new_battery > 100:
            self.__battery_percentage = 100
        else:
            self.__battery_percentage = new_battery

        print("Phone charged successfully.")

    # Use phone
    def use_phone(self, percentage):
        if percentage <= self.__battery_percentage:
            self.__battery_percentage -= percentage
            print("Phone used successfully.")
        else:
            print("Battery is too low.")

    # Display battery status
    def display_battery_status(self):
        print("Brand:", self.__brand)
        print("Model:", self.__model)
        print("Battery:", self.__battery_percentage, "%")


# Object
phone = MobilePhone("Samsung", "S24", 60)

phone.display_battery_status()

phone.use_phone(20)
print("Battery after use:", phone.get_battery_percentage(), "%")

phone.charge_phone(30)
print("Battery after charging:", phone.get_battery_percentage(), "%")

# Using setter
phone.set_battery_percentage(90)
print("Battery after setter:", phone.get_battery_percentage(), "%")