class Pet:
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Warning: Age set to 0 (negative not allowed)")
            self.__age = 0

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def test_pet():
    print("=== Pet Information Program ===\n")
    my_pet = Pet()

    user_name = input("Enter pet's name: ")
    user_type = input("Enter pet's animal type (e.g., Dog, Cat, Bird): ")
    user_age = int(input("Enter pet's age: "))

    print("Input received")

if __name__ == "__main__":
    test_pet()