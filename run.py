import random
import os
import time
from colorama import Fore, Back, Style

TITLE = """
······················································
: ██████╗  █████╗ ████████╗████████╗██╗     ███████╗ :
: ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝ :
: ██████╔╝███████║   ██║      ██║   ██║     █████╗   :
: ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝   :
: ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗ :
: ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝ :
:                                                    :
: ███████╗██╗███████╗██╗     ██████╗                 :
: ██╔════╝██║██╔════╝██║     ██╔══██╗                :
: █████╗  ██║█████╗  ██║     ██║  ██║                :
: ██╔══╝  ██║██╔══╝  ██║     ██║  ██║                :
: ██║     ██║███████╗███████╗██████╔╝                :
: ╚═╝     ╚═╝╚══════╝╚══════╝╚═════╝                 :
······················································
"""

SEA = """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

EXPLOSION = r"""
           _ ._  _ , _ ._        
        (_ ' ( `  )_  .__)       
      ( (  (    )   `)  ) _)     
     (__ (_   (_ . _) _) ,__)    
         `~~`\\ ' . /`~~`        
              ;   ;              
              /  \\              
_____________/_ __\\_____________"""

BOAT = r"""
                 __/___          
           _____/______|         
   _______/_____\_______\_____   
   \              < < <       |  """


class Grid:
    def __init__(self, size):  # Size is given via user input
        # Initialize the grid with water represented by '~'
        self.size = size
        self.grid = [['~' for _ in range(size)] for _ in range(size)]

    def display_grid(self, reveal_ships=False):
        """
        Displays the grid with row and column numbers.
        If reveal_ships is True, shows ship ("S") locations.
        If False, hides ships by showing "~" instead of "S".
        """
        # Print column numbers
        col_numbers = '   ' + ' '.join([str(i + 1) for i in range(self.size)])
        print(col_numbers)

        for index, row in enumerate(self.grid):
            if reveal_ships:
                # Print row number followed by the row contents
                print(
                    f"{index + 1:2} " + Back.BLUE +
                    ' '.join(row) + Style.RESET_ALL
                )
            else:
                # Print row number followed by row contents with ships hidden
                print(
                    f"{index + 1:2} " + Back.BLUE +
                    ' '.join(['~' if cell == 'S' else cell for cell in row]) +
                    Style.RESET_ALL
                )

    def determine_ship_count(self):
        """
        Determines the number of ships based on the grid size.
        Returns the number of ships to place on the grid.
        """
        if self.size <= 4:
            return 3
        elif self.size == 5:
            return 4
        elif self.size == 6:
            return 5
        elif self.size == 7:
            return 6
        else:
            return 7  # For grid sizes 8x8 or larger

    def place_ships(self):
        """
        Randomly adds a number of ships to the grid based on the grid size.
        The number of ships is determined by the determine_ship_count method.
        """
        ship_count = self.determine_ship_count()
        for _ in range(ship_count):  # Loops for the ship_count amount of times
            while True:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                if self.grid[row][col] == "~":  # Checks if the cell is empty
                    self.grid[row][col] = "S"  # Adds a ship ("S")
                    break

    def check_for_ship(self, row, col):
        """
        Checks if there is a ship at the given (row, col) position on the
        internal grid.
        Returns True if there is a ship ('S'), otherwise False.
        """
        return self.grid[row][col] == "S"

    def update_grid(self, row, col, hit):
        """
        Updates the grid if a ship is hit or missed.
        Uses 'X' for hit and 'O' for miss.
        """
        if hit:
            self.grid[row][col] = 'X'
        else:
            self.grid[row][col] = 'O'


def validate_data(value):
    """
    Validates that the grid size is an integer between 3 and 8.
    Raises ValueError with a message if the input is invalid.
    """
    try:
        value = int(value)
    except ValueError:
        raise ValueError(
            f'Invalid input: {value}.\nPlease enter a valid integer.'
                )
    if value > 8:
        raise ValueError(
                f'The maximum grid size is 8 x 8.\n'
                + f'Please provide a number from 3 to 8'
            )
    elif value < 3:
        raise ValueError(
                f'The mininum grid size is 3 x 3.\n'
                + f'Please provide a number from 3 to 8'
            )
    else:
        return value


def get_user_input(grid_size):
    """
    Prompts the user to input the row and column separately.
    Validates the input to ensure it is within the grid bounds.
    Returns the corresponding row and column indices.
    """
    while True:
        try:
            # Prompt for row input
            row = int(input(f"Enter the row number (1 to {grid_size}): ")) - 1
            if row < 0 or row >= grid_size:
                print(
                    Fore.YELLOW +
                    f"Invalid row." +
                    f"Please enter a number between 1 and {grid_size}."
                    + Style.RESET_ALL
                )
                continue

            # Prompt for column input
            col = int(input(
                    f"Enter the column number"
                    + f"(1 to {grid_size}): ")) - 1
            if col < 0 or col >= grid_size:
                print(
                    Fore.YELLOW + f"Invalid column." +
                    f"Please enter a number between 1 and {grid_size}."
                    + Style.RESET_ALL
                )
                continue

            return row, col

        except ValueError:
            print(Fore.YELLOW + "Invalid input. Please enter valid numbers.")


def main():
    while True:
        os.system('cls||clear')
        print(Fore.LIGHTBLUE_EX + TITLE + Style.RESET_ALL)

        # User defines name for greeting
        user_name = input("\nPlease enter your name: \n")

        # Validate grid size input for type and size
        while True:
            grid_size = input(
                f"\nHi {user_name}, enter grid size" +
                "(3 to 8 for a 3x3 to 8x8 grid): \n"
            )
            try:
                grid_size = validate_data(grid_size)
                break  # Exit loop if input is valid
            except ValueError as e:
                print(e)

        # Create Grid class
        player_grid = Grid(grid_size)
        computer_grid = Grid(grid_size)

        # Place ship in grids
        player_grid.place_ships()
        computer_grid.place_ships()

        # Display the player's grid with ships revealed
        print(f"\n{user_name}'s Grid:")
        player_grid.display_grid(reveal_ships=True)

        # Display the computer's grid with ships hidden
        print("\nComputer's Grid:")
        computer_grid.display_grid(reveal_ships=False)

        # Start the game loop
        while True:
            # Player's turn to chooses coordinate to "shoot"
            print(f"\n{user_name}'s turn:")
            row, col = get_user_input(grid_size)

            # Check if the chosen coordinate has already been selected
            if computer_grid.grid[row][col] in ['X', 'O']:
                print(
                    Fore.YELLOW +
                    "You have already chosen this coordinate." +
                    "Please try again.")
                continue

            os.system('cls||clear')

            # Check for a hit and update the grid accordingly
            hit = computer_grid.check_for_ship(row, col)
            computer_grid.update_grid(row, col, hit)

            if hit:
                print(Fore.GREEN + "\nHit!" + Style.RESET_ALL)
                print(Fore.RED + EXPLOSION + Style.RESET_ALL)
                print(Back.BLUE + SEA + Style.RESET_ALL)
            else:
                print(Fore.RED + "\nMiss!" + Style.RESET_ALL)
                print(BOAT)
                print(Back.BLUE + SEA + Style.RESET_ALL)

            time.sleep(1.5)  # Wait on ASCII art

            os.system('cls||clear')  # Clear terminal after hit or miss

            # Display the updated computer grid (hidden ships)
            print("\nComputer's Grid:")
            computer_grid.display_grid(reveal_ships=False)

            # Check for victory condition (all ships hit)
            if all(cell != 'S' for row in computer_grid.grid for cell in row):
                print(
                    f"\nCongratulations {user_name}," +
                    "you've sunk all the computer's ships!"
                )
                break

            # Computer's turn
            print("\nComputer's turn:")
            while True:
                row = random.randint(0, grid_size - 1)
                col = random.randint(0, grid_size - 1)
                if player_grid.grid[row][col] not in ['X', 'O']:
                    break

            hit = player_grid.check_for_ship(row, col)
            player_grid.update_grid(row, col, hit)

            if hit:
                print(
                    f"\nThe computer hit your ship at ({row + 1}, {col + 1})!"
                )
            else:
                print("\nThe computer missed.")

            # Display the updated player's grid
            print("\nYour Grid:")
            player_grid.display_grid(reveal_ships=True)

            # Check for defeat condition (all ships hit)
            if all(cell != 'S' for row in player_grid.grid for cell in row):
                print(
                    Back.RED +
                    "\nThe computer has sunk all your ships! Game over."
                    + Style.RESET_ALL
                )
                break

        # Ask if the user wants to play again
        play_again = input(
                    "\nDo you want to play again? (Y/N): "
                    ).strip().upper()
        if play_again != "Y":
            print("\nThanks for playing! Goodbye!")
            break


main()
