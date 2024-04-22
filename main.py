
#in this file its describe the starting routines for the entire game

import pygame
from settings import WIDTH, HEIGHT, FPS, BLACK
from game.models import PlayerPlane, EnemyPlane, Bullet, Explosion
from game.utils import load_all_graphics
from scenes.game_screen import show_go_screen
from game.ui import draw_text, draw_shield_bar
from game.events import handle_events

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    
    # Loading the graphic resources and configuring the sprites group
    enemy_images, explosion_anim, background = load_all_graphics()
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    #making the Player instance
    player = PlayerPlane()
    all_sprites.add(player)
    
    # initial state of the game
    score = 0
    game_over = True
    
    # Principal game loop
    running = True
    while running:
        if game_over:
            show_go_screen(screen, background, clock)
            game_over = False
            # Restart the game
            all_sprites = pygame.sprite.Group()
            enemies = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            player = PlayerPlane()
            all_sprites.add(player)
            for i in range(8):
                enemy = EnemyPlane(enemy_images)
                all_sprites.add(enemy)
                enemies.add(enemy)
        
        # Event loop handling
        running = not handle_events(player, all_sprites, bullets)
        
        # Updating
        all_sprites.update()
        
        # Cheking enemie's bullets colitions
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10 # Adding points to the score for each hit
            explosion = Explosion(hit.rect.center,explosion_anim)
            all_sprites.add(explosion)
            enemy = EnemyPlane(enemy_images)
            all_sprites.add(enemy)
            enemies.add(enemy)
        
        # checking enemy - player colitions
        hits = pygame.sprite.spritecollide(player, enemies, True)    
        for hit in hits:
            player.shield -= 25
            if player.shield <= 0:
                game_over = True
                

        # Drawing / Rendering
        screen.fill(BLACK)
        screen.blit(background, (0,0))
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH // 2, 10)
        draw_shield_bar(screen, 5, 5, player.shield)
        
        # After draw all, flip the screen
        pygame.display.flip()
        
        # Being sure of stand the game running at the correct velocity
        clock.tick(FPS)
            

    pygame.quit()
    #sys.exit()

if __name__ == "__main__":
    main()
