import pygame
import random
from constants import *
from circleshape import *
from logger import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		old_radius = self.radius

		self.kill()

		if old_radius <= ASTEROID_MIN_RADIUS:
			return []

		log_event("asteroid_split")

		angle = random.uniform(20, 50)
		
		velocity1 = self.velocity.rotate(angle)
		velocity2 = self.velocity.rotate(-angle)

		new_radius = old_radius - ASTEROID_MIN_RADIUS

		asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

		asteroid1.velocity = velocity1 * 1.2
		asteroid2.velocity = velocity2 * 1.2

		return [asteroid1, asteroid2]