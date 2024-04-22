
import pygame
from game.ui import draw_text
from settings import WIDTH, HEIGHT, BLACK, WHITE, BUTTON_COLOR,FPS

def show_go_screen(screen, background, clock):
    screen.blit(background, [0, 0])
    draw_text(screen, "AVIONES", 65, WIDTH // 2, HEIGHT // 4)
    
    draw_text(screen, "INSTRUCCIONES", 24, WIDTH // 2, HEIGHT // 3)  
    draw_text(screen, "MOVERSE = FLECHAS", 24, WIDTH // 2, HEIGHT // 2.4)
    draw_text(screen, "DISPARAR = SPACE", 24, WIDTH // 2, HEIGHT // 2)    
    play_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, play_button)
    draw_text(screen, "Jugar", 24, WIDTH // 2, HEIGHT // 2 + 65, BLACK)
    exit_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 120, 100, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
    draw_text(screen, "Salir", 24, WIDTH // 2, HEIGHT // 2 + 135, BLACK)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    waiting = False
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    return
