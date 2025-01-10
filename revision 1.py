import pygame

pygame.init()

SCREEN_HEIGHT = 660
SCREEN_WIDTH = 360

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

X = 250
Y = 250 
radius = 15
vel = 10

background=  pygame.image.load('busalley.jpeg')
screen.blit(background,  (0,0))
DEFAULT_IMAGE_SIZE = (660,360)
background = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)
player = pygame.Rect(X, Y, radius*2, radius*2)
pygame.draw.rect(screen, (255, 50, 50), player)
pygame.display.set_caption("shanks mas")



userInput = pygame.key.get_pressed()
if userInput[pygame.K_LEFT]:
    X += vel
if userInput[pygame.K_RIGHT]:
    X -= vel

    


pygame.display.update()

run = True 

while run:

    pygame.time.delay(10)

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            pygame.quit()
    