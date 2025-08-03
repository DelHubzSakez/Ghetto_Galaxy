import pygame
from   constants      import *
from   player         import Player
from   asteroid       import Asteroid
from   asteroid_field import *
from   shot           import Shot

def main():
    pygame.init()
    
    clock      : object = pygame.time.Clock()
    dt         : int    = 0
    screen     : object = pygame.display.set_mode((SCREEN_WIDTH,
                                               SCREEN_HEIGHT))
    updateable : object = pygame.sprite.Group()
    drawable   : object = pygame.sprite.Group()
    asteroids  : object = pygame.sprite.Group()
    shots      : object = pygame.sprite.Group()
    
    Player.containers        =  (updateable, drawable)
    Asteroid.containers      =  (asteroids, updateable, drawable)
    AsteroidField.containers =  (updateable,)
    Shot.containers          =  (updateable, drawable)
    
    player   : Player   = Player(x = SCREEN_WIDTH / 2,
                             y = SCREEN_HEIGHT / 2)    
    
    asteroid : Asteroid = AsteroidField()
    
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
        
        for o in asteroids:
            if player.collision(o) == True:
                print("Game Over!")
                raise SystemExit()
    

    
        
     
        
    



if __name__ == "__main__":
    main()