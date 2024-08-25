import random

class Grid:
    def __init__(self, size): #size is given via user input
        self.size = size
        self.grid = [['-' for _ in range(size)] for _ in range(size)]


    def display_grid(self, reveal_ships=False):
        """
        Displays the grid. If reveal_ships is True, shows ship ("S") locations.
        If false, substitute "S" for "-"
        """
        for row in self.grid:
            if reveal_ships:
                print(' '.join(row))
            else:
                print(' '.join(['-' if cell == 'S' else cell for cell in row]))
    

    def place_ships(self):
        """
        Randomly adds 1 ship to both grids
        """
        while True: 
            row = random.randint(0, self.size -1)
            col = random.randint(0, self.size -1)
            if self.grid[row][col] == "-": # Checks if hte cell is empty ("-")
                self.grid[row][col] = "S" # Adds a ship ("S")
                break
    
    def check_for_ship(self, row, col):
        """
        Checks if there is a ship at the given (row, col) position on the internal grid.
        Returns True if there is a ship ('S'), otherwise False.
        """
        return self.grid[row][col] == "S"

def validate_data(value):
    """
    Validates that the grid size is an integer between 3 and 8.
    Raises ValueError with a message if the input is invalid.
    """
    try:
        value = int(value)
    except ValueError:
        raise ValueError(f'Invalid input: {value}. Please enter a valid integer.')
    if value > 8:
        raise ValueError(
                f'The maximum grid size is 8 x 8. Please provide a number from 3 to 8'
            )
    elif value < 3:
            raise ValueError(
                f'The mininum grid size is 3 x 3. Please provide a number from 3 to 8'
            )
    else:
        return value 


def get_user_input(grid_size):
    """
    Prompts the user to input the row and column separately.
    Validates the input and returns the corresponding row and column indices.
    """
    while True:
        try:
            # Prompt for row input
            row = int(input(f"Enter the row number (1 to {grid_size}): ")) - 1
            if row < 0 or row >= grid_size:
                print(f"Invalid row. Please enter a number between 1 and {grid_size}.")
                continue

            # Prompt for column input
            col = int(input(f"Enter the column number (1 to {grid_size}): ")) - 1
            if col < 0 or col >= grid_size:
                print(f"Invalid column. Please enter a number between 1 and {grid_size}.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter valid numbers.")


def main():
    # User defines name for greeting
    user_name = input("Please enter your name: \n")
    
    # Validate grid size input for type and size
    while True:
        grid_size = input(f"Hi {user_name}, enter grid size (3 to 8 for a 3x3 to 8x8 grid): \n")
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

    # Display the grids
    print(f"\n{user_name}'s Grid:")
    player_grid.display_grid(reveal_ships=True)
    
    print("\nComputer's Grid:")
    computer_grid.display_grid(reveal_ships=False)

    # User chooses coordinate to "shoot"
    while True:
        row, col = get_user_input(grid_size)
        
        if computer_grid.check_for_ship(row, col): # checking the spot on the grid
            print("Hit!")
        else:
            print("Miss!")
        break


main()