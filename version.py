import pygame, random
# Definir constantes para el juego
WIDTH = 420  # Ancho de la pantalla
HEIGHT = 720  # Alto de la pantalla
BLACK = (0, 0, 0)  # Color negro en RGB
WHITE = (255, 255, 255)  # Color blanco en RGB
GREEN = (0, 255, 0)  # Color verde en RGB

# Inicializar Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crear ventana del juego
pygame.display.set_caption("FLY FIGHT")  # Establecer título de la ventana
clock = pygame.time.Clock()  # Crear objeto Clock para controlar FPS

# Función para dibujar texto en la pantalla
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)  # Definir fuente y tamaño de texto
    text_surface = font.render(text, True, GREEN)  # Renderizar texto en superficie
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
    
    # Mostrar el porcentaje de vida restante en la barra
    draw_text(surface, f'{percentage}%', 20, x + BAR_LENGTH + 24, y)

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

    def update(self):
        # Actualizar la posición del jugador en función de las teclas presionadas
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

    def shoot(self):
        # Crear una nueva bala desde la posición del jugador
        bullet = Bullet(self.rect.centerx, self.rect.top)  # Crear objeto bala
        all_sprites.add(bullet)  # Agregar bala al grupo de sprites
        bullets.add(bullet)  # Agregar bala al grupo de balas

# Clase para los aviones enemigos
class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(enemy_images)  # Cargar imagen aleatoria del avión
        self.image.set_colorkey(BLACK)  # Establecer color transparente
        self.rect = self.image.get_rect()  # Obtener rectángulo de la imagen
        self.rect.x = random.randrange(WIDTH - self.rect.width)  # Posición X aleatoria
        self.rect.y = random.randrange(-140, -100)  # Posición Y aleatoria
        self.speedy = random.randrange(1, 10)  # Velocidad vertical aleatoria
        self.speedx = random.randrange(-5, 5)  # Velocidad horizontal aleatoria

    def update(self):
        # Mover el avion y reiniciar su posición si sale de la pantalla
        self.rect.y += self.speedy  # Mover enemyo hacia abajo
        self.rect.x += self.speedx  # Mover enemyo horizontalmente
        if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
            # Si el enemyo sale de la pantalla por abajo o los lados
            self.rect.x = random.randrange(WIDTH - self.rect.width)  # Reiniciar posición X
            self.rect.y = random.randrange(-140, -100)  # Reiniciar posición Y
            self.speedy = random.randrange(1, 10)  # Reiniciar velocidad vertical

# Clase para las balas
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/laser1.png")  # Cargar imagen de bala
        self.image.set_colorkey(BLACK)  # Establecer color transparente
        self.rect = self.image.get_rect()  # Obtener rectángulo de la imagen
        self.rect.y = y  # Establecer posición Y de la bala
        self.rect.centerx = x  # Centrar posición X de la bala
        self.speedy = -10  # Velocidad vertical de la bala

    def update(self):
        # Mover la bala hacia arriba y eliminarla si sale de la pantalla
        self.rect.y += self.speedy  # Mover bala hacia arriba
        if self.rect.bottom < 0:  # Si la bala sale de la pantalla por arriba
            self.kill()  # Eliminar la bala

# Clase para las explosiones
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = explosion_anim[0]  # Cargar primera imagen de la animación de explosión
        self.rect = self.image.get_rect()  # Obtener rectángulo de la imagen
        self.rect.center = center  # Centrar la explosión en el centro del objeto
        self.frame = 0  # Inicializar frame de la animación
        self.last_update = pygame.time.get_ticks()  # Obtener tiempo actual
        self.frame_rate = 50  # Velocidad de la explosión

    def update(self):
        # Actualizar la animación de la explosión
        now = pygame.time.get_ticks()  # Obtener tiempo actual
        if now - self.last_update > self.frame_rate:  # Si ha pasado suficiente tiempo
            self.last_update = now  # Actualizar último tiempo
            self.frame += 1  # Avanzar al siguiente frame
            if self.frame == len(explosion_anim):  # Si se alcanza el final de la animación
                self.kill()  # Eliminar la explosión
            else:
                center = self.rect.center  # Obtener centro actual
                self.image = explosion_anim[self.frame]  # Cambiar imagen al siguiente frame
                self.rect = self.image.get_rect()  # Obtener nuevo rectángulo de imagen
                self.rect.center = center  # Mantener centro

