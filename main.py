import pygame
from constants import *
from player import Player


def main():
    # --- Initialization ---
    pygame.init()
    clock = pygame.time.Clock()  # Manage frame timing
    dt = 0  # Delta time

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    # Initialize the player at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    ast_player = Player(x, y)

    # --- Main Game Loop ---
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop
                break

        # --- Game Logic ---
        ast_player.update(dt)  # Update the player's state

        # --- Drawing ---
        screen.fill((0, 0, 0))  # Clear the screen with black
        ast_player.draw(screen)  # Draw the player
        pygame.display.flip()  # Update the display

        # --- Frame Timing ---
        dt = clock.tick(60) / 1000  # Frame time in seconds (for smooth updates)

        # Optional: Print frame rate for debugging
        # print(f"FPS: {clock.get_fps():.2f}")

    # --- Cleanup ---
    pygame.quit()


# Start the game only if the script is run directly
if __name__ == "__main__":
    main()
