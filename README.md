![flowchart of the game logic](assets/docs/flowchart.png)
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

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
