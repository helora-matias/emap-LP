import pygame

# Inicializa o Pygame
pygame.init()

# Define a tela do jogo
screen = pygame.display.set_mode((640, 480))  # Cria uma janela de 640x480 pixels
pygame.display.set_caption('Exemplo de Loop do Jogo')  # Define o título da janela

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():  # Captura eventos
        if event.type == pygame.QUIT:  # Verifica se o evento é de fechamento
            running = False  # Encerra o loop

# Encerra o Pygame
pygame.quit()