import random

# The game will be played in a 3x3 grid
ROWS = 3
COLS = 3

# instead of using array of array just use a dictionary

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


class Game:
    """
    Hold state of the tic-tac-toe game.

    Attributes:
         grid (array[array[badge]]) :
         players (array[Player]):
         currentPlayer (Player):
         gridKey (dict) :
         movesRemaining (int): Number of moves remaining before the grid is full.
    """

    def __init__(self):
        self.grid = [[' ' for i in range(COLS)] for j in range(ROWS)]
        self.players = self.startGame()
        self.currentPlayer = random.choice(self.players)
        self.gridKey = {"a": 0, "b": 1, "c": 2}
        self.movesRemaining = ROWS*COLS

    def print_grid(self):
        """Print the current game grid including the location of past players' moves."""
        print(f'    0   1   2 ')
        print(f'    .   .   . ')
        print(f'a . {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} ')
        print(f'   ---|---|---')
        print(f'b . {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} ')
        print(f'   ---|---|---')
        print(f'c . {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} ')

    def startGame(self):
        """Start the game by printing prompts for user to input player names,
        prints the empty game board grid and instructions."""
        player1 = Player(input("Who is the first player? "), 'X')
        player2 = Player(input("Who is the second player? "), 'O')

        print("-----------------------------------------------------------------------------------------------")
        print(f"Welcome to the game {player1.name} and {player2.name}, good luck!")
        print(f"{player1.name} will be {player1.badge}s and {player2.name} will be {player2.badge}s.")
        print("To make a move enter a letter followed by a number to indicate the square you want to play in.")
        print("-----------------------------------------------------------------------------------------------")

        self.print_grid()
        return [player1, player2]

    def __is_valid_turn(self, letter, number):
        """Determine if a user's input results in a valid turn.
        Args:
            letter (str):
            number (str):
        """
        if letter not in ('a', 'b', 'c'):
            return False
        if number not in ('0', '1', '2'):
            return False
        r = self.gridKey[letter]
        c = int(number)
        if (self.grid[r][c] == 'X') | (self.grid[r][c] == 'O'):
            return False

        return True

    def take_turn(self, try_again=False):
        """

        :param try_again:
        :return:
        """
        print(' ')
        if try_again:
            move = input(f'That is not a valid move {self.currentPlayer.name}, try again.')
        else:
            move = input(f"Make your move  {self.currentPlayer.name}, (enter letter then number, example a1): ")

        letter = move[0]
        number = move[1]

        if self.__is_valid_turn(letter, number):
            self.__update_grid(letter,number)
            self.print_grid()
            self.__switch_player()
            self.movesRemaining = self.movesRemaining - 1
            self.check_state()
        else:
            print()
            self.take_turn(True)

    def __switch_player(self):
        """Switch from one player as current player to the other."""
        if self.currentPlayer == self.players[0]:
            self.currentPlayer = self.players[1]
        else:
            self.currentPlayer = self.players[0]

    def __declare_game_over(self, msg):
        """Print message declaring game's end and set state of gameOver.
        Args:
            msg (str): Specific message to print following Game Over announcement.
        """
        print(f'Game Over! {msg}')

    def __update_grid(self, letter, number):
        """Update game grid with most recent valid move.
        Args:
            letter (str): The character denoting the row of the player's move.
            number (str): The character representation of the number denoting the column
                          of the player's move.
        """
        r = self.gridKey[letter]
        c = int(number)
        self.grid[r][c] = self.currentPlayer.badge

    def check_state(self):
        """Check if the game has ended after last played turn due to win or tie."""

        # check if the game has ended in a tie
        if self.movesRemaining == 0:
            return self.__declare_game_over('It\'s a Tie! No more moves remain.')

        # check for all the horizontal wins
        for r in range(ROWS):
            if self.grid[r][0] == ' ':
                continue
            if all([x == self.grid[r][0] for x in [self.grid[r][1], self.grid[r][2]]]):
                print(all([x == self.grid[r][0] for x in [self.grid[r][1], self.grid[r][2]]]))
                return self.__declare_game_over(f'The winner is {self.currentPlayer.name}!')

        # check for all the vertical wins
        for c in range(COLS):
            if self.grid[0][c] == ' ':
                continue
            if all([x == self.grid[0][c] for x in [self.grid[1][c], self.grid[2][c]]]):
                return self.__declare_game_over(f'The winner is {self.currentPlayer.name}!')

        # check for the diagonal wins
        if all([x == self.grid[0][0] for x in [self.grid[1][1], self.grid[2][2]]]) & (self.grid[0][0] != ' '):
            return self.__declare_game_over(f'The winner is {self.currentPlayer.name}!')

        if all([x == self.grid[0][2] for x in [self.grid[1][1], self.grid[2][0]]]) & (self.grid[0][2] != ' '):
            return self.__declare_game_over(f'The winner is {self.currentPlayer.name}!')


if __name__ == '__main__':

    aGame = Game()
    while aGame.movesRemaining > 0:
        aGame.take_turn()