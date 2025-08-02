import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS 

class Player(CircleShape):
    def __init__(self, x : int, y : int) -> object:
        self.rotation : int = 0
        super().__init__(x , y, PLAYER_RADIUS)
         
       
    def triangle(self): 
        forward : function   = pygame.Vector2(0, 1).rotate(self.rotation)
        right   : function   = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a       : function   = self.position + forward * self.radius
        b       : function   = self.position - forward * self.radius - right
        c       : function   = self.position - forward * self.radius + right
        return [a, b, c]

