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

    def turn_on(self):
        self.__on = True
    def turn_off(self):
        self.__on = False

    def display(self):
        state = "on" if self.__on else "off"
        speed_names = {Fan.SLOW: "SLOW", Fan.MEDIUM: "MEDIUM", Fan.FAST: "FAST"}
        speed_str = speed_names.get(self.__speed, "UNKNOWN")
        return (f"Fan speed={speed_str} ({self.__speed}), radius={self.__radius}, "
                f"color={self.__color}, state={state}")