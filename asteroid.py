import pygame
import random
from   circleshape import CircleShape
from   constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y , radius)
        self.og_image = pygame.image.load("asteroid.png").convert_alpha()
        self.og_image = pygame.transform.scale(self.og_image, (self.radius * 2, self.radius * 2))
        self.image    = self.og_image
        self.rect     = self.image.get_rect(center=self.position)


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
    #def draw(self, screen):
    #    pygame.draw.circle(screen,
    #    (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position    += self.velocity * dt
        self.rect.center = self.position
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle   = random.uniform(20, 50)
            vector1        = self.velocity.rotate(random_angle)
            vector2        = self.velocity.rotate(-random_angle)
            new_radius     = self.radius - ASTEROID_MIN_RADIUS
            
            sp_aster_1     = Asteroid(self.position.x, self.position.y, new_radius)
            sp_aster_1.velocity = vector1 * 1.2
            sp_aster_1.og_image = pygame.transform.scale(self.og_image, (new_radius * 2, new_radius * 2))
            sp_aster_1.image = sp_aster_1.og_image
            sp_aster_1.rect = sp_aster_1.image.get_rect(center=sp_aster_1.position)
            
            sp_aster_2     = Asteroid(self.position.x, self.position.y, new_radius)   
            sp_aster_2.velocity = vector2 * 1.2
            sp_aster_2.og_image = pygame.transform.scale(self.og_image, (new_radius * 2, new_radius * 2))
            sp_aster_2.image = sp_aster_2.og_image
            sp_aster_2.rect = sp_aster_2.image.get_rect(center=sp_aster_2.position)
       
        
        

        
        
    
        


        