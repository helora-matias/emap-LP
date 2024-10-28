import pygame

# Inicializa o Pygame
pygame.init()

# Cria a tela do jogo
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('Movimentação do Retângulo')

# Define a cor do retângulo (vermelho)
rect_color = (255, 0, 0)
rect = pygame.Rect(100, 100, 50, 50)  # (x, y, largura, altura)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.x -= 1  # Move para a esquerda
    if keys[pygame.K_RIGHT]:
        rect.x += 1  # Move para a direita
    if keys[pygame.K_UP]:
        rect.y -= 1  # Move para cima
    if keys[pygame.K_DOWN]:
        rect.y += 1  # Move para baixo

    # Preenche a tela com branco
    screen.fill((255, 255, 255))
    # Desenha o retângulo na tela
    pygame.draw.rect(screen, rect_color, rect)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()