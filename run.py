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


def main():
    # User defines grid size and name for greeting
    user_name = input("Please enter your name: \n")
    grid_size = int(input(f"Hi {user_name}, enter grid size (e.g., 5 for a 5x5 grid): \n"))

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


main()