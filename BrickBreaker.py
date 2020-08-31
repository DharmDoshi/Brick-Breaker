import pygame
from paddle import Paddle
from brick import Brick
from ball import Ball

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
light_blue = (0, 176, 240)
red = (255, 0, 0)
orange = (255, 100, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (143, 0, 255)


score = 0
lives = 3

# Screen and title
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker")
all_sprites_list = pygame.sprite.Group()

# Paddle
paddle = Paddle(white, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 580

# Ball
ball = Ball(white, 10, 10)
ball.rect.x = 345
ball.rect.y = 300

# Bricks
all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(red, 80, 30)
    brick.rect.x = 60 + i*100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(6):
    brick = Brick(orange, 80, 30)
    brick.rect.x = 110 + i*100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(5):
    brick = Brick(yellow, 80, 30)
    brick.rect.x = 160 + i*100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(4):
    brick = Brick(green, 80, 30)
    brick.rect.x = 210 + i*100
    brick.rect.y = 180
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(3):
    brick = Brick(blue, 80, 30)
    brick.rect.x = 260 + i*100
    brick.rect.y = 220
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(2):
    brick = Brick(indigo, 80, 30)
    brick.rect.x = 310 + i*100
    brick.rect.y = 260
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(1):
    brick = Brick(violet, 80, 30)
    brick.rect.x = 360 + i*100
    brick.rect.y = 300
    all_sprites_list.add(brick)
    all_bricks.add(brick)

all_sprites_list.add(paddle)
all_sprites_list.add(ball)

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement of paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(10)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(10)

    all_sprites_list.update()

    # Boundary condition for Ball
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, white)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]


    # Collision b/w ball and Paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # Collision of ball with Brick
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 100
        brick.kill()
        if len(all_bricks) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, white)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    screen.fill(black)
    pygame.draw.line(screen, white, [0, 38], [800, 38], 2)

    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (650, 10))

    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
