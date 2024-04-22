# Shooter Game

Este es un juego de disparos desarrollado utilizando Pygame, diseñado para demostrar el manejo de sprites, colisiones y eventos en un entorno de juego 2D.

## Descripción

El juego es un shooter vertical donde el jugador controla una nave que debe esquivar y destruir aviones enemigos. 
A medida que el jugador destruye enemigos, gana puntos que se acumulan para aumentar su puntuación. 
El juego termina cuando el escudo del jugador se agota.

## Características

- **Control de Nave**: El jugador puede mover la nave hacia arriba, abajo, izquierda y derecha.
- **Disparos**: El jugador puede disparar a los enemigos.
- **Enemigos**: Los aviones enemigos aparecen en la parte superior y se mueven hacia abajo.
- **Colisiones**: Las colisiones entre las balas del jugador y los enemigos resultan en explosiones y puntos para el jugador.
- **Puntuación**: La puntuación aumenta al destruir enemigos.
- **Explosiones**: Animaciones de explosión cuando los enemigos son destruidos.

## Tecnologías Utilizadas

- Python 3.9
- Pygame 2.5.2
- SDL 2.28.3

## Estructura del Proyecto

C:.
| README.md
| main.py
| settings.py
|
+---assets
| // Imágenes y sonidos utilizados en el juego
|
+---game
| events.py // Manejo de eventos de entrada
| models.py // Modelos de sprite como Player, Enemy, Bullet
| ui.py // Funciones de interfaz de usuario como mostrar texto y la barra de escudo
| utils.py // Funciones utilitarias, como la carga de gráficos
|
---scenes
game_screen.py // Pantalla de inicio y pantalla de juego
menu_screen.py // Pantalla del menú (si es necesaria)


## Cómo Jugar

1. Clonar el repositorio o descargar los archivos.
2. Asegurarse de tener Python y Pygame instalados.
3. Ejecutar `main.py` para iniciar el juego.
4. Usar las teclas de flecha para mover la nave y la barra espaciadora para disparar.

