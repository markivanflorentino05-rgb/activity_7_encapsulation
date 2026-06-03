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

    try:
        user_age = int(input("Enter pet's age: "))
    except ValueError:
        print("Invalid age. Setting age to 0.")
        user_age = 0

    my_pet.set_name(user_name)
    my_pet.set_animal_type(user_type)
    my_pet.set_age(user_age)

    print("\n--- Your Pet Details ---")
    print(f"Name: {my_pet.get_name()}")
    print(f"Animal Type: {my_pet.get_animal_type()}")
    print(f"Age: {my_pet.get_age()} years")

if __name__ == "__main__":
    test_pet()