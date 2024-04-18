import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define game objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\admin\Downloads\jeff\player_car.JPG")
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH // 2
        self.rect.y = WINDOW_HEIGHT - 100
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < WINDOW_WIDTH - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < WINDOW_HEIGHT - self.rect.height:
            self.rect.y += self.speed

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\admin\Downloads\jeff\coin.JPG")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\admin\Downloads\jeff\enemy_car.JPG")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -50)
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > WINDOW_HEIGHT:
            self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
            self.rect.y = random.randint(-200, -50)
            self.speed = random.randint(3, 7)

# Game loop
def main():
    player = Player()
    coins = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Create initial coins and enemies
    for _ in range(10):
        coins.add(Coin())
        enemies.add(Enemy())

    score = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game objects
        player.update()
        coins.update()
        enemies.update()

        # Check for collisions
        coin_collected = pygame.sprite.spritecollide(player, coins, True)
        if coin_collected:
            score += len(coin_collected)

        enemy_collision = pygame.sprite.spritecollide(player, enemies, False)
        if enemy_collision:
            running = False

        # Draw the game objects
        game_window.fill(WHITE)
        game_window.blit(player.image, player.rect)
        coins.draw(game_window)
        enemies.draw(game_window)

        # Display the score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        game_window.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()