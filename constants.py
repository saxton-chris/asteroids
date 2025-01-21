# Screen dimensions for the game window
SCREEN_WIDTH = 1280  # Width of the screen in pixels
SCREEN_HEIGHT = 720  # Height of the screen in pixels

# Constants related to asteroids
ASTEROID_MIN_RADIUS = 20  # Minimum radius of an asteroid in pixels
ASTEROID_KINDS = 3  # Number of different asteroid types
ASTEROID_SPAWN_RATE = 0.8  # Time interval (in seconds) for spawning asteroids
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Maximum radius of an asteroid, dependent on asteroid kinds

# Player-related constants
PLAYER_RADIUS = 20  # Radius of the player character in pixels
PLAYER_TURN_SPEED = 300 #Speed at which the player turns