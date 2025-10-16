import pygame
from .paddle import Paddle
from .ball import Ball

# Game Engine
BLACK = (0, 0, 0)
WINNING_SCORE = 5

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height, winning_score=5):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100
        self.winning_score = winning_score

        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)
        pygame.mixer.init()
        self.hit_sound = pygame.mixer.Sound("sounds/hit.wav")
        self.wall_sound = pygame.mixer.Sound("sounds/wall.wav")
        self.score_sound = pygame.mixer.Sound("sounds/score.wav")


        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player.move(10, self.height)

    def update(self):
        # Move the ball
        self.ball.move()

        # 🔊 Wall bounce sound
        if self.ball.y <= 0 or self.ball.y + self.ball.height >= self.height:
            self.wall_sound.play()

        # 🔊 Paddle collision + fix for tunneling
        if self.ball.rect().colliderect(self.player.rect()) or self.ball.rect().colliderect(self.ai.rect()):
            self.hit_sound.play()
        self.ball.check_collision(self.player, self.ai)

        # 🧮 Check scoring
        if self.ball.x <= 0:
            self.ai_score += 1
            self.score_sound.play()
            self.ball.reset()

        elif self.ball.x >= self.width:
            self.player_score += 1
            self.score_sound.play()
            self.ball.reset()

        # 🤖 AI auto tracking
        self.ai.auto_track(self.ball, self.height)

    
    def check_game_over(self, screen):
    
        if self.player_score >= self.winning_score:
            self.display_winner(screen, "Player Wins!")
            return True
        elif self.ai_score >= self.winning_score:
            self.display_winner(screen, "AI Wins!")
            return True
        return False

    def display_winner(self, screen, message):
        font = pygame.font.SysFont("Arial", 60)
        text = font.render(message, True, WHITE)
        screen.blit(text, (self.width // 2 - text.get_width() // 2,
                        self.height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)

    def render(self, screen):
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width//2, 0), (self.width//2, self.height))

        # Draw score
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width//4, 20))
        screen.blit(ai_text, (self.width * 3//4, 20))
