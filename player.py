import pygame
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
	def __init__(self, x, y, PLAYER_RADIUS):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shot_timer = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		super().draw(screen)

		points = self.triangle()
		pygame.draw.polygon(screen, "white", points, 2)

	def rotate(self, direction, dt):
		self.rotation += direction * (PLAYER_TURN_SPEED * dt)

	def move (self, dt):
		unit_vector = pygame.Vector2(0, 1)
		rotated_vector = unit_vector.rotate(self.rotation)
		rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
		self.position += rotated_with_speed_vector

	def shoot(self):
		shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
		shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
		shot_velocity = shot_direction * PLAYER_SHOOT_SPEED
		shot.velocity = shot_velocity
		
		return shot

	def update(self, dt):
		if self.shot_timer > 0:
			self.shot_timer -= dt

		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-1, dt)
		if keys[pygame.K_d]:
			self.rotate(1, dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(dt)
		if keys[pygame.K_SPACE]:
			if self.shot_timer <= 0:
				self.shot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
				return self.shoot()

		return None