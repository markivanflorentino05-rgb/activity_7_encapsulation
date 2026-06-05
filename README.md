# Encapsulation Demo: Fan, Car, and Pet Classes

This repository contains three Python programs that demonstrate **encapsulation** in object-oriented programming. Each class hides its internal data using private attributes and provides controlled access through public getter and setter methods.

## 📁 Folder Structure
activity_7_encapsulation/
├── README.md
├── fan
│ └── fan.py # Fan class with test program
├── car
│ └── car.py # Car class with test program
└── pet
└── pet.py # Pet class with test program

## 🚀 How to Run

### Prerequisites
- Python 3.6 or higher (no external libraries needed)

### Run Individual Programs
# Fan class test
fan/fan.py

# Car class test
car/car.py

# Pet class test (interactive – you enter pet details)
pet/pet.py

🔒 What is Encapsulation?
Encapsulation is an OOP principle that bundles data (attributes) and methods that operate on that data into a single unit (class), while restricting direct access to some of the object's internal components.

In Python:

Private attributes are prefixed with __ (double underscore), e.g., __speed, __name.

They cannot be accessed directly from outside the class.

Public getter methods (e.g., get_speed()) allow reading the value.

Public setter methods (e.g., set_speed()) allow modifying the value, often with validation.

📚 Program Descriptions
1. Fan Class (fan/fan.py)
Purpose: Model a ceiling fan with speed, radius, color, and on/off state.

Key Features:

Class constants: SLOW = 1, MEDIUM = 2, FAST = 3

Private attributes: __speed, __radius, __color, __on

Getters: get_speed(), get_radius(), get_color(), is_on()

Setters with validation: set_speed(), set_radius(), set_color()

Behaviour methods: turn_on(), turn_off()

display() method returns a formatted string.

Test Output:
Fan 1 details: Fan speed=FAST (3), radius=10.0, color=yellow, state=on
Fan 2 details: Fan speed=MEDIUM (2), radius=5.0, color=blue, state=off

--- Fan 1 via getters ---
Speed: 3
Radius: 10.0
Color: yellow
On: True

2. Car Class (car/car.py)
Purpose: Simulate a car's speed with accelerate and brake actions.

Key Features:

Private attributes: __year_model, __make, __speed

Getters: get_year_model(), get_make(), get_speed()

Behaviour methods: accelerate() (+5), brake() (-5, never below 0)

Test Output:
Accelerating 5 times:
  After accelerate #1: speed = 5 km/h
  After accelerate #2: speed = 10 km/h
  After accelerate #3: speed = 15 km/h
  After accelerate #4: speed = 20 km/h
  After accelerate #5: speed = 25 km/h

Braking 5 times:
  After brake #1: speed = 20 km/h
  After brake #2: speed = 15 km/h
  After brake #3: speed = 10 km/h
  After brake #4: speed = 5 km/h
  After brake #5: speed = 0 km/h

  3. Pet Class (pet_class/pet.py)
Purpose: Store and retrieve pet information with age validation.

Key Features:

Private attributes: __name, __animal_type, __age

Getters: get_name(), get_animal_type(), get_age()

Setters: set_name(), set_animal_type(), set_age() (validates age ≥ 0)

Interactive user input in test program.

Sample Interaction:
Enter pet's name: Luna
Enter pet's animal type (e.g., Dog, Cat, Bird): Cat
Enter pet's age: 2

--- Your Pet Details ---
Name: Luna
Animal Type: Cat
Age: 2 years

🎯 Learning Outcomes
By studying this code, you will understand:

How to declare private attributes using __ in Python

How to write getter and setter methods

Why validation in setters protects data integrity

The difference between direct attribute access and method-based access

How to structure a class with both data and behaviour

📜 License
This project is for educational purposes. Feel free to use, modify, and share.
