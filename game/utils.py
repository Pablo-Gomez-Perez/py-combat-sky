import pygame
from settings import BLACK

def load_all_graphics():
    enemy_images = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(img).convert_alpha(), (100, 100)), False, True)
                    for img in ["assets/colored_2.png", "assets/colored_3.png", "assets/JU87B2-progress_5_1.png", "assets/JU87B2-progress_5.png"]]
    
    explosion_anim = [pygame.transform.scale(pygame.image.load(f"assets/regularExplosion0{i}.png").convert(), (70, 70))
                      for i in range(9)]
    for img in explosion_anim:
        img.set_colorkey(BLACK)  # Aplicar colorkey sin sobrescribir la lista con None

    background = pygame.image.load("assets/main_menu_image.png").convert()
    return enemy_images, explosion_anim, background
