# this file include all the game entities

import pygame
import random
from settings import WIDTH,HEIGHT,BLACK

# Clase para el jugador
class PlayerPlane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/colored.png").convert_alpha()  # Cargar imagen del jugador
        self.rect = self.image.get_rect()  # Obtener rect�ngulo de la imagen
        self.rect.centerx = WIDTH // 2  # Centrar jugador en X
        self.rect.bottom = HEIGHT - 10  # Colocar jugador en la parte inferior de la pantalla
        self.speed_x = 0  # Velocidad horizontal inicial
        self.speed_y = 0  # Velocidad vertical inicial
        self.shield = 100  # Valor inicial del escudo del jugador

    def update(self):# Actualizar la posici�n del jugador en funci�n de las teclas presionadas
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

    def shoot(self, all_sprites, bullets):# Crear una nueva bala desde la posici�n del jugador
        bullet = Bullet(self.rect.centerx, self.rect.top)  # Crear objeto bala
        all_sprites.add(bullet)  # Agregar bala al grupo de sprites
        bullets.add(bullet)  # Agregar bala al grupo de balas
        
# Clase para los aviones enemigos
class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self, enemy_images):
        super().__init__()
        self.image = random.choice(enemy_images)  # Cargar imagen aleatoria del avi�n
        self.image.set_colorkey(BLACK)  # Establecer color transparente
        self.rect = self.image.get_rect()  # Obtener rect�ngulo de la imagen
        self.rect.x = random.randrange(WIDTH - self.rect.width)  # Posici�n X aleatoria
        self.rect.y = random.randrange(-140, -100)  # Posici�n Y aleatoria
        self.speedy = random.randrange(1, 10)  # Velocidad vertical aleatoria
        self.speedx = random.randrange(-5, 5)  # Velocidad horizontal aleatoria

    def update(self):# Mover el avion y reiniciar su posici�n si sale de la pantalla
        self.rect.y += self.speedy  # Mover enemyo hacia abajo
        self.rect.x += self.speedx  # Mover enemyo horizontalmente
        if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
            # Si el enemyo sale de la pantalla por abajo o los lados
            self.rect.x = random.randrange(WIDTH - self.rect.width)  # Reiniciar posici�n X
            self.rect.y = random.randrange(-140, -100)  # Reiniciar posici�n Y
            self.speedy = random.randrange(1, 10)  # Reiniciar velocidad vertical
            
# Clase para las balas
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/laser1.png")  # Cargar imagen de bala
        self.image.set_colorkey(BLACK)  # Establecer color transparente
        self.rect = self.image.get_rect()  # Obtener rect�ngulo de la imagen
        self.rect.y = y  # Establecer posici�n Y de la bala
        self.rect.centerx = x  # Centrar posici�n X de la bala
        self.speedy = -10  # Velocidad vertical de la bala

    def update(self):# Mover la bala hacia arriba y eliminarla si sale de la pantalla
        self.rect.y += self.speedy  # Mover bala hacia arriba
        if self.rect.bottom < 0:  # Si la bala sale de la pantalla por arriba
            self.kill()  # Eliminar la bala
            
# Clase para las explosiones
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, anim):
        super().__init__()
        self.frames = anim
        self.image = self.frames[0]  # Cargar primera imagen de la animaci�n de explosi�n
        self.rect = self.image.get_rect()  # Obtener rect�ngulo de la imagen
        self.rect.center = center  # Centrar la explosi�n en el centro del objeto
        self.frame = 0  # Inicializar frame de la animaci�n
        self.last_update = pygame.time.get_ticks()  # Obtener tiempo actual
        self.frame_rate = 50  # Velocidad de la explosi�n

    def update(self):# Actualizar la animaci�n de la explosi�n
        now = pygame.time.get_ticks()  # Obtener tiempo actual
        if now - self.last_update > self.frame_rate:  # Si ha pasado suficiente tiempo
            self.last_update = now  # Actualizar �ltimo tiempo
            self.frame += 1  # Avanzar al siguiente frame
            if self.frame == len(self.frames):  # Si se alcanza el final de la animaci�n
                self.kill()  # Eliminar la explosi�n
            else:
                center = self.rect.center  # Obtener centro actual
                self.image = self.frames[self.frame]  # Cambiar imagen al siguiente frame
                self.rect = self.image.get_rect(center = self.rect.center)
                #self.rect = self.image.get_rect()  # Obtener nuevo rect�ngulo de imagen
                #self.rect.center = center  # Mantener centro
