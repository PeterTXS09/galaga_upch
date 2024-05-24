import pygame


class Ganaste(pygame.sprite.Sprite):

    def __init__(self, ancho, alto):
        self.fuente = pygame.font.SysFont(None, 40)
        self.texto = self.fuente.render("GANASTE!!!", True, (0,255, 0))
        self.texto_rectangulo = self.texto.get_rect(center=(ancho // 2, alto // 2))
        self.imagen = pygame.image.load('imagenes/astronauta_ganaste.jpeg')
        self.imagen_rectangulo = self.imagen.get_rect(center=(ancho // 2, alto // 4))

    def draw(self, screen):
        screen.blit(self.imagen, self.imagen_rectangulo)
        screen.blit(self.texto, self.texto_rectangulo)