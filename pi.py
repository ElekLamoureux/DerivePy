import pygame
import random
import math
pygame.init()

# Set up the screen
screen_width = 10000
screen_height = 10000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Circle")
r = screen_width/2

screen.fill((255, 255, 255))  # Clear the screen
pygame.draw.circle(screen, (0, 0, 0), (r, r), r) # Draw a black circle
    

# Game loop
running = True
circle = 0
out = 0
n = 0
while running:
    n+=1
    x = (random.randint(0, screen_width))
    y = (random.randint(0, screen_height))
    if r < math.sqrt((x-r)**2+(y-r)**2):
        out += 1
    else:
        circle += 1
     #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    # Drawing
    #pygame.draw.circle(screen, (0, 255, 0), (x, y), 1)
     #Update the display
    #pygame.display.flip()
    if n == 100000:
        total = circle + out
        print(4*circle/total)
        n = 0

    total = circle + out
pygame.quit()

