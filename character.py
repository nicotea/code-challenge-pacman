from world import direction_to_string, is_in_world
from math import sin, cos, radians

class Character:

	def __init__(self):
		self.x = None
		self.y = None
		self.direction = None

	# Check that the character is placed
	def _is_placed(self):
		if (self.x != None and self.y != None):
			return True
		else:
			return False
	    
	# Place the character
	def place(self,x,y,direction):
		self.x = x
		self.y = y
		self.direction = direction
	
	# Discard all below commands until a valid PLACE command has been executed
	def move(self):
		if self._is_placed():
			newX = self.x + int(cos(radians(self.direction)))
			newY = self.y + int(sin(radians(self.direction)))
			# Prevent Pac-man to moving off the grid
			if is_in_world(newX,newY):
				self.x = newX
				self.y = newY
	
	# Turn the character on the left
	def left(self):
		if self._is_placed():
			self.direction = (self.direction + 90) % 360
	
	# Turn the character on the right
	def right(self):
		if self._is_placed():
			self.direction = (self.direction - 90) % 360
  
  	# Print the character's position and direction
	def report(self):
		if self._is_placed():
			print("Output: " + str(self.x) + "," + str(self.y) + "," + direction_to_string(self.direction))
