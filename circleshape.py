import pygame

class CircleShape(pygame.sprite.Sprite):
    """
    Base class for circle-shaped game objects, extending Pygame's Sprite class.

    Attributes:
    - position (pygame.Vector2): The 2D position of the object.
    - velocity (pygame.Vector2): The 2D velocity of the object.
    - radius (float): The radius of the circle.
    """

    def __init__(self, x, y, radius, containers=None):
        """
        Initializes a generic circle-shaped game object.

        Parameters:
        - x (float): The initial x-coordinate of the object.
        - y (float): The initial y-coordinate of the object.
        - radius (float): The radius of the circle.
        - containers (iterable, optional): Sprite groups to automatically add this object to.
        """
        # Initialize the Sprite base class and add to specified containers, if provided
        super().__init__(containers) if containers else super().__init__()

        # Initialize position and velocity as 2D vectors
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        # Store the radius of the circle
        self.radius = radius

    def draw(self, screen):
        """
        Draws the object on the screen. This method should be overridden by subclasses.

        Parameters:
        - screen (pygame.Surface): The surface to draw on.
        """
        raise NotImplementedError("Subclasses must implement the draw() method.")

    def update(self, dt):
        """
        Updates the object's state. This method should be overridden by subclasses.

        Parameters:
        - dt (float): The time since the last update (delta time).
        """
        raise NotImplementedError("Subclasses must implement the update() method.")
