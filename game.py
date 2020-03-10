import numpy as np
import random

# The game will be played in a 3x3 grid
ROWS = 3
COLS = ROWS


class Player:
    """
    Hold the properties of each player.

    Attributes:
        name (str): A player's name, as input by the user.
        badge (str): A player's badge, either X or O. Assigned based on order of input.
    """

    def __init__(self, name, badge):
        self.name = name
        self.badge = badge


class Grid:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.ord_a = 97  # integer corresponding to the unicode character 'a'
        self.row_indices = [chr(i) for i in range(self.ord_a, self.ord_a + rows)]
        self.col_indices = [str(i) for i in range(1, cols + 1)]
        self.grid_keys = list(zip(list(np.repeat([chr(i) for i in range(self.ord_a, self.ord_a + rows)], cols)),
                                  [str(i) for i in range(1, cols + 1)] * rows))
        self.grid = {key: ' ' for key in self.grid_keys}

    def print_grid(self):
        """Print the current game grid including the location of past players' moves."""
        print(f"    1   2   3 ")
        print(f"    .   .   . ")
        print(f"a . {self.grid['a', '1']} | {self.grid['a', '2']} | {self.grid['a', '3']} ")
        print(f"   ---|---|---")
        print(f"b . {self.grid['b', '1']} | {self.grid['b', '2']} | {self.grid['b', '3']} ")
        print(f"   ---|---|---")
        print(f"c . {self.grid['c', '1']} | {self.grid['c', '2']} | {self.grid['c', '3']} ")


class Game:
    """
    Hold state of the tic-tac-toe game, the grid, and the players.

    Attributes:
         grid dict{k: Badge}:
         players (array[Player]):
         current_player (Player):
         gridKey (dict) :
         movesRemaining (int): Number of moves remaining before the grid is full.
    """

    def __init__(self):
        self.grid = Grid(ROWS, COLS)
        self.players = []
        self.current_player = None
        self.game_over = False

    def start_game(self):
        """Start the game by printing prompts for user to input player names,
        prints the empty game board grid and instructions."""
        player1 = Player(input("Who is the first player? "), 'X')
        player2 = Player(input("Who is the second player? "), 'O')

        self.players = [player1, player2]
        self.current_player = random.choice(self.players)

        print("-----------------------------------------------------------------------------------------------")
        print(f"Welcome to the game {player1.name} and {player2.name}, good luck!")
        print(f"{player1.name} will be {player1.badge}s and {player2.name} will be {player2.badge}s.")
        print("To make a move enter a letter followed by a number to indicate the square you want to play in.")
        print("-----------------------------------------------------------------------------------------------")

        self.grid.print_grid()

    def __is_valid_player(self, player):


    def __is_valid_turn(self, move):
        """
        Determine ig a user's input results in a valid turn.
        :param move:
        :return:
        """
        # the user entered nothing
        if move == '':
            return False

        # the letter input is not one of the row indices
        if move[0] not in self.grid.row_indices:
            return False

        # the number input is not one of the column indices
        if move[1] not in self.grid.col_indices:
            return False

        # the location entered has already been marked in a previous turn
        if (self.grid.grid[(move[0], move[1])] == 'X') | (self.grid.grid[(move[0], move[1])] == 'O'):
            return False

        return True

    def take_turn(self, try_again=False):
        """

        :param try_again:
        :return:
        """
        if try_again:
            move = input(f'Invalid move {self.current_player.name}. Try again :')
        else:
            move = input(f"Make your move {self.current_player.name} : ")

        if self.__is_valid_turn(move):
            self.grid.grid[(move[0], move[1])] = self.current_player.badge
            self.grid.print_grid()
            self.__check_state()
            self.__switch_player()
        else:
            self.take_turn(try_again=True)

    def __switch_player(self):
        """
        Switch from one player as current player to the other.
        :return: None
        """
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def __check_for_win(self, ind_keys):
        if all([self.grid.grid[(x, y)] == self.grid.grid[ind_keys[0]] for (x, y) in ind_keys]) \
                and self.grid.grid[ind_keys[0]] != ' ':
            print(f'Game Over! The winner is {self.current_player.name}!')
            self.game_over = True

    def __check_state(self):

        # check for tie
        if len([badge for badge in self.grid.grid.values() if badge == ' ']) == 0:
            print(f'Game Over! No moves remain, it is a tie!')
            self.game_over = True

        # check for a horizontal win
        for ind in self.grid.row_indices:
            self.__check_for_win(list(zip([ind]*self.grid.cols, self.grid.col_indices)))

        # check for a vertical win
        for ind in self.grid.col_indices:
            self.__check_for_win(list(zip(self.grid.row_indices, [ind]*self.grid.rows)))

        # check for a left to right diagonal win
        self.__check_for_win(list(zip(self.grid.row_indices, self.grid.col_indices)))

        # check for a right to left diagonal win
        self.__check_for_win(list(zip(self.grid.row_indices, self.grid.col_indices.__reversed__())))


if __name__ == '__main__':

    aGame = Game()
    aGame.start_game()

    # while some spots on the game board are blank, keep taking turns
    while not aGame.game_over:
        aGame.take_turn()
