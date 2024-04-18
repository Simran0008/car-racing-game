# car-racing-game

https://www.youtube.com/watch?v=v4WfJtPIBR4

Imports: The script imports the Pygame library and the random module.

Pygame Initialization: The script initializes Pygame using pygame.init().

Game Window Setup: It sets up the game window with a specified width and height using pygame.display.set_mode(). It also sets the window caption using pygame.display.set_caption().

Define Colors: Constants for different colors (BLACK, WHITE, RED, GREEN) are defined using RGB tuples.

Define Game Objects: Three classes are defined for different game objects:

Player: Represents the player's car. It has methods for initializing the car's image, updating its position based on user input, and handling collision detection.
Coin: Represents a coin that the player can collect. It has methods for initializing the coin's image and position.
Enemy: Represents enemy cars that the player must avoid. It has methods for initializing the enemy car's image and position, updating its position, and handling collision detection.
Main Function: The main() function is defined to manage the game loop and handle user input. It sets up the initial game state, including the player's car, coins, enemies, score, clock, and running status.

Start Screen: Before the game starts, a start screen is displayed with a "Start" button. The game loop waits for the player to click the "Start" button before proceeding.

Game Loop: The main game loop runs while the game is running. It updates the game objects, handles user input, checks for collisions, and draws the game objects on the screen.

Collision Detection: The game checks for collisions between the player's car and coins/enemies using pygame.sprite.spritecollide().

Game Over Screen: If the player collides with an enemy, the game over screen is displayed with a "Restart" button. The game loop waits for the player to click the "Restart" button before restarting the game.

Score Display: The current score is displayed on the screen during gameplay.

Quit Pygame: After the game loop exits, Pygame is quit using pygame.quit().

Main Function Call: Finally, the main() function is called if the script is executed directly.
