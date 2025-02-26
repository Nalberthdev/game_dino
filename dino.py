import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo do Dino")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

# Configuração do dinossauro
dino = pygame.Rect(50, 300, 50, 50)
velocidade_y = 0
gravidade = 1

# Obstáculo
obstaculo = pygame.Rect(800, 300, 20, 50)
velocidade_obstaculo = 5

# Relógio para FPS
clock = pygame.time.Clock()

# Loop do jogo
rodando = True
pulando = False
while rodando:
    tela.fill(BRANCO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not pulando:
                velocidade_y = -15
                pulando = True

    # Física do pulo
    velocidade_y += gravidade
    dino.y += velocidade_y

    # Limite do chão
    if dino.y >= 300:
        dino.y = 300
        pulando = False

    # Movimento do obstáculo
    obstaculo.x -= velocidade_obstaculo
    if obstaculo.x < -20:
        obstaculo.x = random.randint(800, 1000)

    # Colisão
    if dino.colliderect(obstaculo):
        print("Game Over!")
        rodando = False

    # Desenha o dinossauro e o obstáculo
    pygame.draw.rect(tela, VERDE, dino)
    pygame.draw.rect(tela, PRETO, obstaculo)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
