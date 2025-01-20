import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        """
        Initializes a generic circle-shaped game object.
        
        Parameters:
        - x (float): The initial x-coordinate of the object.
        - y (float): The initial y-coordinate of the object.
        - radius (float): The radius of the circle.
        """
        # Initialize the Sprite class with the provided container groups, if specified
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Set the initial position of the circle as a 2D vector
        self.position = pygame.Vector2(x, y)
        
        # Set the initial velocity of the circle as a 2D vector (default is stationary)
        self.velocity = pygame.Vector2(0, 0)
        
        # Define the radius of the circle
        self.radius = radius

    def draw(self, screen):
        """
        Draws the object on the screen. Must be overridden by subclasses.
        
        Parameters:
        - screen (pygame.Surface): The surface to draw on.
        """
        pass  # This is an abstract method to be implemented by subclasses

    def update(self, dt):
        """
        Updates the object's state. Must be overridden by subclasses.
        
        Parameters:
        - dt (float): The time since the last update (delta time).
        """
        pass  # This is an abstract method to be implemented by subclasses
