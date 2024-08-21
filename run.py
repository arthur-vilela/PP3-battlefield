class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [['-' for _ in range(size)] for _ in range(size)]
        print(self.grid)



def main():
    user_name = input("Please enter your name: \n")
    grid_size = int(input(f"Hi {user_name}, enter grid size (e.g., 5 for a 5x5 grid): "))

    player_grid = Grid(grid_size) #create Grid class
    computer_grid = Grid(grid_size)

    # Display the grids
    print(f"\n{user_name}'s Grid: \n{player_grid.grid}")
    print(f"\nComputer's Grid: \n {computer_grid.grid}")


main()