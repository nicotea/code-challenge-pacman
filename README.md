# Code Challenge - Pacman Simulator

Code problem details here: https://github.com/ie/Code-Challenge-1

-----------

## Description

This Pacman simulator reads a text file containing commands of the following form:

```
PLACE X,Y,F

MOVE

LEFT

RIGHT

REPORT
```
It then execute each command to place, move, rotate or report the position of "Pacman" in a 5 x 5 dimension world.

## Constraints

- All commands must be ignored until the first valid PLACE command has been executed
- Pacman must not move off the grid during movement. This also includes the initial placement of Pacman.
- Any move that would cause Pacman to fall must be ignored.

## Architecture
The architecture of the file consists of 4 modules with the following dependencies:

![alt text](https://github.com/nicotea/code-challenge-pacman/blob/master/images/archi_pacman.png)

### main.py 
This module read the file given in the arguments and executes its commands

### character.py 
It contains the class Character() and its method to place, move, rotate and report it:
- **_is_placed()**: Check that the character is placed
- **place(x,y,direction)**: Place the character
- **move()**: Move the character one unit in the direction it is facing
- **left()** and **right()**: Rotate the character by 90° without changing its position
- **report()**: Print the character's position and direction
  
### command.py
It contains the commands list in a table of string (command_list) and the class Command() with the following methods:
- **_set_command(action,x,y,direction,valid)**: It set the action (PLACE, MOVE, etc.), coordinates and valid flag (defaulted to False)
- **read_command(input)**: The input parameter corresponds to a line in the text file that is being read. This method read the line, verify its validity (first word found in command_list, and if the command is a PLACE, check if the coordinates are in the grid), and calls _set_command
- **reset_command()**: reset all variables to None and set the variable "valid" to False
- **is_command_valid()**: returns the value of variable "valid"

### world.py
It contains the constants "worldsize" and "origin", the direction dictionary (each cardinal directions refers to an angle) and the following functions:
- **format_direction(angle)**: Function to format a direction according to the 4 cardinal directions angles (e.g. an angle of 85° would be reformated to 90°)
- **direction_to_string(dir_angle)**: Function to translate the following 4 angles in degree to a cardinal direction string from 0, 90, 180, 270 to EAST, NORTH, WEST, SOUTH
- **is_in_world(x,y)**: Function to verify if the point is in the 5x5 grid

## Testing instructions
Run the following:
```
git clone https://github.com/nicotea/code-challenge-pacman

cd code-challenge-pacman
```

Unit test:
```
cd tests

python tests.py
```

Integration test :
Make sure you're located in the root of the repo
```
python main.py ./command-files/command-1.txt
python main.py ./command-files/command-2.txt
python main.py ./command-files/command-3.txt
python main.py ./command-files/command-4.txt
python main.py ./command-files/command-5.txt
python main.py ./command-files/command-6.txt
```

Remark: Use "py" instead of "python" if you're using Windows
