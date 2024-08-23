import pygame
import random
import sys

# Inicializar o Pygame
pygame.init()

# Definir dimensões da tela
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Adivinhação de Números")

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonte
font = pygame.font.Font(None, 74)


# Função para desenhar texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def main():
    # Inicializar variáveis do jogo
    secret_number = random.randint(1, 100)
    guess = None
    guess_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Limpar a tela
        screen.fill(WHITE)

        # Atualizar o display
        draw_text("Adivinhe o Número (1 a 100)", font, BLACK, screen,
                  SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        # Adicionar mais lógica do jogo e desenhar os elementos na tela
        # Exemplo de atualização com feedback
        if guess is not None:
            if guess < secret_number:
                feedback = "Tente um número maior!"
            elif guess > secret_number:
                feedback = "Tente um número menor!"
            else:
                feedback = f"Parabéns! Você acertou o número {secret_number}!"
        else:
            feedback = "Faça uma adivinhação!"

        draw_text(feedback, font, GREEN if guess == secret_number else RED,
                  screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.flip()

        # Simulação de lógica de adivinhação - para fins de demonstração, substitua com entrada real
        guess = random.randint(
            1, 100)  # Simulação, substitua com input do usuário
        guess_count += 1

        pygame.time.delay(2000)  # Atraso para ver o feedback


if __name__ == "__main__":
    main()
