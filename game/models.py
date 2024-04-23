# this file include all the game entities

from re import I
import pygame
import random
from settings import WIDTH,HEIGHT,BLACK

# Clase para el jugador
class PlayerPlane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/colored.png").convert_alpha()  # Cargar imagen del jugador
        self.rect = self.image.get_rect()  # Obtener rectángulo de la imagen
        self.rect.centerx = WIDTH // 2  # Centrar jugador en X
        self.rect.bottom = HEIGHT - 10  # Colocar jugador en la parte inferior de la pantalla
        self.speed_x = 0  # Velocidad horizontal inicial
        self.speed_y = 0  # Velocidad vertical inicial
        self.shield = 100  # Valor inicial del escudo del jugador
        self.mask = pygame.mask.from_surface(self.image)
        self.reduce_collision_area()
        
    def reduce_collision_area(self, reduction_persentage = 20):
        mask_size = self.mask.get_size()
        
        for x in range(mask_size[0]):
            for y in range(mask_size[1]):
                if(x < reduction_persentage / 100 * mask_size[0] or
                   x > mask_size[0] * (1 - reduction_persentage / 100) or
                   y < reduction_persentage / 100 * mask_size[1] or
                   y > mask_size[1] * (1 - reduction_persentage / 100)):
                    self.mask.set_at((x,y),0)

    def update(self):# Actualizar la posición del jugador en función de las teclas presionadas
        self.speed_x = 0  # Reiniciar velocidad horizontal
        self.speed_y = 0  # Reiniciar velocidad vertical
        keystate = pygame.key.get_pressed()  # Obtener estado de teclas
        if keystate[pygame.K_LEFT]:  # Si se presiona la tecla izquierda
            self.speed_x = -5  # Establecer velocidad hacia la izquierda
        if keystate[pygame.K_RIGHT]:  # Si se presiona la tecla derecha
            self.speed_x = 5  # Establecer velocidad hacia la derecha
        if keystate[pygame.K_UP]:  # Si se presiona la tecla arriba
            self.speed_y = -5  # Establecer velocidad hacia arriba
        if keystate[pygame.K_DOWN]:  # Si se presiona la tecla abajo
            self.speed_y = 5  # Establecer velocidad hacia abajo
        self.rect.x += self.speed_x  # Mover jugador horizontalmente
        if self.rect.right > WIDTH:  # Si el jugador sale del borde derecho
            self.rect.right = WIDTH  # Mantener al jugador dentro del borde derecho
        if self.rect.left < 0:  # Si el jugador sale del borde izquierdo
            self.rect.left = 0  # Mantener al jugador dentro del borde izquierdo
        self.rect.y += self.speed_y  # Mover jugador verticalmente
        if self.rect.bottom > HEIGHT:  # Si el jugador sale del borde inferior
            self.rect.bottom = HEIGHT  # Mantener al jugador dentro del borde inferior
        if self.rect.top < 0:  # Si el jugador sale del borde superior
            self.rect.top = 0  # Mantener al jugador dentro del borde superior

    def shoot(self, all_sprites, bullets):# Crear una nueva bala desde la posición del jugador
        inclination_factor = 1.25
        bullet_speed_x = self.speed_x * inclination_factor
        bullet = Bullet(self.rect.centerx, self.rect.top, bullet_speed_x)  # Crear objeto bala
        all_sprites.add(bullet)  # Agregar bala al grupo de sprites
        bullets.add(bullet)  # Agregar bala al grupo de balas
        
# Clase para los aviones enemigos
class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self, enemy_images):
        super().__init__()
        self.image = random.choice(enemy_images)  # Cargar imagen aleatoria del avión
        self.image.set_colorkey(BLACK)  # Establecer color transparente
        self.rect = self.image.get_rect()  # Obtener rectángulo de la imagen
        self.rect.x = random.randrange(WIDTH - self.rect.width)  # Posición X aleatoria
        self.rect.y = random.randrange(-140, -100)  # Posición Y aleatoria
        self.speedy = random.randrange(1, 10)  # Velocidad vertical aleatoria
        self.speedx = random.randrange(-5, 5)  # Velocidad horizontal aleatoria

    def update(self):# Mover el avion y reiniciar su posición si sale de la pantalla
        self.rect.y += self.speedy  # Mover enemyo hacia abajo
        self.rect.x += self.speedx  # Mover enemyo horizontalmente
        if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
            # Si el enemyo sale de la pantalla por abajo o los lados
            self.rect.x = random.randrange(WIDTH - self.rect.width)  # Reiniciar posición X
            self.rect.y = random.randrange(-140, -100)  # Reiniciar posición Y
            self.speedy = random.randrange(1, 10)  # Reiniciar velocidad vertical
            
# Clase para las balas
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x=0):
        super().__init__()
        self.image = pygame.image.load("assets/laser1.png")  # Cargar imagen de bala
        self.image.set_colorkey(BLACK)  # Establecer color transparente
        self.rect = self.image.get_rect()  # Obtener rectángulo de la imagen
        self.rect.centerx = x  # Centrar posición X de la bala
        self.rect.y = y  # Establecer posición Y de la bala
        self.speedy = -10  # Velocidad vertical de la bala
        self.speedx = speed_x

    def update(self):# Mover la bala hacia arriba y eliminarla si sale de la pantalla
        self.rect.y += self.speedy  # Mover bala hacia arriba
        self.rect.x += self.speedx
        if self.rect.bottom < 0:  # Si la bala sale de la pantalla por arriba
            self.kill()  # Eliminar la bala
            
# Clase para las explosiones
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, anim):
        super().__init__()
        self.frames = anim
        self.image = self.frames[0]  # Cargar primera imagen de la animación de explosión
        self.rect = self.image.get_rect()  # Obtener rectángulo de la imagen
        self.rect.center = center  # Centrar la explosión en el centro del objeto
        self.frame = 0  # Inicializar frame de la animación
        self.last_update = pygame.time.get_ticks()  # Obtener tiempo actual
        self.frame_rate = 50  # Velocidad de la explosión

    def update(self):# Actualizar la animación de la explosión
        now = pygame.time.get_ticks()  # Obtener tiempo actual
        if now - self.last_update > self.frame_rate:  # Si ha pasado suficiente tiempo
            self.last_update = now  # Actualizar último tiempo
            self.frame += 1  # Avanzar al siguiente frame
            if self.frame == len(self.frames):  # Si se alcanza el final de la animación
                self.kill()  # Eliminar la explosión
            else:
                center = self.rect.center  # Obtener centro actual
                self.image = self.frames[self.frame]  # Cambiar imagen al siguiente frame
                self.rect = self.image.get_rect(center = self.rect.center)
                #self.rect = self.image.get_rect()  # Obtener nuevo rectángulo de imagen
                #self.rect.center = center  # Mantener centro
