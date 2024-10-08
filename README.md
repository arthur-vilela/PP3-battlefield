# Battlefield

This project was created to provide a simple yet engaging experience for those seeking a quick distraction through a classic, retro-inspired game. It is designed for individuals who enjoy nostalgic, old-school games and are looking for a fun and accessible way to pass the time. The target audience includes casual gamers, fans of classic strategy games like Battleship, and anyone who appreciates the charm of retro-style graphics and gameplay. Whether you're looking to take a break from your day or relive the joy of a traditional board game in a digital format, this project offers a delightful way to do so.


## [Live Website](https://pp3-battlefield-b25fdc0835a9.herokuapp.com/)

## [Repository](https://github.com/arthur-vilela/PP3-battlefield)



## Table of contents

1. <a href="#flowchart">Flowchart</a>
2. <a href="#game-flow">Game Flow</a>
3. <a href="#technologies-used">Technologies used</a>
4. <a href="#testing">Testing</a>
5. <a href="#bugs">Bugs</a>
6. <a href="#validator-testing">Validator testing</a>
7. <a href="#deployment">Deployment</a>
8. <a href="#credits">Credits</a>
9. <a href="#acknowledgements">Acknowledgements</a>

## Flowchart

![flowchart of the game logic](docs/flowchart.png)

## Game Flow

The Battleship game is a classic two-player strategy game where the objective is to sink all of the opponent's ships. In this Python implementation, the player competes against the computer. The game proceeds through the following steps:

> ### 1. Introduction and Setup

- The game begins with a welcome screen displaying the title of the game.

- The player is prompted to enter their name. The input is validated to ensure it meets specific criteria:
  - The username must have more than three characters.
  - It must contain only letters, with no numbers or special characters.

  ![Screenshot of error messages after wrong name inputs](docs/screenshot-name-validation.png)

  - If the input is invalid, an error message is displayed, and the player is prompted to enter a valid name.

- The player is then asked to choose the size of the grid on which the game will be played. The grid size can range from 3x3 to 8x8.

- Based on the selected grid size, a certain number of ships are placed randomly on both the player’s and the computer’s grids.

  ![Screenshot of the game displaying title, user name input and asking for the grid size](docs/screenshot-flow-intro.png)

> ### 2. Displaying the Grids

- The player's grid is displayed, revealing the locations of their ships (S).

- The computer's grid is also displayed, but with the ships hidden, represented by ~ (water).

  ![Screenshot of player's grid with 3 "S" for ships, and the computer's grid with none](docs/screenshot-flow-display-grid.png)

>### 3. Gameplay Loop

- The game enters a loop where the player and the computer take turns to attack each other’s grid by selecting coordinates.

  #### 3.1 Player's Turn

  - The player is prompted to enter the row and column numbers for their attack.
    ![Screenshot displaying inputs for row and column](docs/screenshot-flow-attack.png)

  - If the selected coordinate has already been chosen, the player is informed and asked to choose a different coordinate.

  - The game checks whether the player's attack hits a ship on the computer's grid:


    - Hit: The grid is updated to mark the hit with an X, and an explosion animation is displayed.
      ![Screenshot displaying text "Hit!" and explosion in ASCII art](docs/screenshot-flow-hit.png)

    - Miss: The grid is updated to mark the miss with an O, and a miss animation is displayed.
      ![Screenshot displaying the text "Miss!" and a ship in ASCII art](docs/screenshot-flow-miss.png)

  - The updated computer grid is then displayed with hidden ships.
    ![Screenshot with updated grids](docs/screenshot-flow-update-grid.png)

  #### 3.2 Victory Check

- After the player's turn, the game checks if all of the computer's ships have been sunk.

- If all ships are hit, the player wins, and the game congratulates the player before ending the loop.
  ![Screenshot of congratulatory message and inviting player to play again](docs/screenshot-flow-congratulations.png)

  #### 3.3 Computer's Turn

- The computer randomly selects a coordinate on the player's grid to attack.

- The game checks whether the computer's attack hits a ship on the player's grid:

  - Hit: The grid is updated to mark the hit with an X, and a message is displayed informing the player of the hit.

  - Miss: The grid is updated to mark the miss with an O, and a message is displayed informing the player of the miss.

- The updated player's grid is then displayed with the locations of ships revealed.

  #### 3.3 Defeat Check

  - After the computer's turn, the game checks if all of the player's ships have been sunk.
  
  - If all ships are hit, the computer wins, and the game displays a game-over message before ending the loop.

    ![Screenshot of game over message](docs/screenshot-flow-game-over.png)

>### 4. Game Over and Replay

- Once the game loop ends (either due to a player win or loss), the player is asked if they want to play again.

- If the player chooses to play again (Y), the game restarts from the beginning with a new grid setup.

- If the player chooses not to play again (N), the game displays a farewell message and exits.
  ![Screenshot displaying goodbye message](docs/screenshot-flow-goodbye.png)

