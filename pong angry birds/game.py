import pygame
from player import Player
from ball import Ball

class PongGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.Tamano = (800, 600)

        self.Ventana = pygame.display.set_mode(self.Tamano)
        self.clock = pygame.time.Clock()

        # Jugador 1 con teclas W, S, A, D
        self.player1 = Player(50, 300 - 45, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        # Jugador 2 con teclas UP, DOWN, LEFT, RIGHT
        self.player2 = Player(750 - 15, 300 - 45, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

        self.ball = Ball(400, 300)

    def run_game(self):
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                self.player1.handle_event(event)
                self.player2.handle_event(event)

            self.player1.update()  # Actualiza la posición del jugador 1
            self.player2.update()  # Actualiza la posición del jugador 2
            
            self.ball.update()

            self.Ventana.fill(self.BLACK)

            jugador1 = self.player1.draw(self.Ventana)
            jugador2 = self.player2.draw(self.Ventana)
            
            pelota = self.ball.draw(self.Ventana)

            if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
                self.ball.vel_X *= -1
                self.player1.play_hit_sound()  # Reproduce el sonido de la raqueta

            if self.ball.x >= self.Tamano[0]:
                self.player1.score += 1
                self.ball.reset()
            
            if self.ball.x <= 0:
                self.player2.score += 1
                self.ball.reset()

            if self.player1.score >= 5 or self.player2.score >= 5:
                game_over = True

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == '__main__':
    game = PongGame()
    game.run_game()
