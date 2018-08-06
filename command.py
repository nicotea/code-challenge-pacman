from world import direction_list, is_in_world
import re

# List of commands handled
command_list = ("PLACE","MOVE","LEFT","RIGHT","REPORT")

# Adding constants for code readibility
PLACE = 0
MOVE = 1
LEFT = 2
RIGHT = 3
REPORT = 4

class Command:

	def __init__(self):
		self.reset_command()

	# Set the command
	def _set_command(self,action,x,y,direction,valid):
		self.action = action
		self.x = x
		self.y = y
		self.direction = direction
		self.valid = valid
	
	# Check the command validity and set its variables
	def read_command(self,input):
		# Store the arguments of the command in a table
		tabInput = input.split(" ")

		# Check if the first argument of the command (action) is valid
		if tabInput[0] in command_list:

			# If the command is PLACE, additional checks to be made
			if tabInput[0] == command_list[PLACE]:

				# Check that the 2nd part of the command is existing and in the format X,Y,DIRECTION
				if len(tabInput) > 1 and re.match(r"([0-9]),([0-9]),(\w+)",tabInput[1]):
					# Store the coordinates of the 2nd argument in a table
					tabCoordinates = tabInput[1].split(",")

					# Check that the coordinates are in the world dimension and that the direction command is correct
					if tabCoordinates[2] in direction_list and is_in_world(int(tabCoordinates[0]),int(tabCoordinates[1])):
						# Store the commands coordinates
						self._set_command(tabInput[0],int(tabCoordinates[0]),int(tabCoordinates[1]),direction_list[tabCoordinates[2]],True)

			# If the command is MOVE, LEFT, RIGHT or REPORT, set the command as valid
			else:
				self._set_command(tabInput[0],None,None,None,True)
	
	# Reset all variables and set validity to False	by default
	def reset_command(self):
		self.action = None
		self.x = None
		self.y = None
		self.direction = None
		self.valid = False

	# Return the validity of the command
	def is_command_valid(self):
		return self.valid