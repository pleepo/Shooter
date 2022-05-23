import pygame

pygame.init()


SCREEN_WIDTH = 800
# hard-coded
# SCREEN_HEIGHT = 100
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter Platformer')



(x, y) = (100, 200)  ## sprite image position
#scale = 4
img = pygame.image.load('img/player/Idle/0.png')
img = pygame.transform.scale(img, (img.get_width(), img.get_height()))
rect = img.get_rect()
rect.center = (x, y)


run = True
while run:

	screen.blit(img, rect)

	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False


	pygame.display.update()

pygame.quit()