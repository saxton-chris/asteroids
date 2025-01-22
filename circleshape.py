import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        """
        Initialize a CircleShape instance.

        :param x: The x-coordinate of the object's position.
        :param y: The y-coordinate of the object's position.
        :param radius: The radius of the circle.
        """
        super().__init__(getattr(self, "containers", []))
        self.position = pygame.Vector2(x, y)  # Position vector of the object
        self.velocity = pygame.Vector2(0, 0)  # Velocity vector of the object
        self.radius = radius  # Radius of the circle

    def draw(self, screen):
        """
        To be overridden by subclasses for custom drawing.

        :param screen: The Pygame surface on which the object is drawn.
        """
        raise NotImplementedError("Subclasses must implement draw method.")

    def update(self, dt):
        """
        To be overridden by subclasses for custom updates.

        :param dt: Delta time (elapsed time since the last frame in seconds).
        """
        raise NotImplementedError("Subclasses must implement update method.")

