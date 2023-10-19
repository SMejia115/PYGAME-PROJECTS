import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.SonidoRebote = pygame.mixer.Sound("Rebote.mp3")
        self.SonidoGol = pygame.mixer.Sound("Gol.mp3")
        self.Blanco = (255, 255, 255)
        self.vel_X = 3
        self.vel_Y = 3

    def update(self):
        # Actualizar la posición de la pelota
        self.x += self.vel_X
        self.y += self.vel_Y

        if self.y > 590 or self.y < 10:
            self.vel_Y *= -1
            pygame.mixer.Sound.play(self.SonidoRebote)

        if self.x > 800:
            self.x = 400
            self.y = 300
            self.vel_X *= -1
            self.vel_Y *= -1
            # PuntosPlayer1 += 1
            pygame.mixer.Sound.play(self.SonidoGol)

        if self.x < 0:
            self.x = 400
            self.y = 300
            self.vel_X *= -1
            self.vel_Y *= -1
            # PuntosPlayer2 += 1
            pygame.mixer.Sound.play(self.SonidoGol)

    def draw(self, surface):
        # Dibujar la pelota en la superficie
        pelota = pygame.draw.circle(surface, self.Blanco, (self.x, self.y), 10)
        return pelota
        

    def reset(self):
        self.x = 400
        self.y = 300
        self.vel_X = abs(self.vel_X)  # Asegura que la pelota se mueva hacia el jugador 1
        self.vel_Y = 3  # Reinicia la velocidad vertical
    # Agregar otros métodos según sea necesario
