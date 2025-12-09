import pygame
import enum


class ColorScheme:
    grey_background = pygame.Color("#212F3C")
    player_red = pygame.Color("#E3301C")
    goal_green = pygame.Color("#2ECC71")


class GameState(enum.Enum):
    STARTED = 0
    WON = 1
    LOST = 2


class GameStateMachine:
    """This is an interface that an RL model can query"""
    def __init__(self):
        self.state = GameState.STARTED

    def set_won(self):
        self.state = GameState.WON

    def set_lost(self):
        self.state = GameState.LOST

    def get_state(self) -> GameState:
        return self.state


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, radius, color):
        super().__init__()
        self.radius = radius

        diameter = radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)

        self.rect = self.image.get_rect(center=pos)

    def update(self, dt, keys):
        speed = 300
        if keys[pygame.K_w]:
            self.rect.y -= speed * dt
        if keys[pygame.K_s]:
            self.rect.y += speed * dt
        if keys[pygame.K_a]:
            self.rect.x -= speed * dt
        if keys[pygame.K_d]:
            self.rect.x += speed * dt


class Goal(pygame.sprite.Sprite):
    def __init__(self, pos, size, color):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0

WIDTH, HEIGHT = screen.get_size()

player = Player((50, 50), 40, ColorScheme.player_red)
goal = Goal((WIDTH - 90, HEIGHT - 90), (80, 80), ColorScheme.goal_green)

all_sprites = pygame.sprite.Group(player, goal)
game_state = GameStateMachine()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.update(dt, keys)

    background = ColorScheme.grey_background

    if game_state.get_state() == GameState.WON:
        background = ColorScheme.goal_green

    if game_state.get_state() == GameState.LOST:
        background = ColorScheme.player_red

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background)

    all_sprites.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    if pygame.sprite.collide_circle(player, goal):
        game_state.set_won()


    clock.tick(60)  # limits FPS to 60

    dt = clock.tick(60) / 1000

pygame.quit()
