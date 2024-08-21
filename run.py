def main():
    user_name = input("Please enter your name: \n")
    grid_size = input(f"Hi {user_name}, enter grid size (e.g., 5 for a 5x5 grid): ")

    player_grid = Grid(grid_size) #create Grid class
    computer_grid = Grid(grid_size)

    # Display the grids
    print(f"\n{user_name}'s Grid:")
    
    print("\nComputer's Grid:")

main()