# Función para mostrar la pantalla de inicio
def show_go_screen():
    screen.blit(background, [0, 0])  # Dibujar imagen de fondo en la pantalla
    draw_text(screen, "AVIONES", 65, WIDTH // 2, HEIGHT // 8)  # Dibujar texto "SHOOTER"
    draw_text(screen, "INSTRUCCIONES", 24, WIDTH // 2, HEIGHT // 3)  # Dibujar texto "SHOOTER"
    draw_text(screen, "MOVERSE = FLECHAS", 24, WIDTH // 2, HEIGHT // 2.4)
    draw_text(screen, "DISPARAR= SPACE", 24, WIDTH // 2, HEIGHT // 2)
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50))
    draw_text(screen, "Jugar", 24, WIDTH // 2, HEIGHT // 2.1 + 75)
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 50, HEIGHT // 2 + 120, 100, 50))  # Agregar botón "Salir"
    draw_text(screen, "Salir", 24, WIDTH // 2, HEIGHT // 2.1 + 145)  # Agregar texto "Salir"
    pygame.display.flip()  # Actualizar pantalla
    waiting = True  # Variable de espera
    while waiting:  # Bucle de espera
        clock.tick(60)  # Controlar FPS
        for event in pygame.event.get():  # Obtener eventos
            if event.type == pygame.QUIT:  # Si se cierra la ventana
                pygame.quit()  # Cerrar Pygame
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if WIDTH // 2 - 50 <= mouse_pos[0] <= WIDTH // 2 + 50 and HEIGHT // 2 + 50 <= mouse_pos[1] <= HEIGHT // 2 + 100:
                    waiting = False
                elif WIDTH // 2 - 50 <= mouse_pos[0] <= WIDTH // 2 + 50 and HEIGHT // 2 + 120 <= mouse_pos[1] <= HEIGHT // 2 + 170:
                    pygame.quit()  # Cerrar Pygame cuando se presiona "Salir"



# Lista de imágenes de aviones
enemy_images = []
enemy_list = ["assets/colored_2.png", "assets/colored_3.png", "assets/JU87B2-progress_5_1.png", "assets/JU87B2-progress_5.png"]
for img in enemy_list:  # Para cada imagen en la lista
    enemy_image = pygame.image.load(img).convert_alpha()  # Cargar imagen
    enemy_image_resized = pygame.transform.scale(enemy_image, (100, 100))  # Cambiar tamaño de la imagen
    avion_invertido = pygame.transform.flip(enemy_image_resized, False, True)  # Invertir imagen verticalmente
    enemy_images.append(avion_invertido)  # Agregar imagen a la lista

# Lista de imágenes de explosiones
explosion_anim = []
for i in range(9):  # Para cada frame de la animación
    file = "assets/regularExplosion0{}.png".format(i)  # Nombre del archivo de imagen
    img = pygame.image.load(file).convert()  # Cargar imagen
    img.set_colorkey(BLACK)  # Establecer color transparente
    img_scale = pygame.transform.scale(img, (70, 70))  # Cambiar tamaño de la imagen
    explosion_anim.append(img_scale)  # Agregar imagen a la lista de animación

# Cargar imagen de fondo
background = pygame.image.load("assets/main_menu_image.png").convert()

# Bucle principal del juego
game_over = True  # Variable de estado del juego
running = True  # Variable de ejecución del juego
while running:  # Bucle principal del juego
    if game_over:  # Si el juego está en estado de game over
        show_go_screen()  # Mostrar pantalla de inicio
        game_over = False  # Cambiar estado de game over
        all_sprites = pygame.sprite.Group()  # Grupo de todos los sprites
        enemy_list = pygame.sprite.Group()  # Grupo de aviones aunque la clase se llama enemyos
        bullets = pygame.sprite.Group()  # Grupo de balas

        player = PlayerPlane()  # Crear jugador
        all_sprites.add(player)  # Agregar jugador al grupo de sprites
        for i in range(8):  # Para crear varios avioneds al inicio
            enemy = EnemyPlane()  # Crear avion
            all_sprites.add(enemy)  # Agregar enemyo al grupo de sprites
            enemy_list.add(enemy)  # Agregar enemyo al grupo de aviones
        score = 0  # Inicializar puntuación del jugador

    clock.tick(60)  # Controlar FPS
    for event in pygame.event.get():  # Obtener eventos
        if event.type == pygame.QUIT:  # Si se cierra la ventana
            running = False  # Salir del bucle principal

        elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
            if event.key == pygame.K_SPACE:  # Si se presiona la barra espaciadora
                player.shoot()  # El jugador dispara

    all_sprites.update()  # Actualizar todos los sprites

    # Colisiones - Avion - Bala
    hits = pygame.sprite.groupcollide(enemy_list, bullets, True, True)  # Colisiones entre enemyos y balas
    for hit in hits:  # Para cada colisión
        score += 10  # Incrementar puntuación
        explosion = Explosion(hit.rect.center)  # Crear explosión en la posición del avion
        all_sprites.add(explosion)  # Agregar explosión al grupo de sprites
        enemy = EnemyPlane()  # Crear nuevo avion
        all_sprites.add(enemy)  # Agregar nuevo avion al grupo de sprites
        enemy_list.add(enemy)  # Agregar nuevo avion al grupo de enemyos

    # Chequear colisiones - Jugador - Avion
    hits = pygame.sprite.spritecollide(player, enemy_list, True)  # Colisiones entre jugador y enemyos
    for hit in hits:  # Para cada colisión
        player.shield -= 25  # Reducir escudo del jugador
        enemy = EnemyPlane()  # Crear nuevo avion
        all_sprites.add(enemy)  # Agregar nuevo avion al grupo de sprites
        enemy_list.add(enemy)  # Agregar nuevo avion al grupo de enemyos
        if player.shield <= 0:  # Si el escudo del jugador llega a cero
            game_over = True  # Cambiar estado a game over

    screen.blit(background, [0, 0])  # Dibujar imagen de fondo en la pantalla
    all_sprites.draw(screen)  # Dibujar todos los sprites en la pantalla

    # Marcador
    draw_text(screen, str(score), 25, WIDTH // 2, 10)  # Dibujar puntuación en la pantalla

    # Escudo
    draw_shield_bar(screen, 5, 5, player.shield)  # Dibujar barra de escudo en la pantalla

    pygame.display.flip()  # Actualizar pantalla

pygame.quit()  # Salir de Pygame
