import pygame

class Player:
    def __init__(self, x, y, up_key, down_key, left_key, right_key):
        self.x = x
        self.y = y
        self.vel_Y = 0
        self.vel_X = 0
        self.score = 0
        self.up_key = up_key
        self.down_key = down_key
        self.left_key = left_key
        self.right_key = right_key
        self.rect = pygame.Rect(x, y, 15, 90)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.up_key:
                self.vel_Y = -3
            if event.key == self.down_key:
                self.vel_Y = 3
            if event.key == self.left_key:
                self.vel_X = -3
            if event.key == self.right_key:
                self.vel_X = 3
        if event.type == pygame.KEYUP:
            if event.key == self.up_key:
                self.vel_Y = 0
            if event.key == self.down_key:
                self.vel_Y = 0
            if event.key == self.left_key:
                self.vel_X = 0
            if event.key == self.right_key:
                self.vel_X = 0

    def update(self):

        # Limita el movimiento de los jugadores para que no salgan de la pantalla
        self.y = max(0, min(self.y, 600 - 90))  # Limita el movimiento vertical
        self.x = max(0, min(self.x, 800 - 15))  # Limita el movimiento horizontal

        # Actualiza la posición de los jugadores en cada fotograma
        self.y += self.vel_Y
        self.x += self.vel_X


    def draw(self, surface):
        jugador = pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, 15, 90))
        return jugador

    def play_hit_sound(self):
        pygame.mixer.Sound("Raqueta.mp3").play()

    def update(self):
        self.y += self.vel_Y
        self.x += self.vel_X

    def increase_score(self):
        self.score += 1
