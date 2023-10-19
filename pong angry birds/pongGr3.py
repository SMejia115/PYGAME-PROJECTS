import pygame

if __name__=='__main__':
	pygame.init()
	pygame.mixer.init()
	pygame.font.init()
	#Colores
	Negro = (0, 0, 0)
	Blanco = (255, 255, 255)
	Tamano = (800, 600)
	PlayerAncho = 15
	PlayerAlto = 90

	Ventana = pygame.display.set_mode(Tamano)
	clock = pygame.time.Clock()

	SonidoRaqueta = pygame.mixer.Sound("Raqueta.mp3")
	SonidoGol = pygame.mixer.Sound("Gol.mp3")
	SonidoRebote = pygame.mixer.Sound("Rebote.mp3")
	MiFuente = pygame.font.SysFont

	#Coordenadas y velocidad del jugador 1
	CoorPlayer1_X = 50
	CoorPlayer1_Y = 300 - 45
	player1Vel_Y = 0
	player1Vel_X = 0
	PuntosPlayer1 = 0

	#Coordenadas y velocidad del jugador 2
	CoorPlayer2_X = 750 - PlayerAncho
	CoorPlayer2_Y = 300 - 45
	Player2Vel_Y = 0
	Player2Vel_X = 0
	PuntosPlayer2 = 0

	# Coordenadas de la pelota
	Pelota_X = 400
	Pelota_Y = 300
	PelotaVel_X = 3
	PelotaVel_Y = 3

	

	game_over = False

	while (not game_over) or (PuntosPlayer1 > 5) or (PuntosPlayer2 > 5):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
			# Jugador 1
				if event.key == pygame.K_w:
					player1Vel_Y = -3
				if event.key == pygame.K_s:
					player1Vel_Y = 3
				if event.key == pygame.K_a:
					player1Vel_X = -3
				if event.key == pygame.K_d:
					player1Vel_X = 3
				# Jugador 2
				if event.key == pygame.K_UP:
					Player2Vel_Y = -3
				if event.key == pygame.K_DOWN:
					Player2Vel_Y = 3
				if event.key == pygame.K_LEFT:
					Player2Vel_X = -3
				if event.key == pygame.K_RIGHT:
					Player2Vel_X = 3

			if event.type == pygame.KEYUP:
			# Jugador 1
				if event.key == pygame.K_w:
					player1Vel_Y = 0
				if event.key == pygame.K_s:
					player1Vel_Y = 0
				if event.key == pygame.K_a:
					player1Vel_X = 0
				if event.key == pygame.K_d:
					player1Vel_X = 0
				# Jugador 2
				if event.key == pygame.K_UP:
					Player2Vel_Y = 0
				if event.key == pygame.K_DOWN:
					Player2Vel_Y = 0
				if event.key == pygame.K_LEFT:
					Player2Vel_X = 0
				if event.key == pygame.K_RIGHT:
					Player2Vel_X = 0

		if Pelota_Y > 590 or Pelota_Y < 10:
			PelotaVel_Y *= -1
			pygame.mixer.Sound.play(SonidoRebote)

	# Revisa si la pelota sale del lado derecho
		if Pelota_X > 800:
			Pelota_X = 400
			Pelota_Y = 300
			# Si sale de la pantalla, invierte direccion
			PelotaVel_X *= -1
			PelotaVel_Y *= -1
			PuntosPlayer1 += 1

			#	Sonido de Gol
			pygame.mixer.Sound.play(SonidoGol)

		# Revisa si la pelota sale del lado izquierdo
		if Pelota_X < 0:
			Pelota_X = 400
			Pelota_Y = 300
			# Si sale de la pantalla, invierte direccion
			PelotaVel_X *= -1
			PelotaVel_Y *= -1

			PuntosPlayer2 += 1

			#	Sonido de Gol
			pygame.mixer.Sound.play(SonidoGol)


		# Modifica las coordenadas para dar mov. a los jugadores/ pelota
		CoorPlayer1_Y += player1Vel_Y
		CoorPlayer2_Y += Player2Vel_Y
		if ( (CoorPlayer1_X + player1Vel_X) < 394 and (CoorPlayer1_X + player1Vel_X) > 0):
			CoorPlayer1_X += player1Vel_X
		if ( (CoorPlayer2_X + Player2Vel_X) > 400 and (CoorPlayer2_X + Player2Vel_X) < 785):
			CoorPlayer2_X += Player2Vel_X
		# Movimiento pelota
		Pelota_X += PelotaVel_X
		Pelota_Y += PelotaVel_Y

		Ventana.fill(Negro)
		#Zona de dibujo
		LineaCentral = pygame.draw.rect(Ventana, Blanco, (400, 0,6, 600))
		jugador1 = pygame.draw.rect(Ventana, Blanco, (CoorPlayer1_X, CoorPlayer1_Y, PlayerAncho, PlayerAlto))
		jugador2 = pygame.draw.rect(Ventana, Blanco, (CoorPlayer2_X, CoorPlayer2_Y, PlayerAncho, PlayerAlto))
		pelota = pygame.draw.circle(Ventana, Blanco, (Pelota_X, Pelota_Y), 10)

		# Colisiones
		if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
			PelotaVel_X *= -1
			pygame.mixer.Sound.play(SonidoRaqueta)

		pygame.display.flip()
		clock.tick(60)
	pygame.quit()