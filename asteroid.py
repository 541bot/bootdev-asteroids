from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        # forward = pygame.Vector2(0, 1)
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity_fragment_a= self.velocity.rotate(angle) * 1.2
        velocity_fragment_b = self.velocity.rotate(-angle) * 1.2
        radius_fragment_a = self.radius - ASTEROID_MIN_RADIUS
        radius_fragment_b = self.radius - ASTEROID_MIN_RADIUS
        fragment_a= Asteroid(self.position.x, self.position.y, radius_fragment_a)
        fragment_a.velocity = velocity_fragment_a
        fragment_b= Asteroid(self.position.x, self.position.y, radius_fragment_b)
        fragment_b.velocity = velocity_fragment_b
