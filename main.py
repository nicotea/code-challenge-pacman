from character import *
from command import *
import sys, os


# If there are at least 2 arguments
if len(sys.argv) > 1:
	# If the file given in 2nd argument is found
	if os.path.isfile(sys.argv[1]):
		# Store each line in a table
		content = open(sys.argv[1],'r').read().splitlines()

		# Initialisation of objects
		pacman = Character()
		command_temp = Command()

		# Read file, verify commands' validity and execute them
		for line in content:
			command_temp.read_command(line)
			if command_temp.is_command_valid():
				if command_temp.action == command_list[PLACE]:
					pacman.place(command_temp.x, command_temp.y, command_temp.direction)
				elif command_temp.action == command_list[MOVE]:
					pacman.move()
				elif command_temp.action == command_list[LEFT]:
					pacman.left()
				elif command_temp.action == command_list[RIGHT]:
					pacman.right()
				elif command_temp.action == command_list[REPORT]:
					pacman.report()

			# Reset command
			command_temp.reset_command()