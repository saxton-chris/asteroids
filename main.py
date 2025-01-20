# Import the pygame library to create the game and handle its graphical and interactive components
import pygame

# Import constants defined in a separate module for cleaner and reusable code
from constants import *

# Main function to initialize and run the game
def main():
    # Initialize all the pygame modules
    pygame.init()

    # Create a clock object to control the frame rate of the game
    clock = pygame.time.Clock()

    # Log game initialization details to the console
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up the display window with the specified dimensions from constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main game loop that runs continuously until the game is quit
    while True:
        # Handle events such as quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check if the Quit event is triggered
                return  # Exit the main function and end the game

        # Fill the screen with a black background for each frame
        screen.fill("black")
        
        # Update the display to reflect any changes
        pygame.display.flip()

        # Limit the game to run at 60 frames per second
        clock.tick(60)

# Check if the script is being run directly and start the game
if __name__ == "__main__":
    main()
