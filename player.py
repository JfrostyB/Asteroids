import pygame
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from circleshape import CircleShape
from constants import PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, PLAYER_RADIUS, "white")
        self.rotation = 0
        self.image = pygame.Surface([PLAYER_RADIUS * 2, PLAYER_RADIUS * 2], pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.draw()

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self):
        center = (self.image.get_width() / 2, self.image.get_height() / 2)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        pygame.draw.polygon(self.image, "white", [a, b, c], 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.image.fill((0, 0, 0, 0))
        self.draw()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.center = self.position