

# # Importar los módulos necesarios
# import pygame, random

# # Definir constantes para el juego
# WIDTH = 420  # Ancho de la pantalla
# HEIGHT = 720  # Alto de la pantalla
# BLACK = (0, 0, 0)  # Color negro en RGB
# WHITE = (255, 255, 255)  # Color blanco en RGB
# GREEN = (0, 255, 0)  # Color verde en RGB

# # Inicializar Pygame
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crear ventana del juego
# pygame.display.set_caption("Shooter")  # Establecer título de la ventana
# clock = pygame.time.Clock()  # Crear objeto Clock para controlar FPS



# # Función para mostrar la pantalla de inicio
# def show_go_screen():
#     screen.blit(background, [0, 0])  # Dibujar imagen de fondo en la pantalla
#     draw_text(screen, "AVIONES", 65, WIDTH // 2, HEIGHT // 4)  # Dibujar texto "SHOOTER"
#     draw_text(screen, "PRESIONA PARA INICIAR ", 27, WIDTH // 2, HEIGHT // 2)  # Dibujar instrucciones
#     pygame.display.flip()  # Actualizar pantalla
#     waiting = True  # Variable de espera
#     while waiting:  # Bucle de espera
#         clock.tick(60)  # Controlar FPS
#         for event in pygame.event.get():  # Obtener eventos
#             if event.type == pygame.QUIT:  # Si se cierra la ventana
#                 pygame.quit()  # Cerrar Pygame
#             if event.type == pygame.KEYUP:  # Si se suelta una tecla
#                 waiting = False  # Salir del bucle de espera

# # Lista de imágenes de aviones
# enemy_images = []
# enemy_list = ["assets/colored_2.png", "assets/colored_3.png", "assets/JU87B2-progress_5_1.png", "assets/JU87B2-progress_5.png"]
# for img in enemy_list:  # Para cada imagen en la lista
#     enemy_image = pygame.image.load(img).convert_alpha()  # Cargar imagen
#     enemy_image_resized = pygame.transform.scale(enemy_image, (100, 100))  # Cambiar tamaño de la imagen
#     avion_invertido = pygame.transform.flip(enemy_image_resized, False, True)  # Invertir imagen verticalmente
#     enemy_images.append(avion_invertido)  # Agregar imagen a la lista

# # Lista de imágenes de explosiones
# explosion_anim = []
# for i in range(9):  # Para cada frame de la animación
#     file = "assets/regularExplosion0{}.png".format(i)  # Nombre del archivo de imagen
#     img = pygame.image.load(file).convert()  # Cargar imagen
#     img.set_colorkey(BLACK)  # Establecer color transparente
#     img_scale = pygame.transform.scale(img, (70, 70))  # Cambiar tamaño de la imagen
#     explosion_anim.append(img_scale)  # Agregar imagen a la lista de animación

# # Cargar imagen de fondo
# background = pygame.image.load("assets/main_menu_image.png").convert()

# # Bucle principal del juego
# game_over = True  # Variable de estado del juego
# running = True  # Variable de ejecución del juego
# while running:  # Bucle principal del juego
#     if game_over:  # Si el juego está en estado de game over
#         show_go_screen()  # Mostrar pantalla de inicio
#         game_over = False  # Cambiar estado de game over
#         all_sprites = pygame.sprite.Group()  # Grupo de todos los sprites
#         enemy_list = pygame.sprite.Group()  # Grupo de aviones aunque la clase se llama enemyos
#         bullets = pygame.sprite.Group()  # Grupo de balas

#         player = PlayerPlane()  # Crear jugador
#         all_sprites.add(player)  # Agregar jugador al grupo de sprites
#         for i in range(8):  # Para crear varios avioneds al inicio
#             enemy = EnemyPlane()  # Crear avion
#             all_sprites.add(enemy)  # Agregar enemyo al grupo de sprites
#             enemy_list.add(enemy)  # Agregar enemyo al grupo de aviones
#         score = 0  # Inicializar puntuación del jugador

#     clock.tick(60)  # Controlar FPS
#     for event in pygame.event.get():  # Obtener eventos
#         if event.type == pygame.QUIT:  # Si se cierra la ventana
#             running = False  # Salir del bucle principal

#         elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
#             if event.key == pygame.K_SPACE:  # Si se presiona la barra espaciadora
#                 player.shoot()  # El jugador dispara

#     all_sprites.update()  # Actualizar todos los sprites

#     # Colisiones - Avion - Bala
#     hits = pygame.sprite.groupcollide(enemy_list, bullets, True, True)  # Colisiones entre enemyos y balas
#     for hit in hits:  # Para cada colisión
#         score += 10  # Incrementar puntuación
#         explosion = Explosion(hit.rect.center)  # Crear explosión en la posición del avion
#         all_sprites.add(explosion)  # Agregar explosión al grupo de sprites
#         enemy = EnemyPlane()  # Crear nuevo avion
#         all_sprites.add(enemy)  # Agregar nuevo avion al grupo de sprites
#         enemy_list.add(enemy)  # Agregar nuevo avion al grupo de enemyos

#     # Chequear colisiones - Jugador - Avion
#     hits = pygame.sprite.spritecollide(player, enemy_list, True)  # Colisiones entre jugador y enemyos
#     for hit in hits:  # Para cada colisión
#         player.shield -= 25  # Reducir escudo del jugador
#         enemy = EnemyPlane()  # Crear nuevo avion
#         all_sprites.add(enemy)  # Agregar nuevo avion al grupo de sprites
#         enemy_list.add(enemy)  # Agregar nuevo avion al grupo de enemyos
#         if player.shield <= 0:  # Si el escudo del jugador llega a cero
#             game_over = True  # Cambiar estado a game over

#     screen.blit(background, [0, 0])  # Dibujar imagen de fondo en la pantalla
#     all_sprites.draw(screen)  # Dibujar todos los sprites en la pantalla

#     # Marcador
#     draw_text(screen, str(score), 25, WIDTH // 2, 10)  # Dibujar puntuación en la pantalla

#     # Escudo
#     draw_shield_bar(screen, 5, 5, player.shield)  # Dibujar barra de escudo en la pantalla

#     pygame.display.flip()  # Actualizar pantalla

# pygame.quit()  # Salir de Pygame
