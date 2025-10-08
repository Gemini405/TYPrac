import pygame, random 
pygame.init() 
screen = pygame.display.set_mode((400,400)) 
clock = pygame.time.Clock() 
x, y, dx, dy = 200, 200, 20, 0 
snake = [(x,y)] 
food = (random.randrange(0, 400, 20), random.randrange(0, 400, 20)) 
 
while True: 
    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: pygame.quit(); exit() 
        if e.type == pygame.KEYDOWN: 
            if e.key == pygame.K_UP and dy == 0: dx, dy = 0, -20 
            if e.key == pygame.K_DOWN and dy == 0: dx, dy = 0, 20 
            if e.key == pygame.K_LEFT and dx == 0: dx, dy = -20, 0 
            if e.key == pygame.K_RIGHT and dx == 0: dx, dy = 20, 0 
 
    x += dx; y += dy 
    if (x, y) in snake or x < 0 or x >= 400 or y < 0 or y >= 400: 
        break  
    snake.append((x, y)) 
    if (x, y) == food: 
        food = (random.randrange(0, 400, 20), random.randrange(0, 400, 20)) 
    else: 
        snake.pop(0) 
 
    screen.fill((0,0,0)) 
    for s in snake: pygame.draw.rect(screen, (0,255,0), (*s, 20, 20)) 
    pygame.draw.rect(screen, (255,0,0), (*food, 20, 20)) 
    pygame.display.flip() 
    clock.tick(10) 
