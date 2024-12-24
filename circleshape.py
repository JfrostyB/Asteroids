import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        pygame.sprite.Sprite.__init__(self)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.color = color

    def update(self, dt):
        self.position += self.velocity * dt
        