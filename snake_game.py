import pygame
import random
import os  # For file handling (to save high score)

# Initialize pygame
pygame.init()

# Screen settings (retro Nokia-like proportions)
screen_width, screen_height = 300, 300
cell_size = 10
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game with High Score")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Clock and speed
clock = pygame.time.Clock()
snake_speed = 5

# Snake properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Food position
food_pos = [random.randrange(1, (screen_width // cell_size)) * cell_size,
            random.randrange(1, (screen_height // cell_size)) * cell_size]
food_spawn = True

# Score variables
score = 0
high_score_file = "high_score.txt"

# Load high score
if os.path.exists(high_score_file):
    with open(high_score_file, "r")   as file:
        high_score = int(file.read())
else:
    high_score = 0

# Save high score function
def save_high_score():
    global high_score
    with open(high_score_file, "w") as file:
        file.write(str(high_score))

# Game over function
def game_over():
    global high_score

    # Update high score if necessary
    if score > high_score:
        high_score = score
        save_high_score()  # Save high score on game over
    
    screen.fill(black)
    font = pygame.font.SysFont('monaco', 24)
    message = font.render('Game Over!', True, white)
    screen.blit(message, (screen_width // 4, screen_height // 2))
    pygame.display.update()
    pygame.time.sleep(2)
    pygame.quit()
    quit()

# Display the score and high score on the screen
def show_score():
    font = pygame.font.SysFont('monaco', 20)
    score_text = font.render(f"Score: {score}", True, white)
    high_score_text = font.render(f"High Score: {high_score}", True, white)
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 30))

# Main game loop
try:
    while True:
        for event in pygame.event.get():
            # Handle window close button
            if event.type == pygame.QUIT:
                save_high_score()  # Save high score when closing the window
                pygame.quit()
                quit()
            # Handle keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Exit game
                    save_high_score()  # Save high score on ESC
                    pygame.quit()
                    quit()
                if event.key == pygame.K_UP and not direction == 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and not direction == 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and not direction == 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and not direction == 'LEFT':
                    change_to = 'RIGHT'

        # Change direction with wrap-around logic
        direction = change_to
        if direction == 'UP':
            snake_pos[1] -= cell_size
            if snake_pos[1] < 0:  # Wrap around when hitting the top wall
                snake_pos[1] = screen_height - cell_size
        elif direction == 'DOWN':
            snake_pos[1] += cell_size
            if snake_pos[1] >= screen_height:  # Wrap around when hitting the bottom wall
                snake_pos[1] = 0
        elif direction == 'LEFT':
            snake_pos[0] -= cell_size
            if snake_pos[0] < 0:  # Wrap around when hitting the left wall
                snake_pos[0] = screen_width - cell_size
        elif direction == 'RIGHT':
            snake_pos[0] += cell_size
            if snake_pos[0] >= screen_width:  # Wrap around when hitting the right wall
                snake_pos[0] = 0

        # Snake growing and food mechanics
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            food_spawn = False
            score += 1  # Increase score when eating fruit
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (screen_width // cell_size)) * cell_size,
                        random.randrange(1, (screen_height // cell_size)) * cell_size]
            food_spawn = True

        # Clear the screen
        screen.fill(black)

        # Draw the snake
        for block in snake_body:
            pygame.draw.rect(screen, white, pygame.Rect(block[0], block[1], cell_size, cell_size))

        # Draw the red fruit
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

        # Game Over conditions
        for block in snake_body[1:]:
            if snake_pos == block:
                game_over()

        # Display the score and high score
        show_score()

        # Update the screen and control the frame rate
        pygame.display.update()
        clock.tick(snake_speed)
except Exception as e:
    save_high_score()  # Save high score in case of unexpected errors
    raise e
