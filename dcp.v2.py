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
        
        self.collision_area = pygame.Rect(50, 50, 300, 50)
        
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    elif event.key == pygame.K_DOWN:
                        self.movement[1] = True  
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.movement[event.key - pygame.K_UP] = False
                        
            self.screen.fill((14, 219 ,248))
                                
            if self.movement[0]:
                self.img_pos[1] -= 2
            if self.movement[1]:
                self.img_pos[1] += 2
                            
            self.screen.blit(self.img, self.img_pos)
            
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            
            
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 95, 250), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 55, 150), self.collision_area)
                
            pygame.display.flip()
            self.Clock.tick(60)
        
Game().run()