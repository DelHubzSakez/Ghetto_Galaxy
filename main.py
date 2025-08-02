import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock  : object = pygame.time.Clock()
    dt     : int    = 0
    screen : object = pygame.display.set_mode((SCREEN_WIDTH,
                                               SCREEN_HEIGHT))
    player : Player = Player(x = SCREEN_WIDTH / 2,
                             y = SCREEN_HEIGHT / 2)
    
    updateable : object = pygame.sprite.Group(player)
    drawable   : object = pygame.sprite.Group(player)
    Player.containers   = (updateable, drawable)
    
    print("Starting Asteroids!")
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        for D in drawable:
            D.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updateable.update(dt)
        
        
     
        
        



if __name__ == "__main__":
    main()