import pygame
from constants import *
from player import *
from logger import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	


	clock = pygame.time.Clock()
	dt = 0

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill((0, 0, 0))

		dt = clock.tick(60) / 1000.0

		player.update(dt)

		player.draw(screen)

		pygame.display.flip()

		log_state()

	pygame.quit()


if __name__ == "__main__":
    main()
