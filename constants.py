
NUM_OF_FLOORS = 21
NUM_OF_ELEVATORS = 1

MARGIN = 10

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

FLOOR_WIDTH, FLOOR_HEIGHT = 150, 70
ELEVATOR_WIDTH, ELEVATOR_HEIGHT = 100, 70

SURFACE_HEIGHT = MARGIN * 3 + FLOOR_HEIGHT * NUM_OF_FLOORS

FONT_SURFACE_HEIGHT = 8

POS_FLOOR_X, POS_FLOOR_Y = MARGIN, SURFACE_HEIGHT - MARGIN - FLOOR_HEIGHT
POS_NUMBER_OF_FLOOR_X, POS_NUMBER_OF_FLOOR_Y = MARGIN + FLOOR_WIDTH // 2 - FONT_SURFACE_HEIGHT, POS_FLOOR_Y + FONT_SURFACE_HEIGHT

RADIUS_BUTTON = 20

SOUND = "resources/ding.mp3"

ELEVATOR_SPEED = 0.5 # seconds per floor
PIXELS_PER_SECONDS = int(FLOOR_HEIGHT / ELEVATOR_SPEED)
ELEVATOR_REST_TIME = 2 # in seconds

# colors
YELLOW = 250, 250, 0
GREEN = 100, 100, 100
RED = 250, 0, 0
WHITE = 250, 250, 250
BLACK = 0, 0, 0

FLOOR_IMAGE_PATH = "resources/floor.jpg"
ELEVATOR_IMAGE_PATH = "resources/Elevator.png"