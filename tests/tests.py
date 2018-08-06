from context import world, command, character
import unittest, os, sys, subprocess, StringIO

###########################
# Testing world module
###########################
class WorldTest(unittest.TestCase):

	# Test the constants value
	def test_world_constants(self):
		self.assertEqual(world.origin,(0,0))
		self.assertEqual(world.worldsize,(5,5))

	# Test the format_direction function
	def test_world_format_angle(self):
		self.assertEqual(world.format_direction(0), 0)
		self.assertEqual(world.format_direction(90), 90)
		self.assertEqual(world.format_direction(180), 180)
		self.assertEqual(world.format_direction(270), 270)
		self.assertEqual(world.format_direction(-80), 270)

	# Test the direction_to_string function
	def test_world_direction_to_string(self):
		self.assertEqual(world.direction_to_string(0), "EAST")
		self.assertEqual(world.direction_to_string(90), "NORTH")
		self.assertEqual(world.direction_to_string(180), "WEST")
		self.assertEqual(world.direction_to_string(270), "SOUTH")
		self.assertEqual(world.direction_to_string(-80), "SOUTH")

	# Test the is_in_world function
	def test_world_is_in_world(self):
		self.assertTrue(world.is_in_world(0,0))
		self.assertTrue(world.is_in_world(4,4))
		self.assertFalse(world.is_in_world(5,3))
		self.assertFalse(world.is_in_world(7,7))


###########################
# Testing character module
###########################
class CharacterTest(unittest.TestCase):

	# Test the character class initialisation
	def test_character_init(self):
		pacman = character.Character()
		self.assertIsNone(pacman.x)
		self.assertIsNone(pacman.y)
		self.assertIsNone(pacman.direction)

	# Test the place function
	def test_character_place(self):
		pacman = character.Character()
		self.assertFalse(pacman._is_placed())
		pacman.place(0,0,90)
		self.assertEqual(pacman.x,0)
		self.assertEqual(pacman.y,0)
		self.assertEqual(pacman.direction,90)
		self.assertTrue(pacman._is_placed())

	# Test the move function
	def test_character_move(self):
		pacman = character.Character()
		# Command move ignored if character is not placed
		pacman.move()
		self.assertIsNone(pacman.x)
		self.assertIsNone(pacman.y)
		self.assertIsNone(pacman.direction)
		pacman.place(0,0,90)
		pacman.move()
		self.assertEqual(pacman.x,0)
		self.assertEqual(pacman.y,1)
		self.assertEqual(pacman.direction,90)
	
	# Test the left function
	def test_character_left(self):
		pacman = character.Character()
		# Command move ignored if character is not placed
		pacman.left()
		self.assertIsNone(pacman.x)
		self.assertIsNone(pacman.y)
		self.assertIsNone(pacman.direction)
		pacman.place(0,0,90)
		pacman.left()
		self.assertEqual(pacman.x,0)
		self.assertEqual(pacman.y,0)
		self.assertEqual(pacman.direction,180)
	
	# Test the right function
	def test_character_right(self):
		pacman = character.Character()
		# Command move ignored if character is not placed
		pacman.right()
		self.assertIsNone(pacman.x)
		self.assertIsNone(pacman.y)
		self.assertIsNone(pacman.direction)
		pacman.place(0,0,90)
		pacman.right()
		self.assertEqual(pacman.x,0)
		self.assertEqual(pacman.y,0)
		self.assertEqual(pacman.direction,0)
  
  	# Test the report function
	def test_character_report(self):
		pacman = character.Character()
		# Command move ignored if character is not placed
		capturedOutput = StringIO.StringIO()
		sys.stdout = capturedOutput
		pacman.report()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(),"")
		pacman.place(0,0,90)
		sys.stdout = capturedOutput
		pacman.report()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(),"Output: 0,0,NORTH\n")


###########################
# Testing command module
###########################
class CommandTest(unittest.TestCase):
	
	# Test the constants value
	def test_command_constants(self):
		self.assertEqual(command.command_list,("PLACE","MOVE","LEFT","RIGHT","REPORT"))
		self.assertEqual(command.PLACE,0)
		self.assertEqual(command.MOVE,1)
		self.assertEqual(command.LEFT,2)
		self.assertEqual(command.RIGHT,3)
		self.assertEqual(command.REPORT,4)

	# Test the command class initialisation
	def test_command_init(self):
		temp_command = command.Command()
		self.assertIsNone(temp_command.action)
		self.assertIsNone(temp_command.x)
		self.assertIsNone(temp_command.y)
		self.assertIsNone(temp_command.direction)
		self.assertFalse(temp_command.valid)

	# Test the set_command function
	def test_command_set_command(self):
		temp_command = command.Command()
		temp_command._set_command("PLACE",0,0,90,True)
		self.assertEqual(temp_command.action,"PLACE")
		self.assertEqual(temp_command.x,0)
		self.assertEqual(temp_command.y,0)
		self.assertEqual(temp_command.direction,90)
		self.assertEqual(temp_command.valid,True)

	# Test the read_command function
	def test_command_read_command(self):
		temp_command = command.Command()
		temp_command.read_command("PLACE 0,0,NORTH")
		self.assertEqual(temp_command.action,"PLACE")
		self.assertEqual(temp_command.x,0)
		self.assertEqual(temp_command.y,0)
		self.assertEqual(temp_command.direction,90)
		self.assertEqual(temp_command.valid,True)

	# Test the reset_command function
	def test_command_reset_command(self):
		temp_command = command.Command()
		temp_command.read_command("PLACE 0,0,NORTH")
		temp_command.reset_command()
		self.assertIsNone(temp_command.action)
		self.assertIsNone(temp_command.x)
		self.assertIsNone(temp_command.y)
		self.assertIsNone(temp_command.direction)
		self.assertFalse(temp_command.valid)

	# Test the is_command_valid function
	def test_command_is_command_valid(self):
		temp_command = command.Command()
		temp_command.read_command("PLACE 0,0,NORTH")
		self.assertTrue(temp_command.is_command_valid())

###########################
# Testing main
###########################
class MainTest(unittest.TestCase):

	def test_main(self):
		# Testing all the program with test.txt
		result = os.popen("python ../main.py test.txt").read()
		self.assertEqual(result, "Output: 1,0,SOUTH\n")

		# Testing all the program with test2.txt
		result = os.popen("python ../main.py test2.txt").read()
		self.assertEqual(result, "")

		# Testing all the program with test3.txt
		result = os.popen("python ../main.py test3.txt").read()
		self.assertEqual(result, "Output: 2,4,NORTH\n")

###########################
# Unit Test Start
###########################
if __name__ == '__main__':
	unittest.main()