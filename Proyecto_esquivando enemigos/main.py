import pygame
import random
import sys

pygame.init()

# Vista cuadro principal del juego
WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva el Enemigo")

# Colores
WHITE = (255, 255, 255)

# Imagenes de jugadores
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")

# Escalado de imagenes
player_size = 100
enemy_size = 100
player_img = pygame.transform.scale(player_img, (player_size, player_size))
enemy_img = pygame.transform.scale(enemy_img, (enemy_size, enemy_size))

# Posiciones-de inicio para jugar y velocidad
player_pos = [WIDTH // 2, HEIGHT - player_size]
player_speed = 5
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 7

clock = pygame.time.Clock()

def detect_collision(player_pos, enemy_pos):
    px, py = player_pos
    ex, ey = enemy_pos
    if (ex < px < ex + enemy_size or ex < px + player_size < ex + enemy_size) and \
       (ey < py < ey + enemy_size or ey < py + player_size < ey + enemy_size):
        return True
    return False

def game_loop():
    running = True
    score = 0

    while running:
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        # Mover a la izquierda
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        # Mover a la derecha
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += player_speed
        # Mover hacia arriba
        if keys[pygame.K_UP] and player_pos[1] > 0:
         player_pos[1] -= player_speed
        # Mover hacia abajo
        if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
         player_pos[1] += player_speed

            

        # Movimiento del enemigo
        enemy_pos[1] += enemy_speed

        if enemy_pos[1] >= HEIGHT:
            enemy_pos[1] = 0
            enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
            score += 1

        if detect_collision(player_pos, enemy_pos):
            print("¡Perdiste! Puntuación:", score)
            running = False

        # Dibujar aviones
        win.blit(player_img, (player_pos[0], player_pos[1]))
        win.blit(enemy_img, (enemy_pos[0], enemy_pos[1]))

        # puntaje
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Puntuación: " + str(score), True, (0, 0, 0))
        win.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(30)

def main_menu():
    menu = True
    while menu:
        win.fill(WHITE)
        font = pygame.font.SysFont("Arial", 40)
        text = font.render("Presiona una tecla y empieza a jugar", True, (0, 0, 0))
        win.blit(text, (50, HEIGHT // 2 - 20))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                menu = False

    game_loop()

main_menu()
