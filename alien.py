import random
import pygame

class Alien(pygame.sprite.Sprite):

    def __init__(self, x, y, atype):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.atype = atype
        self.frame = 1
        self.imagen = pygame.image.load('imagenes/aliens_sm.png')
        self.sprite_size = 32
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (self.x * self.sprite_size + 10,
                             self.y * self.sprite_size + 50)

    def flip_frame(self):
        if self.frame == 0:
            self.frame = 1
        else:
            self.frame = 0

    def draw(self, screen):
        self.rect.topleft = (self.x * self.sprite_size + 10,
                             self.y * self.sprite_size + 50)
        screen.blit(self.imagen, [self.x * self.sprite_size + 10,
                                 self.y * self.sprite_size + 50,
                                 self.sprite_size, self.sprite_size],
                    [self.frame * self.sprite_size, self.sprite_size * self.atype, self.sprite_size, self.sprite_size])
