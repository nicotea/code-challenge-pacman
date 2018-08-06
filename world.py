# Defining gric's size and orgins
origin = (0,0)
worldsize = (5,5)

# Cardinal direction dictionary
direction_list = {
	"NORTH": 90,
	"EAST":  0,
	"SOUTH": 270,
	"WEST":  180
}

# Function to format a direction according to the 4 cardinal directions angles
# Remark: Can be improved if we add additional directions (e.g Southeast)
def format_direction(angle):
	temp_angle = angle % 360
	if temp_angle > 45 and temp_angle <= 135:
		return 90
	if temp_angle > 135 and temp_angle <= 225:
		return 180
	if temp_angle > 225 and temp_angle <= 315:
		return 270
	if temp_angle > 315 or temp_angle <= 45:
		return 0 

# Function to translate the following 4 angles in degree to a cardinal direction string from 0, 90, 180, 270 to EAST, NORTH, WEST, SOUTH
def direction_to_string(dir_angle):
	temp_angle = format_direction(dir_angle)
	for key in direction_list:
		if direction_list[key] == temp_angle:
			return key

# Function to verify if the point is in the grid
def is_in_world(x,y):
	if x >= origin[0] and x < worldsize[0] and y >= origin[1] and y < worldsize[1]:
		return True
	else:
		return False
