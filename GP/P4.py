import pygame, sys, random
from math import sin, cos, radians

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Shooter")
clock = pygame.time.Clock()

# Colors
SKY_BLUE = (173, 216, 230)
RED = (231, 76, 60)
DARK_BLUE = (21, 67, 96)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (244, 208, 63)
BLUE = (46, 134, 193)
PURPLE = (155, 89, 182)

# Font
font = pygame.font.SysFont("Arial", 25)

# Globals
score = 0
GROUND_HEIGHT = 100


class Balloon:
    def __init__(self):
        self.reset()

    def move(self):
        self.y += self.speed * sin(radians(self.angle))
        self.x += self.speed * cos(radians(self.angle))
        if self.y < -50 or self.x < 0 or self.x > WIDTH:
            self.reset()

    def show(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        pygame.draw.line(screen, DARK_BLUE, (self.x, self.y + self.size), (self.x, self.y + self.size + 50), 2)

    def is_clicked(self, pos):
        return (self.x - self.size < pos[0] < self.x + self.size) and (self.y - self.size < pos[1] < self.y + self.size)

    def reset(self):
        self.size = random.randint(20, 40)
        self.x = random.randint(self.size, WIDTH - self.size)
        self.y = HEIGHT - GROUND_HEIGHT
        self.speed = -random.uniform(2, 4)
        self.angle = 90
        self.color = random.choice([RED, YELLOW, BLUE, PURPLE])


def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (20, HEIGHT - GROUND_HEIGHT + 30))


def main():
    global score
    balloons = [Balloon() for _ in range(8)]
    running = True

    while running:
        screen.fill(SKY_BLUE)
        pygame.draw.rect(screen, GRAY, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for balloon in balloons:
                    if balloon.is_clicked(pos):
                        score += 1
                        balloon.reset()

        for balloon in balloons:
            balloon.move()
            balloon.show()

        draw_score()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
