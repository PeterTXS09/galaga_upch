import random
import pygame
import time
from jugador import Jugador
from alien import Alien
from pantalla_ganaste import Ganaste

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Galaga UPCH")
clock = pygame.time.Clock()

# valores iniciales:
jugador = Jugador(screen.get_height() - 100)
ganaste = Ganaste(800, 600)
game_over = False
aliens = [] # lista
alienrows = 5
aliencols = 24
for y in range(alienrows):
    for x in range(aliencols):
        aliens.append(Alien(x, y, random.randint(0, 1)))

start_time = time.time()

while not game_over:
    clock.tick(20) # <--- cuantas veces por segundo se ejecuta el juego
    events = pygame.event.get() # <--- teclas pulsadas y/o botones
    for event in events: # <--- listando los eventos o botones pulsados
        if event.type == pygame.QUIT: # <-- si presionamos la tecla cerrar
            game_over = True # <--- finaliza el ciclo while
    # borrar pantalla
    screen.fill((0, 0, 0))
    # actualizar posiciones
    jugador.update()
    for a in aliens:
        a.y += 0.05 # bajen de la pantalla...
    if aliens == []:
        jugador.ganar = True # cuando ganamos el juego...
    # verificar si colisiona el jugador con los aliens:
    for c in pygame.sprite.spritecollide(jugador, aliens, 0):
        jugador.vidas -= 1
        jugador.x = 400
    # dibujar
    jugador.draw(screen)

    # cambiar el frame de imagenes:
    end_time = time.time()
    elapsed_time = (end_time - start_time)
    if elapsed_time >= 0.2:
        for a in aliens:
            a.flip_frame()
        start_time = time.time()


    for a in aliens:
        a.draw(screen)
    deadbullets = [] # <--- balas que colisionan o salen de la pantalla
    if jugador.disparos != [] and aliens != []:
        # si hemos disparado o hay algun alien
        for b in jugador.disparos:
             # buscar si hay alguna colision
            found = False
             # colocar Found en False
            for a in pygame.sprite.spritecollide(b, aliens, 0):
                # revisar si algun alien ha colisionado con alguna bala
                aliens.remove(a) # si es así ejecutamos remove()
                a.kill() # eliminar el alien de la memoria
                found = True # marcar found como verdadero
            if found: # si esto es verdadero
                deadbullets.append(b) # agregar el disparo a elementos a eliminar
    # eliminamos los disparos
    for b in deadbullets:
        jugador.disparos.remove(b)
        b.kill()
    # actualizar pantalla

    # ganaste.draw(screen)
    pygame.display.update()
pygame.quit() # <--- finalizar el juego
