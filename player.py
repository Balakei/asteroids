import pygame
from constants import *
from circleshape import *

class Player(CircleShape):
	def __init__(self, x, y, PLAYER_RADIUS):
		super().__init__(x, y, PLAYER_RADIUS)

	rotation = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw (self, screen):
		super().draw(screen)

		points = self.triangle()
		pygame.draw.polygon(screen, "white", points, 2)

	def rotate (self, direction, dt):
		self.rotation += direction * (PLAYER_TURN_SPEED * dt)

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-1, dt)
		if keys[pygame.K_d]:
			self.rotate(1, dt)