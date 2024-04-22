
import pygame
from settings import WHITE, GREEN


def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)  # Definir fuente y tamaño de texto
    text_surface = font.render(text, True, WHITE)  # Renderizar texto en superficie
    text_rect = text_surface.get_rect()  # Obtener rectángulo del texto
    text_rect.midtop = (x, y)  # Establecer posición del texto
    surface.blit(text_surface, text_rect)  # Dibujar texto en la superficie

# Función para dibujar la barra de escudo
def draw_shield_bar(surface, x, y, percentage):
    BAR_LENGTH = 100  # Longitud de la barra de escudo
    BAR_HEIGHT = 10  # Altura de la barra de escudo
    fill = (percentage / 100) * BAR_LENGTH  # Calcular tamaño de la barra llena
    border = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)  # Crear rectángulo de la barra
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)  # Crear rectángulo lleno de la barra
    pygame.draw.rect(surface, GREEN, fill)  # Dibujar barra llena
    pygame.draw.rect(surface, WHITE, border, 2)  # Dibujar borde de la barra

