import pygame

# setup
pygame.init()
WINDOW_WIDTH, WINDOW_HIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pygame.display.set_caption('shanks mas ')
running = True

Surf = pygame.surface(100,200)

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

