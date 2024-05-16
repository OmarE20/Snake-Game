import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BACKGROUND_COLOR = (36, 25, 52)  # Dark purple
SNAKE_COLOR = (167, 209, 61)  # Light green
FOOD_COLOR = (209, 61, 75)  # Red

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Aesthetic Snake Game')

# Clock
clock = pygame.time.Clock()

# Snake
snake = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
direction = (0, -1)  # Start direction: Up

# Food
food = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

def draw_object(surface, color, pos):
    rect = pygame.Rect((pos[0]*GRID_SIZE, pos[1]*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, color, rect)

def move_snake():
    global snake, food, direction
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Check for collisions with walls or self
    if (new_head in snake or
        new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
        new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
        raise Exception("Game over")

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
    else:
        snake.pop()

def change_direction(new_direction):
    global direction
    # Prevent reversing
    if (new_direction[0] * direction[0] == 0 and
        new_direction[1] * direction[1] == 0):
        direction = new_direction

def main():
    global direction

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        try:
            move_snake()
        except Exception:
            print("Game Over!")
            running = False
            time.sleep(2)  # Pause before closing
            break

        screen.fill(BACKGROUND_COLOR)
        draw_object(screen, FOOD_COLOR, food)
        for part in snake:
            draw_object(screen, SNAKE_COLOR, part)
        
        pygame.display.flip()
        clock.tick(10)  # Control the game speed

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
