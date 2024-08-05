import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tiny Rectangle Dodger')

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Rectangle settings
RECT_SIZE = 20
rect_x, rect_y = WIDTH // 2, HEIGHT // 2
rect_speed = 5

def main():
    global rect_x, rect_y  # Use global variables inside the function
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect_x -= rect_speed
        if keys[pygame.K_RIGHT]:
            rect_x += rect_speed
        if keys[pygame.K_UP]:
            rect_y -= rect_speed
        if keys[pygame.K_DOWN]:
            rect_y += rect_speed

        # Ensure rectangle stays within the screen bounds
        rect_x = max(0, min(rect_x, WIDTH - RECT_SIZE))
        rect_y = max(0, min(rect_y, HEIGHT - RECT_SIZE))

        # Clear the screen
        screen.fill(WHITE)

        # Draw the rectangle
        pygame.draw.rect(screen, BLUE, (rect_x, rect_y, RECT_SIZE, RECT_SIZE))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

if __name__ == "__main__":
    main()
