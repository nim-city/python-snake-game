import pygame
from random import randint
from snake import Snake
from fruit import Fruit

def main():

    # Game constants
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    BLACK_COLOUR = (0,0,0)
    WHITE_COLOUR = (255,255,255)
    SNAKE_LENGTH = 20
    # Game variables
    is_game_over = False
    score = 0
    jump = 20
    speed = 10
    x_change = 0
    y_change = 0
    should_generate_new_fruit = False

    # Basic set up
    pygame.init()
    pygame.display.set_caption("Simple Snake")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Set up score text
    font = pygame.font.Font("assets/Arial.ttf", 24)
    score_text_position = (10,10)

    # Set up snake and fruit
    snake = Snake(screen, SNAKE_LENGTH)
    fruit = Fruit(SNAKE_LENGTH)
    fruit.generate_random_location(screen)

    i = 0
    # Main game loop
    while True:
        i += 1
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if not is_game_over:
                    if event.key == pygame.K_LEFT:
                        x_change = -jump
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = jump
                        y_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = jump
                        x_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -jump
                        x_change = 0
                else:
                    if event.key == pygame.K_SPACE:
                        score = 0
                        jump = 10
                        is_game_over = False
                        x_change = 0
                        y_change = 0
                        snake = Snake(screen, SNAKE_LENGTH)
                

        # Update states
        if not is_game_over:
            if (i % speed) == 0:
                snake.update_pos_by_amount(x_change, y_change)
                i = 0
        if should_generate_new_fruit:
            fruit_location = fruit.generate_random_location(screen)
            should_generate_new_fruit = False

        # Check for collisions
        if snake.check_if_collided_with_edges(screen):
            is_game_over = True
        elif snake.check_if_collected_fruit(fruit):
            score += 1
            should_generate_new_fruit = True

        # Render graphics   
        screen.fill(BLACK_COLOUR)
        # Draw snake
        snake.draw(pygame, screen)
        # Draw fruit
        fruit.draw(pygame, screen)
        # Draw texts
        if is_game_over:
            end_game_text = font.render("Game over! Final score: {}".format(score), 0, WHITE_COLOUR)
            play_again_text = font.render("Press SPACE to play again", 0, WHITE_COLOUR)
            end_game_text_rect = end_game_text.get_rect()
            end_game_text_rect.center = (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 25)
            play_again_text_rect = play_again_text.get_rect()
            play_again_text_rect.center = (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 25)
            screen.blit(end_game_text, end_game_text_rect)
            screen.blit(play_again_text, play_again_text_rect)
        else:
            score_text = font.render("Score: {}".format(score), 1, WHITE_COLOUR)
            screen.blit(score_text, score_text_position)
        
        pygame.display.update()
        


# Starts the program if run from main thread
if __name__ == "__main__":
    main()