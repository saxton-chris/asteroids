import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField


def main():
    """
    Main function to initialize and run the game.
    """
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    clock = pygame.time.Clock()

    # Sprite groups for game objects
    updatable = pygame.sprite.Group()  # Group of objects to update each frame
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Add the Player to the sprite groups
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidFielr = AsteroidField()

    dt = 0  # Delta time for frame-independent movement

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state
        for obj in updatable:
            obj.update(dt)

        # Clear the screen and draw all objects
        screen.fill((0, 0, 0))  # Black background
        for obj in drawable:
            obj.draw(screen)  # Draw all sprites in the drawable group

        # Update the display
        pygame.display.flip()

        # Cap the frame rate and calculate delta time
        dt = clock.tick(60) / 1000

    # Quit Pygame gracefully
    pygame.quit()

if __name__ == "__main__":
    main()
