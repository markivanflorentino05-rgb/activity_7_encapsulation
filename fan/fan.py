class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self):
        return self.__speed
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color
    def is_on(self):
        return self.__on

    def set_speed(self, speed):
        if speed in (Fan.SLOW, Fan.MEDIUM, Fan.FAST):
            self.__speed = speed
        else:
            print("Error: Speed must be Fan.SLOW, Fan.MEDIUM, or Fan.FAST")

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Error: Radius must be positive")

    def set_color(self, color):
        if isinstance(color, str) and color.strip():
            self.__color = color
        else:
            print("Error: Color must be a non-empty string")