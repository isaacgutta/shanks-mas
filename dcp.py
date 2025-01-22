import pygame

import sys

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("kungfu fighters")
        self.screen = pygame.display.set_mode((1050,600))
        self.Clock = pygame.time.Clock()
        
        self.img = pygame.image.load('cloud.png.png')
        
        self.img_pos = [160, 2]
        self.movement = [False, False]  

    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True  
                        if event.type == pygame.KEYUP:
                        
                                self.screen.fill((14, 219 ,248))
                                self.screen.blit(self.img, self.img_pos)
            
                                
                                pygame.display.update()
                                self.Clock.tick(60)
        
Game().run()