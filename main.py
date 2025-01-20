import pygame
from constants import *

def main():
    # Initialize all pygame modules
    pygame.init()

    # Create a clock object to manage frame timing
    clock = pygame.time.Clock()

    # Set up the game window and set its title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    # Log game initialization details
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop

        # Clear the screen and update the display
        screen.fill("black")
        pygame.display.flip()

        # Maintain frame rate at 60 FPS
        clock.tick(60)

    # Quit pygame gracefully
    pygame.quit()

# Start the game only if the script is run directly
if __name__ == "__main__":
    main()
