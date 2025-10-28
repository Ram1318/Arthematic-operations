import pygame

# Initialize pygame
pygame.init()

# Set display
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Board")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Square size
sq_size = size[0] // 8

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw chess board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = white
            else:
                color = black
            pygame.draw.rect(screen, color, (col * sq_size, row * sq_size, sq_size, sq_size))

    pygame.display.flip()

pygame.quit()
