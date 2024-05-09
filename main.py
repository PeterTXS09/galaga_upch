import random
import pygame
from jugador import Jugador
from alien import Alien

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Galaga UPCH")
clock = pygame.time.Clock()

# valores iniciales:
jugador = Jugador(screen.get_height() - 100)
game_over = False
aliens = []
alienrows = 5
aliencols = 15
for y in range(alienrows):
    for x in range(aliencols):
        aliens.append(Alien(x, y, random.randint(0, 1)))

while not game_over:
    clock.tick(20)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_over = True
    # borrar pantalla
    screen.fill((0, 0, 0))
    # actualizar posiciones
    jugador.update()
    # dibujar
    jugador.draw(screen)
    for a in aliens:
        a.draw(screen)
    deadbullets = []
    if jugador.disparos != [] and aliens != []:
        for b in jugador.disparos:
            found = False
            for a in pygame.sprite.spritecollide(b, aliens, 0):
                aliens.remove(a)
                a.kill()
                found = True
            if found:
                deadbullets.append(b)
    for b in deadbullets:
        jugador.disparos.remove(b)
        b.kill()
    # actualizar pantalla
    pygame.display.update()
pygame.quit()
