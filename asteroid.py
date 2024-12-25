import pygame
from circleshape import CircleShape
import pygame.math

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, color=(255, 255, 255)):
        super().__init__(x, y, radius, color)
        self.image = pygame.Surface((2*radius, 2*radius), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, color, (radius, radius), radius, 2)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(1, 1)
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.rect.center = self.position
        print(f"Asteroid Created at: {self.position} with radius {self.rect.width // 2}")
    
    def draw(self, surface, color=(255, 255, 255)):
        pygame.draw.circle(surface, color, (self.rect.centerx, self.rect.centery), self.rect.width // 2, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
        