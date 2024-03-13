from multiprocessing import reduction

from black import diff
import pygame

pygame.init()  # Always present(loads a lib)

WIDTH, HEIGHT = 700, 500  # Setting the window size
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("arial", 45)

WINNING_SCORE = 10


class Paddle:  # Paddle template
    COLOR = WHITE
    VEL = 4  # What is this???
    # Everything that applies to all are defined semi-globally as VARIABLES

    def __init__(
        self, x, y, width, height
    ):  # This are objects(functions inside classes)
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):  # To move the paddles
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    MAX_VEL = 10
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0  # Because it depends on where it hits the paddles

    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        # We can put += because if it moves negatively(to left) it will be -=
        self.y += self.y_vel

    def reset(self):  # To reset the game once we score
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


def draw(window, paddles, ball, left_score, right_score):  # Its appearance
    window.fill(BLACK)

    left_score_text = SCORE_FONT.render(
        f"{left_score}", 1, WHITE
    )  # 1 stands for antialiasing (always 1)
    right_score_text = SCORE_FONT.render(
        f"{right_score}", 1, WHITE
    )  # These create a drawable object
    window.blit(
        left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20)
    )  # blitting is like drawing
    window.blit(
        right_score_text, (WIDTH * 3 // 4 - right_score_text.get_width() // 2, 20)
    )

    for paddle in paddles:
        paddle.draw(window)  # For loop to draw both paddles

    # To draw a dashed line in the middle of the screen
    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(window, WHITE, (WIDTH // 2, i, 3, HEIGHT // 20))

    ball.draw(window)
    pygame.display.update()  # To update it's appearance


def handle_collision(
    ball, left_paddle, right_paddle
):  # These are the physis of the walls(same refraction angle) and the paddles(depends on position) for hitting the ball
    # To handle the collision with the walls
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    # Physics/Maths
    if ball.x_vel < 0:  # To check where the ball is
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                # To make the physics of ball-paddle. The further from the center of the paddle, the more angle it has
                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def handle_paddle_movement(
    keys, left_paddle, right_paddle
):  # Function for moving the paddles using keyboard movement
    if (
        keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0
    ):  # To stop it from getting out of the screen
        left_paddle.move(up=True)
    if (
        keys[pygame.K_s]
        and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT
    ):
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if (
        keys[pygame.K_DOWN]
        and right_paddle.y + right_paddle.VEL + left_paddle.height <= HEIGHT
    ):
        right_paddle.move(up=False)


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(
        10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
    )  # // is floor division(rounded to nearest whole number)
    right_paddle = Paddle(
        WIDTH - 10 - PADDLE_WIDTH,
        HEIGHT // 2 - PADDLE_HEIGHT // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )

    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while run:  # Initializing the game
        clock.tick(
            FPS
        )  # regulates th speed of th while loop, so that it does not give an error depending on computer's performance
        draw(WINDOW, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():  # Events of user input
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"
        if right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        if won is True:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WINDOW.blit(
                text,
                (
                    WIDTH // 2 - text.get_width() // 2,
                    HEIGHT // 2 - text.get_height() // 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(5000)  # Delay by 5 seconds
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()


if __name__ == "__main__":
    main()  # Only run this if you're going to run the last function
