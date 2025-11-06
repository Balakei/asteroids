import pygame
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	screen.fill((0, 0, 0))
	pygame.display.flip()

	clock = pygame.time.Clock()
	dt = 0

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		dt = clock.tick(60) / 1000.0

pygame.quit()


if __name__ == "__main__":
    main()
