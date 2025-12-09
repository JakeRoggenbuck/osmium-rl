import pygame


class ColorScheme:
    grey_background = pygame.Color("#212F3C")
    player_red = pygame.Color("#E3301C")
    goal_green = pygame.Color("#2ECC71")


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

player_pos = pygame.Vector2(50, 50)

goal_pos = ()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(ColorScheme.grey_background)

    pygame.draw.rect(
        screen,
        ColorScheme.goal_green,
        pygame.Rect(WIDTH - 90, HEIGHT - 90, 80, 80),
    )

    pygame.draw.circle(screen, ColorScheme.player_red, player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    dt = clock.tick(60) / 1000

pygame.quit()
