import pygame


class Disparo(pygame.sprite.Sprite):
    def __init__(self, x, y, yspeed):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load('imagenes/bullet.png')
        self.x = x - self.imagen.get_width() // 2
        self.y = y
        self.dy = yspeed
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (self.x, self.y)


    def draw(self, screen):
        self.y -= self.dy
        self.rect.topleft = (self.x, self.y)
        screen.blit(self.imagen, [self.x, self.y, self.imagen.get_width(), self.imagen.get_height()])