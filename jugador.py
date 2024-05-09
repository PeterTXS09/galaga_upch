import pygame
from pygame.locals import *
from disparo import Disparo


class Jugador(pygame.sprite.Sprite):
    def __init__(self, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load('imagenes/nave.png')
        self.x = 10
        self.y = ypos
        self.disparos = []
        self.fuente = pygame.font.SysFont('Arial', 25)
        self.vidas = 3
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (self.x, self.y)


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.x += 3
        elif keys[K_LEFT]:
            self.x -= 3

        self.rect.topleft = (self.x, self.y)

        if keys[K_SPACE]:
            self.disparos.append(Disparo(self.x + self.imagen.get_width() // 2, self.y, 20))



    def draw(self, screen):
        screen.blit(self.imagen, [self.x, self.y, self.imagen.get_width(), self.imagen.get_height()])
        self.vidas_texto = self.fuente.render('Vidas: ' + str(self.vidas), True, (255, 100, 100))
        screen.blit(self.vidas_texto, (0, 0))

        for d in self.disparos:
            d.draw(screen)