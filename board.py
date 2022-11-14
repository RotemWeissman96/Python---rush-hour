HORIZONTAL = 1
VERTICAL = 0


class Board:
    """
    board for rush hour game, contain car which can move around and an exit
    """
    car_dic = {}
    length = None
    high = None
    target = None

    def __init__(self, high=7, length=7, target=(3, 7)):
        """
        create a new board type object. does not require any parameters but
        can change size by excepting the following
        :param high: the height of the board, 7 by default
        :param length: the length of the board, 7 by default
        :param target: the target to win the game, (3, 7) by default
        """
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.high = high
        self.length = length
        self.target = target
        self.car_dic = {}

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        middle_list = [" " + "_" * (self.length*2 + 1)]
        for y in range(self.high - 1):  # create the board itself
            if y == self.target[0] - 1:
                middle_list.append("|" + " ." * (self.length - 1) + " |___")
            elif y == self.target[0]:
                middle_list.append("|" + " ." * (self.length - 1) + "  ___")
            else:
                middle_list.append("|" + " ." * (self.length-1) + " |")
        middle_list.append("|" + "_" * (self.length*2 - 1) + "|")
        for car in self.car_dic.values():  # adds all the cars
            for i in car.car_coordinates():
                new = middle_list[1 + i[0]][:1 + i[1]*2] + car.get_name() + \
                      middle_list[1 + i[0]][2 + i[1]*2:]
                middle_list[1 + i[0]] = new
        return str(middle_list).replace(",", "\n").replace("[", "").replace(
            "]", "").replace("'", "")

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        cell_list = []
        for x in range(self.length):
            for y in range(self.high):
                cell_list.append((y, x))
        cell_list.append(self.target)
        return cell_list

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,move_key,description)
                 representing legal moves
        """
        valid_moves = []
        for car in self.car_dic.values():  # check every car
            for move in car.possible_moves().items():
                # check every possible move if it is open and in the board
                if move[0] == "u":
                    destin = car.movement_requirements("u")[0]
                    if destin[0] < 0 or self.cell_content(destin):
                        continue
                elif move[0] == "l":
                    destin = car.movement_requirements("l")[0]
                    if destin[1] < 0 or self.cell_content(destin):
                        continue
                elif move[0] == "d":
                    destin = car.movement_requirements("d")[0]
                    if destin[0] > self.high - 1 \
                            or self.cell_content(destin):
                        continue
                elif move[0] == "r":
                    destin = car.movement_requirements("r")[0]
                    if destin == self.target_location():
                        valid_moves.append((car.get_name(), move[0],
                                            "right, win!!"))
                        continue
                    if destin[1] > self.length - 1 \
                            or self.cell_content(destin):
                        continue
                valid_moves.append((car.get_name(), move[0], move[1]))
        return valid_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return self.target

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car in self.car_dic.values():
            if coordinate in car.car_coordinates():
                return car.get_name()

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        if car.get_name() in self.car_dic:
            return False
        for i in car.car_coordinates():
            if self.cell_content(i):
                return False
            if i not in self.cell_list():
                return False
        self.car_dic[car.get_name()] = car
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for possible_move in self.possible_moves():
            if name == possible_move[0] and movekey == possible_move[1]:
                self.car_dic[name].move(movekey)
                return True
        return False
