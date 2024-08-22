![flowchart of the game logic](assets/docs/flowchart.png)
## Bugs

```
File "/workspace/PP3-battlefield/run.py", line 4, in __init__
    self.grid = [['-' for _ in range(size)] for _ in range(size)]
                                                     ^^^^^^^^^^^
TypeError: 'str' object cannot be interpreted as an integer
```

The size input was being received as a string, instead of integer. Fixed by add int() to the function

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

Fixed by adding `self` as a parameter in `place_ships()` function. This parameter is necessary for it to access the Grid instance and check if the cell is empty in `self[row][col]`


## Credits

- Solution for the positional argument bug was found in [this answer](https://stackoverflow.com/questions/43839536/typeerror-generatecode-takes-0-positional-arguments-but-1-was-given) on StackOverflow

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
