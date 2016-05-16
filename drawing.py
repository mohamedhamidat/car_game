import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue_b =(53, 115, 255)
green= (0, 255,0)

gameDisolay = pygame.display.set_mode((800,600))

gameDisolay.fill(black)

# piwArr = pygame.PixelArray(gameDisolay)
# piwArr [10] [20] = green

# #DRAW LINE 
# pygame.draw.line(gameDisolay, blue_b, (100,100), (300,400), 5)

# #DRAW rect
pygame.draw.rect(gameDisolay, red, (400,0,20, 150))
pygame.draw.rect(gameDisolay, red, (400,300,20, 150))


# #DRAW circle
# pygame.draw.circle(gameDisolay, white, (150,150), 75)

x =70

y = 100
# #DRAW polygone
# pygame.draw.polygon(gameDisolay, green, ((x,y), (x+30,y+30), (x+60,y-40), 
# 	(x+100, y+50),(x+150,y+30), (x+200,y-40), (x+250, y+50)))


# pygame.draw.circle(gameDisolay, white, (350,150), 75)


while True:
	for event in pygame.event.get():
		print (event)
		if event.type == pygame.QUIT :

			pygame.quit()
			quit()


	pygame.display.update()
