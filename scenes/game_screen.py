
import pygame
from game.ui import draw_text
from settings import WIDTH, HEIGHT, FPS

def show_go_screen(screen, background, clock):
    screen.blit(background, [0, 0])
    draw_text(screen, "AVIONES", 65, WIDTH // 2, HEIGHT // 4)
    draw_text(screen, "PRESIONA PARA INICIAR", 27, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
