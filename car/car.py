class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed = max(0, self.__speed - 5)

def test_car():
    print("=== Car Acceleration and Brake Test ===\n")
    my_car = Car(2022, "Toyota")

    print("Accelerating 5 times:")
    for i in range(5):
        my_car.accelerate()
        print(f"  After accelerate #{i+1}: speed = {my_car.get_speed()} km/h")

if __name__ == "__main__":
    test_car()