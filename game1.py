import pygame

class Player:
    def __init__(self, x: int, y: int, width: int = 50, height: int = 50):
        self.rect = pygame.Rect(x, y, width, height)  # Define o retângulo do jogador
        self.vel_y = 0  # Velocidade vertical
        self.gravity = 0.5  # Força da gravidade
        self.is_jumping = False  # Estado de pulo

    def __jump(self):
        if not self.is_jumping:
            self.vel_y = -15  # Força do pulo
            self.is_jumping = True

    def __apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y  # Atualiza a posição do personagem

    def __on_out_of_bounds(self):
        if self.rect.right > SCREEN_WIDTH:  # Limite da borda direita
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:   # Limite da borda esquerda
            self.rect.left = 0
        if self.rect.top < 0:   # Limite da borda superior
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:   # Limite da borda inferior
            self.rect.bottom = SCREEN_HEIGHT
            self.is_jumping = False

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.__jump() 

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10

    def update(self):
        self.__apply_gravity()
        self.__on_out_of_bounds()
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Desenha o jogador

# Inicialização do Pygame
pygame.init()

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Instância dos objetos
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.on_event(event)

    keys = pygame.key.get_pressed()
    player.move(keys)

    # Atualização do estado do jogo
    player.update()

    # Renderização
    screen.fill((0, 0, 0))  # Limpa a tela
    player.draw(screen)
    pygame.display.flip()  # Atualiza a tela
    clock.tick(30)  # Controla a taxa de quadros por segundo

pygame.quit()