>### 5. Exiting the Game
Upon exiting, the game displays a message thanking the player for playing.

## Technologies Used

| **Tool/Service**                              | **Purpose**                                      |
|-----------------------------------------------|--------------------------------------------------|
| Python                                        | Used to write and create the application         |
| Heroku                                        | Used to deploy and host the application          |
| GitHub                                        | Used to store the code, files and documentation  |
| Gitpod                                        | IDE used for creating the application            |
| Git                                           | Used for version control                         |
|[Code:WOF Style checker](https://www.codewof.co.nz/style/python3/)|Used for formatting Python code according to [PEP 8](https://www.python.org/dev/peps/pep-0008/) (Style Guide for Python Code) and PEP 257 (Docstring Conventions).                      |
|[Lucidcharts](https://lucid.app/)              | Used for creating a flowchart                    |
|[ASCII Art Archive](https://www.asciiart.eu/)  | Used to get ASCII art images for SEA, EXPLOSION, BOAT and TITLE |
|[Colorama](https://pypi.org/project/colorama/) | Used to add color to font and background, improving overall visual appeal to the game |






## Testing


| User story / Feature | Test Method | Expected Outcome | Outcome | Pass/Fail |
|--|--|--|--|--|
| **I want to know if my username input is accepted**  | Enter an invalid username, non-aplha "333", less than 3 characters "a", an empty space within the name "aaa aa" | The game should display an error message prompting for a valid user name. | ![Screenshot of the game displayin error messages and instructing the player to enter a correct input](docs/screenshot-name-validation.png) | Pass |
| **I want to know when my inputs are accepted** | Enter an invalid grid size (e.g., 2 or 9) | The game should display an error message prompting for a valid grid size between 3 and 8. | ![Screenshot of the game display error messages and instructing player to enter a number between 3 and 8](docs/screenshot-grid-size-error.png) | Pass |
| **I want to know what data to enter and when a wrong value is entered** | Enter a non-integer value when prompted for grid size (e.g., "abc") | The game should display an error message prompting for a valid integer. | ![Screenshot of error message indicating invalid input and instructing player to enter an integer](docs/screenshot-grid-size-type-error.png) | Pass |
| **I want to place ships on the grid** | Start the game and observe the player's grid after ships are placed | Ships ('S') should be randomly placed on the grid based on grid size. | ![Screenshot of both grids displaying "S" in random coordinates on player's grid](docs/screenshot-ship-on-grid.png) | Pass |
| **I want to avoid entering a coordinate already used** | Enter a coordinate that has already been shot at | The game should display a message indicating that the coordinate has already been chosen, and prompt the player to select a new one. | ![Screenshot of error message indicating the coordinate has already been chosen](docs/screenshot-repeated-coordinate-error.png) | Pass |
| **I want to see if I hit or miss the opponent's ship** | Take a shot at a coordinate on the computer's grid | The game should display "Hit!" or "Miss!" depending on whether a ship was hit. | ![Screenshot of ASCII art of a ship and the word "Miss!"](docs/screenshot-hit.png) ![Screenshot of ASCII art of an explosion and the word "Hit!"](docs/screenshot-miss.png) | Pass |
| **I want to see the grid updated after each turn** | After each shot, observe the computer's grid display | The grid should update with 'X' for hits and 'O' for misses. | ![Screenshot of computer's grid with "O"s for missed coordinates and "X" for hit ones](docs/screenshot-computers-grid.png) | Pass |
| **I want the computer to take its turn after mine** | Observe the game after the player takes a turn | The computer should randomly select a coordinate on the player's grid and update it with 'X' or 'O'. | ![Screenshot of the computer's turn, their coordinate choice and hit message](docs/screenshot-computers-turn.png) | Pass |
| **I want to know when I've won the game** | Sink all of the computer's ships | The game should display a congratulatory message indicating the player has won. | ![Screenshot of congratulatory message with user's name](docs/screenshot-congratulations-message.png) | Pass |
| **I want to know when I've lost the game** | Let the computer sink all of the player's ships | The game should display a message indicating that the player has lost. | ![Screenshot of game over message and the player's final grid](docs/screenshot-game-over.png) | Pass |
| **I want to play the game again after finishing** | After winning or losing, choose to play again by entering 'Y' | The terminal should be cleared. The game should restart with a new grid and ship placements. | ![Screenshot of initial welcome message with "Battlefield" title in ASCII art](docs/screenshot-welcome-message.png) | Pass |
| **I want the game to exit when I choose not to play again** | After winning or losing, choose not to play again by entering any value other than "Y" or "y" | The game should display a goodbye message and exit. | ![Screenshot of goodbye message after refusing to play again by entering "4"](docs/screenshot-goodbye-message.png) | Pass |



## Bugs

#### The size input was being received as a string, instead of integer.
  ```
  File "/workspace/PP3-battlefield/run.py", line 4, in __init__
      self.grid = [['-' for _ in range(size)] for _ in range(size)]
                                                      ^^^^^^^^^^^
  TypeError: 'str' object cannot be interpreted as an integer
  ```

  - Fixed by adding `int()` to the function

---

#### TypeError due to positional arguments mismatch

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

---

#### TypeError: 'Grid' object is not subscriptable

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

  >  "This error occurs because of a mistake in how you're trying to access the grid within the place_ships method. 
Specifically, the line if self[row][col] == "-" is trying to use the Grid object itself as if it were a list, but self refers to the entire Grid object, not just the grid attribute inside it." - [**Fernando Vilela**](https://github.com/vmafer)

---

#### SyntaxError: 'break' outside loop
  ```
  gitpod /workspace/PP3-battlefield (main) $ python3 run.py
    File "/workspace/PP3-battlefield/run.py", line 148
      break
      ^^^^^
  SyntaxError: 'break' outside loop
  ```
  - Solved indentation issue by moving the if statement into the while loop

    ```
    # Check for victory condition (all ships hit)
        if all(cell != 'S' for row in computer_grid.grid for cell in row):
            print(f"\nCongratulations {user_name}, you've sunk all the computer's ships!")
            break
    ```

---

#### Favicon not being found
![Screenshot of error messages indicating wrong filepath](docs/screenshot-bug-favicon.png)
  - Solved by changing the favicon href to an external href to the image itself in the project's Github repository.
  - The solution was found by Code Institute's tutors John and Rebecca
  ```
  <link rel="icon" type="image/svg+xml" href="https://raw.githubusercontent.com/arthur-vilela/PP3-battlefield/main/assets/favicon/favicon.ico"/>
  ```

## Validator testing

The code in `run.py` was run in [Code Institute's Python Linter](https://pep8ci.herokuapp.com/#) showing no errors found.

![Screenshot of CI Python Linter showing no errors](docs/screenshot-ci-python-linter.png)

## Credits

- Solution for the positional argument bug was found in [this answer](https://stackoverflow.com/questions/43839536/typeerror-generatecode-takes-0-positional-arguments-but-1-was-given) on StackOverflow

- Solution for the `TypeError: 'Grid' object is not subscriptable` bug was given by developer [Fernando Vilela](https://github.com/vmafer)

- Explanation and examples for enumerate function used on the grid was taken from this [GeeksforGeeks](https://www.geeksforgeeks.org/enumerate-in-python/) tutorial.

- Line of code used to clear the terminal after every round and when the game is restarted was taken from this [StackOverflow answer](https://stackoverflow.com/a/36941376/26410724). The idea for it was given by my mentor [Alan Bushell](https://github.com/Alan-Bushell).
  ```
  import os
  os.system('cls||clear')
  ```

- The function `time.sleep()` was found and explained in this [Code Institute](https://codeinstitute.net/global/blog/how-to-wait-in-python/) post.

- Solution for the missing favicon bug was found by Code Institute's tutors John and Rebecca.

## Deployment

### 1. Create a New App on Heroku
1. Navigate to [Heroku](https://www.heroku.com/) and log in to your account.
2. Click on the `New` button and select `Create New App`.
3. Provide a unique name for your application and choose your preferred region.
4. Click on the `Create app` button.

### 2. Configure App Settings
1. After creating the app, go to the `Settings` tab.
2. Under `Config Vars`, click the `Reveal Config Vars` button.
3. Add a new variable:
   - KEY: `PORT`
   - VALUE: `8000`
4. Click the `Add` button to save the configuration.

### 3. Set Up Buildpacks
1. In the `Settings` tab, scroll down to the `Buildpacks` section.
2. Click on `Add buildpack` and select _**Python**_.
3. Add another buildpack and select _**Node.js**_.
4. Ensure that the buildpacks are in this order: Python first, followed by Node.js.
5. Click the `Save changes` button.

### 4. Deploy Your Application
1. Navigate to the `Deploy` tab.
2. Under `Deployment method`, select _**GitHub**_.
3. Connect your GitHub account if it's not already connected.
4. Search for your repository and select it.
5. Click `Connect` to link the repository to Heroku.

### 5. Choose Deployment Method
- **Automatic Deploys**:
  - Enable automatic deploys to allow Heroku to rebuild and deploy your app every time you push changes to the selected branch.
  - Choose the branch you want to deploy and click `Enable Automatic Deploys`.
  
- **Manual Deploys**:
  - To deploy manually, scroll down to the `Manual Deploy` section.
  - Select the branch you want to deploy and click `Deploy Branch`.

### 6. Launch Your Application
- Once the deployment is complete, click on the `Open App` button at the top of the page to view your live application.


## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

## Acknowledgements

- My mentor Alan Bushell for great counseling and positive reinforcement
- My wife Kyra Sendler for user testing and encouragement
