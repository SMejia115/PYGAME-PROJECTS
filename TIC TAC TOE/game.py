import pygame 
import sys
import os

current_dir = os.path.dirname(__file__)


menu_dir = os.path.join(current_dir, "..")
sys.path.append(menu_dir)

# import button as button

from button import Button   
from tictactoeLogic import run_tic_tac_toe





#Imagen de fondo 
background_image = pygame.image.load("./images/tic-tac-toe-background.jpg")

def run_game():
  pygame.init()
  screen = pygame.display.set_mode((600,600))
  pygame.display.set_caption("TIC TAC TOE")

  #Poner imagen de fondo 


  #Boton de titulo
  title_button = Button(140, 100, 600, 100, pygame.image.load("./images/buttons/tittle2.png"), pygame.image.load("./images/buttons/tittle1.png"), lambda: print("Title button clicked"))
  title_button.draw(screen)

  #Boton para jugar
  play_button = Button(225, 300, 200, 100, pygame.image.load("./images/buttons/playButton1.png"), pygame.image.load("./images/buttons/playButton2.png"), run_tic_tac_toe)
  play_button.draw(screen)

  #Botón para salir
  exit_button = Button(225, 400, 150, 50, pygame.image.load("./images/buttons/exitButton1.png"), pygame.image.load("./images/buttons/exitButton2.png"), lambda: print("Exit button clicked"))
  exit_button.draw(screen)

  #Booleano para saber si el juego esta corriendo o no
  quit_game = False

  buttons = [title_button, play_button, exit_button]

  #Ciclo para que el juego se mantenga corriendo y se actualice la pantalla
  while not quit_game:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    button.check_hover(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1:
                    for button in buttons:
                        if button.is_hovered:
                            button.perform_action()


    screen.blit(background_image, (0, 0))


    for button in buttons:
      button.draw(screen)

    
        
    pygame.display.flip()

run_game()


  


