import pygame

# Inicializa o Pygame
pygame.init()

# Cria a tela do jogo
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('Colisão de Objetos')

# Define as cores dos retângulos
rect_color_1 = (255, 0, 0)   # Vermelho
rect_color_2 = (0, 0, 255)   # Azul

# Cria dois retângulos
rect1 = pygame.Rect(100, 100, 50, 50)  # (x, y, largura, altura)
rect2 = pygame.Rect(300, 300, 50, 50)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.x -= 1  # Move o retângulo vermelho para a esquerda
    if keys[pygame.K_RIGHT]:
        rect1.x += 1  # Move o retângulo vermelho para a direita
    if keys[pygame.K_UP]:
        rect1.y -= 1  # Move o retângulo vermelho para cima
    if keys[pygame.K_DOWN]:
        rect1.y += 1  # Move o retângulo vermelho para baixo

    # Preenche a tela com branco
    screen.fill((255, 255, 255))
    
    # Desenha os retângulos na tela
    pygame.draw.rect(screen, rect_color_1, rect1)
    pygame.draw.rect(screen, rect_color_2, rect2)

    # Verifica a colisão
    if rect1.colliderect(rect2):
        # Se houver colisão, transporta o rect1 para uma nova posição
        rect1.x = 100
        rect1.y = 100

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()