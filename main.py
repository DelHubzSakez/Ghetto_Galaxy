import pygame
from   constants      import *
from   player         import Player
from   asteroid       import Asteroid
from   asteroid_field import *
from   shot           import Shot
from   menu           import Menu

def main():
    pygame.init()
    
    game_state = "menu"
    menu_op    : list   = ["Start Game", "Options", "Quit Game"]
    clock      : object = pygame.time.Clock()
    dt         : int    = 0
    screen     : object = pygame.display.set_mode((SCREEN_WIDTH,
                                               SCREEN_HEIGHT))
    
    background : object = pygame.image.load("Ghetto.png").convert()
    
    updateable : object = pygame.sprite.Group()
    drawable   : object = pygame.sprite.Group()
    asteroids  : object = pygame.sprite.Group()

    Player.containers        =  (updateable, drawable)
    Asteroid.containers      =  (asteroids, updateable, drawable)
    AsteroidField.containers =  (updateable,)
    Shot.containers          =  (updateable, drawable)
    
    player    : Player   = Player(x = SCREEN_WIDTH / 2,
                             y = SCREEN_HEIGHT / 2)    
    
    asteroid  : Asteroid = AsteroidField()

    menu      : Menu     = Menu(screen, menu_op, 0)
 
    game_over : object  = pygame.font.Font(None, 100)

    print("Starting Asteroids!")
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if game_state == "menu" and event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                   menu.move_up()
                
                elif event.key == pygame.K_DOWN:
                    menu.move_down()
                
                elif event.key == pygame.K_RETURN:
                    selected_option = menu.options[menu.selected]
                    
                    if selected_option == "Start Game":
                        game_state = "playing"
                    
                    elif selected_option == "Quit Game":
                        return    
                                
        
        screen.blit(background, (0, 0))
        
        if game_state == "menu":
            menu.draw(screen)
        elif game_state == "playing":
                
            for D in drawable:
                D.draw(screen)

            dt = clock.tick(60) / 1000
            updateable.update(dt)     
        
            for o in asteroids:
                if player.collision(o) == True:
                    print("Game Over!")
                    game_state = "game_over"

            for a in asteroids:
                for s in player.shots:
                    if s.collision(a) and a.collision(s):
                        a.split()
                        s.kill() 

        elif game_state == "game_over":
            game_over_surf    = game_over.render("YOU SUCK", True, (128, 0, 0))
            text_rect         = game_over_surf.get_rect()
            text_rect.centerx = (SCREEN_WIDTH / 2)
            text_rect.centery = (SCREEN_HEIGHT/ 2)
            screen.blit(game_over_surf, text_rect)
        
        pygame.display.flip()                  
    

    
        
     
        
    



if __name__ == "__main__":
    main()