import pygame
pygame.init()

# Set up display
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird Replica")
# Load images
bird_img = pygame.image.load("bird.png")
obstacle_img = pygame.image.load("obstacle.png")
background_img = pygame.image.load("background.png")
# Bird variables
bird_x, bird_y = 100, height // 2
bird_speed = 5

# Obstacle variables
obstacle_x, obstacle_y = width, 0
obstacle_speed = 5
obstacle_width, obstacle_height = 50, height

# Score
score = 0
font = pygame.font.SysFont(None, 55)
def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Code to make the bird jump
                pass
def move_objects():
    global bird_y, obstacle_x

    # Move bird
    bird_y += bird_speed

    # Move obstacle
    obstacle_x -= obstacle_speed
def check_collision():
    global bird_x, bird_y, obstacle_x, obstacle_y, obstacle_width, obstacle_height

    if bird_x < obstacle_x + obstacle_width and bird_x + 50 > obstacle_x and bird_y < obstacle_y + obstacle_height and bird_y + 50 > obstacle_y:
        # Code for collision (e.g., game over)
        pass
def update_score():
    global score
    score += 1
def display_assets():
    win.blit(background_img, (0, 0))
    win.blit(bird_img, (bird_x, bird_y))
    win.blit(obstacle_img, (obstacle_x, obstacle_y))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    pygame.display.update()
while True:
    handle_input()
    move_objects()
    check_collision()
    update_score()
    display_assets()
