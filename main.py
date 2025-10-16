import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60
WINNING_SCORE=5
# Game loop
engine = GameEngine(WIDTH, HEIGHT, WINNING_SCORE)


def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)
    if engine.check_game_over(SCREEN):
      if engine.check_game_over(SCREEN):
        pygame.time.delay(2000)
        return  # immediately stop the main loop

 
    pygame.quit()

def replay_menu():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 48)
    options = ["Best of 3", "Best of 5", "Best of 7", "Exit"]
    selected = 0
    running = True

    while running:
        screen.fill((0, 0, 0))
        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected else (150, 150, 150)
            text = font.render(option, True, color)
            screen.blit(text, (300, 200 + i * 60))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 3:
                        return None
                    # Best of N → first to (N // 2 + 1)
                    best_of = int(options[selected].split()[-1])
                    winning_score = best_of // 2 + 1
                    return winning_score



if __name__ == "__main__":
    if __name__ == "__main__":
        WINNING_SCORE = 5  # default value

        while True:
            engine = GameEngine(WIDTH, HEIGHT, WINNING_SCORE)
            running = True
            while running:
                SCREEN.fill((0, 0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                engine.handle_input()
                engine.update()
                engine.render(SCREEN)

                if engine.check_game_over(SCREEN):
                    pygame.time.delay(2000)
                    running = False

                pygame.display.flip()
                clock.tick(FPS)

            best_score = replay_menu()
            if not best_score:
                pygame.quit()
                break
            WINNING_SCORE = best_score

