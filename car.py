HORIZONTAL = 1
VERTICAL = 0


class Car:
    """
    a car that can move in 1 line on a board
    :var length - the length of the car
    :var orientation - represents the way the car is facing (horizontal 1,
    or vertical 0).
    :var name - the name of the car
    :var location - tuple that represents the location of the car in the board
    """
    length = None
    orient = None
    name = None
    location = []

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        self.name = name
        self.length = length
        self.location = tuple(location)
        self.orient = orientation

    def car_coordinates(self):
        """
        calculate the car possition baed on location and length
        :return: A list of coordinates the car is in
        """
        if self.orient == HORIZONTAL:
            return [(self.location[0], x + self.location[1])
                    for x in range(self.length)]
        if self.orient == VERTICAL:
            return [(y + self.location[0], self.location[1])
                    for y in range(self.length)]

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
         permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        possible_moves = {}
        if self.orient == HORIZONTAL:
            possible_moves["l"] = "cause the car to move left"
            possible_moves["r"] = "cause the car to move right"
        else:
            possible_moves["u"] = "cause the car to move up"
            possible_moves["d"] = "cause the car to move down"
        return possible_moves

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        if movekey in self.possible_moves().keys():
            if movekey == "d":
                return [(self.location[0] + self.length, self.location[1])]
            elif movekey == "u":
                return [(self.location[0] - 1, self.location[1])]
            elif movekey == "l":
                return [(self.location[0], self.location[1] - 1)]
            elif movekey == "r":
                return [(self.location[0], self.location[1] + self.length)]
        return []

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        if movekey in self.possible_moves().keys():
            if movekey == "d":
                self.location = (self.location[0] + 1, self.location[1])
                return True
            elif movekey == "u":
                self.location = (self.location[0] - 1, self.location[1])
                return True
            elif movekey == "l":
                self.location = (self.location[0], self.location[1] - 1)
                return True
            elif movekey == "r":
                self.location = (self.location[0], self.location[1] + 1)
                return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name
