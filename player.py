import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x : int, y : int) -> object:
        self.rotation : int = 0
        super().__init__(x , y, PLAYER_RADIUS)
    
    def rotate(self : object, dt : int)->None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)    

    def move(self : object, dt : int)->None:
        self.position += (pygame.Vector2(0, 1).rotate(self.rotation) *
                         PLAYER_SPEED * dt)
        
        

                
        

       
    def triangle(self): 
        forward : function   = pygame.Vector2(0, 1).rotate(self.rotation)
        right   : function   = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a       : function   = self.position + forward * self.radius
        b       : function   = self.position - forward * self.radius - right
        c       : function   = self.position - forward * self.radius + right
        return [a, b, c]

