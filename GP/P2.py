# Aim: Learn basic game designing technologies with Pygame.

# A)	Simple pygame Example.
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 500))
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
      pygame.display.flip()


# B)	Adding an Image in Pygame.
import pygame
from IPython.core.display_functions import display
pygame.init()
white = (255, 255, 255)
height = 678
width = 800
display_surface = pygame.display.set_mode((height,width))
pygame.display.set_caption('Image')
image = pygame.image.load(r"D:\ath\game_dev\PracticalNo2\neymar.jpg")
while True:
  display_surface.fill(white)
  display_surface.blit(image,(0,0))
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      quit()
    pygame.display.update()


# C)	Making use of Pygame Rect.
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
  pygame.display.flip()


# D)	Handling Keydown events in Pygame.
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
done = False
is_blue = True
x = 30
y = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    # Handle continuous key presses for movement (outside the event loop)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 0.5
    if pressed[pygame.K_DOWN]: y += 0.5
    if pressed[pygame.K_LEFT]: x -= 0.5
    if pressed[pygame.K_RIGHT]: x += 0.5

    # Decide color based on is_blue state
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    # Clear the screen and redraw the object
    screen.fill((0, 0, 0))  # Fill the screen with black to clear previous frames
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    # Update the display once per frame
    pygame.display.flip()


# E)	Editing Text and Font in pygame.
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False
font = pygame.font.SysFont("Times new Roman", 72)
text = font.render("Hello, Pygame", True, (255, 0, 0))
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      done = True
  screen.fill((255, 255, 255))
  screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
  pygame.display.flip()
