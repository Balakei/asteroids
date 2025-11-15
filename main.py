import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from shot import *
from logger import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

	asteroids = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = (updatable,)

	asteroid_field = AsteroidField()

	shots = pygame.sprite.Group()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill((0, 0, 0))

		dt = clock.tick(60) / 1000.0

		new_shot = player.update(dt)
		if new_shot:
			shots.add(new_shot)
			updatable.add(new_shot)
			drawable.add(new_shot)

		updatable.update(dt)

		for obj in asteroids:
			if obj.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()

		for shot in shots:
			for asteroid in asteroids:
				if shot.collides_with(asteroid):
					log_event("asteroid_shot")
					obj.kill()
					asteroid.kill()

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		log_state()

	pygame.quit()


if __name__ == "__main__":
    main()
