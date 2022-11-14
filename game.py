from board import Board
from car import Car
import helper
import sys


HIGH = 7
LENGTH = 7
VALID_NAMES = ["R", "G", "W", "O", "B", "Y"]
VALID_LEN = [2, 3, 4]
VALID_MOVES = ["r", "d", "u", "l"]
VALID_ORIENT = [1, 0]
TARGET = (3, 7)


class Game:
    """
    rush hour game, get user input in order to move cars around the board
    until a car is in the target
    """
    board = None

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        moves_list = []
        for i in self.board.possible_moves():
            moves_list.append([i[0], i[1]])
        while True:
            user_move = input("\n Enter Car name and way to move")
            if user_move == "!":
                return False
            elif len(user_move) != 3 or "," == user_move[0]\
                    or "," == user_move[2] or "," != user_move[1]:
                print("The input format is - car_name,move")
            else:
                car_to_move, move = user_move.split(",")
                if [car_to_move, move] not in moves_list:
                    print("Not a possible move")
                else:
                    break
        self.board.move_car(car_to_move, move)
        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while not self.board.cell_content(TARGET):
            print("\n" + str(self.board))
            if not self.__single_turn():
                return None
        # print("You won!!!")


def check_valid_car(car_values):
    """
    check the validity of the car
    :param car_values:
    :return:
    """
    if car_values[0] not in VALID_NAMES:
        return False
    if car_values[1][0] not in VALID_LEN:
        return False
    if car_values[1][2] not in VALID_ORIENT:
        return False
    return True


def add_cars_to_board(board, car_config):
    """
    adds only valid cars from a car dic to the board, uses the check calid car
    method
    :param board: the board to enter
    :param car_config: a dictionary of cars received from the json file
    :return: the board after adding all valid cars
    """
    for i in car_config.items():
        if check_valid_car(i):  # if the car is valid, add to board
            board.add_car(Car(i[0], i[1][0], i[1][1], i[1][2]))
    return board


if __name__ == "__main__":
    car_config = helper.load_json(sys.argv[1])
    board = Board()
    add_cars_to_board(board, car_config)
    game = Game(board)
    game.play()
