import pygame

# Inicializa o Pygame
pygame.init()

# Cria a tela do jogo
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('Foguinho e Aguinha')

WaterGirl = pygame.image.load('aguinha.png')
WaterGirl = pygame.transform.scale(WaterGirl, (100, 100))
wg = WaterGirl.get_rect()
wg.topleft = (100, 100)

FireBoy = pygame.image.load('foguinho.png')
FireBoy = pygame.transform.scale(FireBoy, (100, 100))
fb = FireBoy.get_rect()
fb.topleft = (300, 100)

Diamond = pygame.image.load('diamante.png')
Diamond = pygame.transform.scale(Diamond, (60, 60))
dm = Diamond.get_rect()
dm.topleft = (600, 300)

dm_visible = True

# mascara = pygame.mask.from_surface(WaterGirl)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        wg.x -= 1  # Move para a esquerda
    if keys[pygame.K_RIGHT]:
        wg.x += 1  # Move para a direita
    if keys[pygame.K_UP]:
        wg.y -= 1  # Move para cima
    if keys[pygame.K_DOWN]:
        wg.y += 1  # Move para baixo
    if keys[pygame.K_w]:
        fb.y -= 1
    if keys[pygame.K_s]:
        fb.y += 1
    if keys[pygame.K_a]:
        fb.x -= 1
    if keys[pygame.K_d]:
        fb.x += 1
    
    # Verifica colisão entre personagens e o diamante
    if dm_visible:
        if wg.colliderect(dm) or fb.colliderect(dm):
            dm_visible = False  # diamante some

    # Preenche a tela com branco
    screen.fill((255, 255, 255))

    screen.blit(WaterGirl, wg)
    screen.blit(FireBoy, fb)

    # Desenha o diamante apenas se ainda estiver visível
    if dm_visible:
        screen.blit(Diamond, dm)

    # Desenha o retângulo na tela
    # pygame.draw.rect(screen, rect_color, rect)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()