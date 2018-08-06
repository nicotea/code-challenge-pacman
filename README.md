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
- **left()** and **right(self)**: Rotate the character by 90° without changing its position
- **report()**: Print the character's position and direction
  
### command.py
It contains the 
- world.py: Contains the worldsize and origin constants, the direction dictionary and 
