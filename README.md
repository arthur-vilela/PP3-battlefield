# Battlefield

The Battleship game is a classic two-player strategy game where the objective is to sink all of the opponent's ships. In this Python implementation, the player competes against the computer.

![flowchart of the game logic](assets/docs/flowchart.pn)
## Table of contents
1. <a href="#ux-design">UX Design</a> 
2. <a href="#features">Features</a>
3. <a href="#game-flow">Game Flow</a>
4. <a href="#technologies-used">Technologies used</a>
5. <a href="#testing">Testing</a>
6. <a href="#bugs">Bugs</a>
7. <a href="#validator-testing">Validator testing</a>
8. <a href="#deployment">Deployment</a>
9. <a href="#credits">Credits</a>
10. <a href="#acknowledgements">Acknowledgements</a>

## UX Design
## Features
## Game Flow

Game Flow
The Battleship game is a classic two-player strategy game where the objective is to sink all of the opponent's ships. In this Python implementation, the player competes against the computer. The game proceeds through the following steps:

> ### 1. Introduction and Setup

- The game begins with a welcome screen displaying the title of the game.

- The player is prompted to enter their name, which will be used throughout the game.

- The player is then asked to choose the size of the grid on which the game will be played. The grid size can range from 3x3 to 8x8.

- Based on the selected grid size, a certain number of ships are placed randomly on both the player’s and the computer’s grids.

> ### 2. Displaying the Grids

- The player's grid is displayed, revealing the locations of their ships (S).

- The computer's grid is also displayed, but with the ships hidden, represented by ~ (water).

>### 3. Gameplay Loop

- The game enters a loop where the player and the computer take turns to attack each other’s grid by selecting coordinates.

  #### 3.1 Player's Turn

  - The player is prompted to enter the row and column numbers for their attack.

  - If the selected coordinate has already been chosen, the player is informed and asked to choose a different coordinate.

  - The game checks whether the player's attack hits a ship on the computer's grid:

    - Hit: The grid is updated to mark the hit with an X, and an explosion animation is displayed.

    - Miss: The grid is updated to mark the miss with an O, and a miss animation is displayed.

  - The updated computer grid is then displayed with hidden ships.

  #### 3.2 Victory Check

- After the player's turn, the game checks if all of the computer's ships have been sunk.

- If all ships are hit, the player wins, and the game congratulates the player before ending the loop.

  #### 3.3 Computer's Turn

- The computer randomly selects a coordinate on the player's grid to attack.

- The game checks whether the computer's attack hits a ship on the player's grid:

  - Hit: The grid is updated to mark the hit with an X, and a message is displayed informing the player of the hit.

  - Miss: The grid is updated to mark the miss with an O, and a message is displayed informing the player of the miss.

- The updated player's grid is then displayed with the locations of ships revealed.

  #### 3.3 Defeat Check

  - After the computer's turn, the game checks if all of the player's ships have been sunk.
  
  - If all ships are hit, the computer wins, and the game displays a game-over message before ending the loop.

>### 4. Game Over and Replay

- Once the game loop ends (either due to a player win or loss), the player is asked if they want to play again.

- If the player chooses to play again (Y), the game restarts from the beginning with a new grid setup.

- If the player chooses not to play again (N), the game displays a farewell message and exits.

>### 5. Exiting the Game
Upon exiting, the game displays a message thanking the player for playing.

## Technologies Used
## Testing

## Bugs

### The size input was being received as a string, instead of integer.
  ```
  File "/workspace/PP3-battlefield/run.py", line 4, in __init__
      self.grid = [['-' for _ in range(size)] for _ in range(size)]
                                                      ^^^^^^^^^^^
  TypeError: 'str' object cannot be interpreted as an integer
  ```

  - Fixed by adding `int()` to the function

### TypeError due to positional arguments mismatch

  ```
  $ python3 run.py
  Please enter your name: 
  Art
  Hi Art, enter grid size (e.g., 5 for a 5x5 grid): 
  3
  Traceback (most recent call last):
    File "/workspace/PP3-battlefield/run.py", line 54, in <module>
      main()
    File "/workspace/PP3-battlefield/run.py", line 43, in main
      player_grid.place_ships()
  TypeError: Grid.place_ships() takes 0 positional arguments but 1 was given
  ```

  - Fixed by adding `self` as a parameter in `place_ships()` function. This parameter is necessary for it to access the Grid instance and check if the cell is empty in `self[row][col]`

  ### TypeError: 'Grid' object is not subscriptable

  ```
  Traceback (most recent call last):
    File "/workspace/PP3-battlefield/run.py", line 54, in <module>
      main()
    File "/workspace/PP3-battlefield/run.py", line 43, in main
      player_grid.place_ships()
    File "/workspace/PP3-battlefield/run.py", line 28, in place_ships
      if self[row][col] == "-": # Checks if hte cell is empty ("-")
        ~~~~^^^^^
  TypeError: 'Grid' object is not subscriptable
  ```

    >  This error occurs because of a mistake in how you're trying to access the grid within the place_ships method.
    > Specifically, the line if self[row][col] == "-" is trying to use the Grid object itself as if it were a list, but self refers to the entire Grid object, not just the grid attribute inside it. - [**Fernando Vilela**](https://github.com/vmafer)

  ### SyntaxError: 'break' outside loop
  ```
  gitpod /workspace/PP3-battlefield (main) $ python3 run.py
    File "/workspace/PP3-battlefield/run.py", line 148
      break
      ^^^^^
  SyntaxError: 'break' outside loop
  ```
  Solved indentation issue by moving the if statement into the while loop

  ```
  # Check for victory condition (all ships hit)
      if all(cell != 'S' for row in computer_grid.grid for cell in row):
          print(f"\nCongratulations {user_name}, you've sunk all the computer's ships!")
          break
  ```
## Validator testing
## Credits

- Solution for the positional argument bug was found in [this answer](https://stackoverflow.com/questions/43839536/typeerror-generatecode-takes-0-positional-arguments-but-1-was-given) on StackOverflow

- Solution for the `TypeError: 'Grid' object is not subscriptable` bug was given by developer [Fernando Vilela](https://github.com/vmafer)

- Explanation and examples for enumerate function used on the grid was taken from this [GeeksforGeeks](https://www.geeksforgeeks.org/enumerate-in-python/) tutorial.

- Line of code used to clear the terminal after every round and when game is restarted was taken from this [StackOverflow answer](https://stackoverflow.com/a/36941376/26410724). The idea for it was given by my mentor [Alan Bushell](https://github.com/Alan-Bushell).
  ```
  import os
  os.system('cls||clear')
  ```

- The function `time.sleep()` was found and explained in this [Code Institute](https://codeinstitute.net/global/blog/how-to-wait-in-python/) post

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Deployment

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

## Acknowledgements

