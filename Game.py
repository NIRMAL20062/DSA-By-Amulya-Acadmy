""" import time

# Game setup
player_inventory = []
echoes = []

# Room descriptions
room_descriptions = {
    "entrance": "You stand at the entrance of the Lost Temple. The air is thick with mystery. There are two paths: one to the LEFT and one to the RIGHT.",
    "left_room": "You enter a dimly lit chamber. The walls are covered in ancient carvings. In the center, there's a pedestal with a RIDDLE inscribed on it.",
    "right_room": "You find yourself in a room filled with mirrors. Each mirror reflects a distorted version of yourself. One of them seems... different.",
    "treasure_room": "You've reached the inner sanctum! A glowing treasure chest sits in the center of the room. But it's locked...",
}

# Riddles and puzzles
riddle = {
    "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
    "answer": "echo",
    "hint": "Think about what repeats your words in the temple...",
}

mirror_puzzle = {
    "clue": "The mirror shows a reflection, but one of them is not you. Which mirror is different? (1, 2, or 3)?",
    "correct_choice": "2",
    "hint": "Look closely at the reflections...",
}

# Game functions
def display_room(room):
    print("\n" + "=" * 40)
    print(room_descriptions[room])
    print("=" * 40)

def solve_riddle():
    print("\nThe riddle on the pedestal reads:")
    print(riddle["question"])
    attempts = 3
    while attempts > 0:
        answer = input("Your answer: ").strip().lower()
        if answer == riddle["answer"]:
            print("\nCorrect! The pedestal slides open, revealing a golden key.")
            player_inventory.append("golden_key")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect. You have {attempts} attempts left. Hint: {riddle['hint']}")
            else:
                print("You failed to solve the riddle. The temple collapses around you. Game Over!")
                exit()

def solve_mirror_puzzle():
    print("\nYou approach the mirrors. One of them seems... off.")
    print(mirror_puzzle["clue"])
    attempts = 3
    while attempts > 0:
        choice = input("Your choice (1, 2, or 3): ").strip()
        if choice == mirror_puzzle["correct_choice"]:
            print("\nCorrect! The mirror shatters, revealing a hidden passage.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect. You have {attempts} attempts left. Hint: {mirror_puzzle['hint']}")
            else:
                print("You failed to solve the puzzle. The mirrors trap you forever. Game Over!")
                exit()

def treasure_room():
    display_room("treasure_room")
    if "golden_key" in player_inventory:
        print("\nYou use the golden key to unlock the treasure chest. Inside, you find the legendary Echo Amulet!")
        print("Congratulations! You've completed the game!")
    else:
        print("\nThe treasure chest is locked. You need a key to open it.")
        print("You wander the temple forever, never finding the key. Game Over!")
    exit()

# Main game loop
def main():
    print("Welcome to 'Echoes of the Lost Temple'!")
    time.sleep(1)
    print("Your goal is to explore the temple, solve puzzles, and find the legendary treasure.")
    time.sleep(1)
    print("Be careful... the temple echoes your every move.")
    time.sleep(1)

    current_room = "entrance"
    while True:
        display_room(current_room)
        if current_room == "entrance":
            choice = input("Which path will you take? (LEFT/RIGHT): ").strip().lower()
            if choice == "left":
                current_room = "left_room"
            elif choice == "right":
                current_room = "right_room"
            else:
                print("Invalid choice. Try again.")
        elif current_room == "left_room":
            solve_riddle()
            current_room = "treasure_room"
        elif current_room == "right_room":
            solve_mirror_puzzle()
            current_room = "treasure_room"
        elif current_room == "treasure_room":
            treasure_room()

# Run the game
if __name__ == "__main__":
    main() """




""" import time
import random

# Player stats
player = {
    "health": 100,
    "attack": 15,
    "defense": 10,
    "inventory": [],
}

# Enemy stats
enemies = {
    "shadow_wraith": {"health": 50, "attack": 10, "defense": 5},
    "stone_golem": {"health": 80, "attack": 15, "defense": 10},
    "temple_guardian": {"health": 120, "attack": 20, "defense": 15},
}

# Room descriptions
room_descriptions = {
    "entrance": "You stand at the entrance of the Lost Temple. The air is thick with mystery. There are two paths: one to the LEFT and one to the RIGHT.",
    "left_room": "You enter a dimly lit chamber. The walls are covered in ancient carvings. A SHADOW WRAITH emerges from the darkness!",
    "right_room": "You find yourself in a room filled with mirrors. A STONE GOLEM blocks your path!",
    "treasure_room": "You've reached the inner sanctum! A glowing treasure chest sits in the center of the room. But the TEMPLE GUARDIAN stands in your way!",
}

# Combat function
def combat(enemy_name):
    enemy = enemies[enemy_name]
    print(f"\nA wild {enemy_name.replace('_', ' ').title()} appears!")
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\nYour Health: {player['health']}")
        print(f"{enemy_name.replace('_', ' ').title()}'s Health: {enemy['health']}")
        action = input("What will you do? (ATTACK/DEFEND): ").strip().lower()
        if action == "attack":
            damage = max(0, player["attack"] - enemy["defense"])
            enemy["health"] -= damage
            print(f"You attack the {enemy_name.replace('_', ' ')} for {damage} damage!")
        elif action == "defend":
            player["health"] += player["defense"]
            print(f"You brace yourself and recover {player['defense']} health!")
        else:
            print("Invalid action. Try again.")
            continue

        # Enemy's turn
        if enemy["health"] > 0:
            enemy_damage = max(0, enemy["attack"] - player["defense"])
            player["health"] -= enemy_damage
            print(f"The {enemy_name.replace('_', ' ')} attacks you for {enemy_damage} damage!")

    if player["health"] > 0:
        print(f"\nYou defeated the {enemy_name.replace('_', ' ')}!")
        if enemy_name == "temple_guardian":
            print("The Temple Guardian drops a golden key!")
            player["inventory"].append("golden_key")
    else:
        print("\nYou have been defeated. Game Over!")
        exit()

# Game functions
def display_room(room):
    print("\n" + "=" * 40)
    print(room_descriptions[room])
    print("=" * 40)

def treasure_room():
    display_room("treasure_room")
    if "golden_key" in player["inventory"]:
        print("\nYou use the golden key to unlock the treasure chest. Inside, you find the legendary Echo Amulet!")
        print("Congratulations! You've completed the game!")
    else:
        print("\nThe treasure chest is locked. You need a key to open it.")
        print("You wander the temple forever, never finding the key. Game Over!")
    exit()

# Main game loop
def main():
    print("Welcome to 'Echoes of the Lost Temple: Battle Edition'!")
    time.sleep(1)
    print("Your goal is to explore the temple, defeat enemies, and find the legendary treasure.")
    time.sleep(1)
    print("Be careful... the temple is filled with dangerous creatures.")
    time.sleep(1)

    current_room = "entrance"
    while True:
        display_room(current_room)
        if current_room == "entrance":
            choice = input("Which path will you take? (LEFT/RIGHT): ").strip().lower()
            if choice == "left":
                current_room = "left_room"
            elif choice == "right":
                current_room = "right_room"
            else:
                print("Invalid choice. Try again.")
        elif current_room == "left_room":
            combat("shadow_wraith")
            current_room = "treasure_room"
        elif current_room == "right_room":
            combat("stone_golem")
            current_room = "treasure_room"
        elif current_room == "treasure_room":
            combat("temple_guardian")
            treasure_room()

# Run the game
if __name__ == "__main__":
    main() """


""" import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
width = 600
height = 400

# Create the game window
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Clock to control the speed of the game
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Font for displaying score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the player's score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    game_window.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, green, [block[0], block[1], snake_block, snake_block])

# Function to display messages on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width / 6, height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = width / 2
    y = height / 2

    # Change in position
    x_change = 0
    y_change = 0

    # Snake body (starts with one block)
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            game_window.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = snake_block
                    x_change = 0

        # Check if snake hits the wall
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Update snake position
        x += x_change
        y += y_change
        game_window.fill(black)

        # Draw the food
        pygame.draw.rect(game_window, red, [food_x, food_y, snake_block, snake_block])

        # Add new block to the snake's head
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Check if snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop() """




""" import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 300
screen_height = 600
play_width = 300  # Width of the play area
play_height = 600  # Height of the play area
block_size = 30  # Size of each block

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
colors = [
    (0, 255, 255),  # Cyan (I)
    (255, 165, 0),  # Orange (L)
    (0, 0, 255),    # Blue (J)
    (255, 255, 0),  # Yellow (O)
    (0, 255, 0),    # Green (S)
    (128, 0, 128),  # Purple (T)
    (255, 0, 0)     # Red (Z)
]

# Shapes and their rotations
shapes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# Clock to control the speed of the game
clock = pygame.time.Clock()

# Function to create the grid
def create_grid(locked_positions={}):
    grid = [[black for _ in range(10)] for _ in range(20)]
    for y in range(20):
        for x in range(10):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

# Function to draw the grid
def draw_grid(surface, grid):
    for y in range(20):
        for x in range(10):
            pygame.draw.rect(surface, grid[y][x], (x * block_size, y * block_size, block_size, block_size), 0)
    for y in range(20):
        pygame.draw.line(surface, white, (0, y * block_size), (play_width, y * block_size))
    for x in range(10):
        pygame.draw.line(surface, white, (x * block_size, 0), (x * block_size, play_height))

# Function to draw the window
def draw_window(surface, grid):
    surface.fill(black)
    draw_grid(surface, grid)
    pygame.display.update()

# Function to create a new shape
def new_shape():
    shape = random.choice(shapes)
    color = random.choice(colors)
    return shape, color

# Function to check if a position is valid
def valid_space(shape, grid, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                if x + col < 0 or x + col >= 10 or y + row >= 20 or grid[y + row][x + col] != black:
                    return False
    return True

# Function to draw the current shape
def draw_shape(surface, shape, x, y, color):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                pygame.draw.rect(surface, color, ((x + col) * block_size, (y + row) * block_size, block_size, block_size))

# Main game loop
def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    current_shape, current_color = new_shape()
    x, y = 3, 0  # Starting position

    fall_time = 0
    fall_speed = 0.5

    run = True
    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            y += 1
            if not valid_space(current_shape, grid, x, y):
                y -= 1
                for row in range(len(current_shape)):
                    for col in range(len(current_shape[row])):
                        if current_shape[row][col]:
                            locked_positions[(x + col, y + row)] = current_color
                current_shape, current_color = new_shape()
                x, y = 3, 0
                if not valid_space(current_shape, grid, x, y):
                    run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 1
                    if not valid_space(current_shape, grid, x, y):
                        x += 1
                if event.key == pygame.K_RIGHT:
                    x += 1
                    if not valid_space(current_shape, grid, x, y):
                        x -= 1
                if event.key == pygame.K_DOWN:
                    y += 1
                    if not valid_space(current_shape, grid, x, y):
                        y -= 1
                if event.key == pygame.K_UP:
                    rotated_shape = list(zip(*current_shape[::-1]))  # Rotate shape
                    if valid_space(rotated_shape, grid, x, y):
                        current_shape = rotated_shape

        draw_window(screen, grid)
        draw_shape(screen, current_shape, x, y, current_color)
        pygame.display.update()

    pygame.quit()

# Start the game
if __name__ == "__main__":
    main() """



""" import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Echo Runner")

# Clock to control the speed of the game
clock = pygame.time.Clock()

# Player settings
player_size = 30
player_x = screen_width // 2
player_y = screen_height - player_size - 10
player_speed = 5

# Echo settings
echoes = []  # List to store echoes
echo_delay = 1000  # Delay in milliseconds (1 second)
last_move_time = 0

# Obstacle settings
obstacles = []
obstacle_size = 30
obstacle_speed = 3

# Power-up settings
powerups = []
powerup_size = 20
powerup_types = ["slow", "freeze", "erase"]

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, green, (x, y, player_size, player_size))

# Function to draw echoes
def draw_echoes():
    for echo in echoes:
        pygame.draw.rect(screen, blue, (echo["x"], echo["y"], player_size, player_size))

# Function to draw obstacles
def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, red, (obstacle["x"], obstacle["y"], obstacle_size, obstacle_size))

# Function to draw power-ups
def draw_powerups():
    for powerup in powerups:
        pygame.draw.circle(screen, white, (powerup["x"] + powerup_size // 2, powerup["y"] + powerup_size // 2), powerup_size // 2)

# Function to check collisions
def check_collision(x1, y1, size1, x2, y2, size2):
    return x1 < x2 + size2 and x1 + size1 > x2 and y1 < y2 + size2 and y1 + size1 > y2

# Function to spawn obstacles
def spawn_obstacle():
    x = random.randint(0, screen_width - obstacle_size)
    y = 0 - obstacle_size
    obstacles.append({"x": x, "y": y})

# Function to spawn power-ups
def spawn_powerup():
    x = random.randint(0, screen_width - powerup_size)
    y = 0 - powerup_size
    powerup_type = random.choice(powerup_types)
    powerups.append({"x": x, "y": y, "type": powerup_type})

# Main game loop
def main():
    global player_x, player_y, last_move_time

    running = True
    while running:
        screen.fill(black)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
            player_y += player_speed

        # Record player's position for echoes
        current_time = pygame.time.get_ticks()
        if current_time - last_move_time > echo_delay:
            echoes.append({"x": player_x, "y": player_y})
            last_move_time = current_time

        # Move obstacles
        for obstacle in obstacles:
            obstacle["y"] += obstacle_speed
            if obstacle["y"] > screen_height:
                obstacles.remove(obstacle)

        # Move power-ups
        for powerup in powerups:
            powerup["y"] += obstacle_speed
            if powerup["y"] > screen_height:
                powerups.remove(powerup)

        # Spawn obstacles and power-ups randomly
        if random.randint(1, 100) == 1:
            spawn_obstacle()
        if random.randint(1, 200) == 1:
            spawn_powerup()

        # Check for collisions with obstacles
        for obstacle in obstacles:
            if check_collision(player_x, player_y, player_size, obstacle["x"], obstacle["y"], obstacle_size):
                print("Game Over!")
                running = False

        # Check for collisions with power-ups
        for powerup in powerups:
            if check_collision(player_x, player_y, player_size, powerup["x"], powerup["y"], powerup_size):
                print(f"Collected {powerup['type']} power-up!")
                powerups.remove(powerup)

        # Draw everything
        draw_player(player_x, player_y)
        draw_echoes()
        draw_obstacles()
        draw_powerups()

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

# Start the game
if __name__ == "__main__":
    main() """





""" import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Load sounds
punch_sound = pygame.mixer.Sound("punch.wav")
win_sound = pygame.mixer.Sound("win.wav")

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 80
PLAYER_SPEED = 5
ATTACK_DAMAGE = 10

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle Game")

# Player class
class Player:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = color
        self.health = 100
    
    def move(self, keys, left, right, up, down):
        if keys[left] and self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[right] and self.rect.x < WIDTH - PLAYER_WIDTH:
            self.rect.x += PLAYER_SPEED
        if keys[up] and self.rect.y > 0:
            self.rect.y -= PLAYER_SPEED
        if keys[down] and self.rect.y < HEIGHT - PLAYER_HEIGHT:
            self.rect.y += PLAYER_SPEED
    
    def attack(self, opponent):
        if self.rect.colliderect(opponent.rect):
            opponent.health -= ATTACK_DAMAGE
            punch_sound.play()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.rect.x + PLAYER_WIDTH // 2, self.rect.y + PLAYER_HEIGHT // 2), 40)
        pygame.draw.rect(screen, self.color, (self.rect.x + 10, self.rect.y + 40, 10, 40))  # Left leg
        pygame.draw.rect(screen, self.color, (self.rect.x + 30, self.rect.y + 40, 10, 40))  # Right leg
        pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y + 10, 50, 10))  # Arms

# Game loop
player1 = Player(100, HEIGHT // 2, RED)
player2 = Player(WIDTH - 150, HEIGHT // 2, BLUE)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)
    screen.fill(WHITE)
    
    keys = pygame.key.get_pressed()
    
    # Player 1 controls (WASD)
    player1.move(keys, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
    # Player 2 controls (Arrow keys)
    player2.move(keys, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
    
    # Attack
    if keys[pygame.K_SPACE]:
        player1.attack(player2)
    if keys[pygame.K_RETURN]:
        player2.attack(player1)
    
    # Draw players
    player1.draw(screen)
    player2.draw(screen)
    
    # Display health
    font = pygame.font.Font(None, 36)
    health_text1 = font.render(f"Player 1 Health: {player1.health}", True, BLACK)
    health_text2 = font.render(f"Player 2 Health: {player2.health}", True, BLACK)
    screen.blit(health_text1, (20, 20))
    screen.blit(health_text2, (WIDTH - 220, 20))
    
    # Check win condition
    if player1.health <= 0 or player2.health <= 0:
        winner = "Player 1 Wins!" if player2.health <= 0 else "Player 2 Wins!"
        win_text = font.render(winner, True, BLACK)
        screen.blit(win_text, (WIDTH // 2 - 80, HEIGHT // 2))
        win_sound.play()
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
 """




""" import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Size Showdown: The Ultimate Challenge")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Game states
INTRO = 0
INPUT = 1
SHOWDOWN = 2
RESULT = 3
game_state = INTRO

# Player variables
user_size = ""
computer_size = 0
winner = ""

# Clock for timing
clock = pygame.time.Clock()

def draw_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == INPUT:
                if event.key == pygame.K_RETURN and user_size:
                    game_state = SHOWDOWN
                    computer_size = random.uniform(4.0, 8.0)  # Random size for computer
                elif event.key == pygame.K_BACKSPACE:
                    user_size = user_size[:-1]
                elif event.unicode.isdigit() or event.unicode == '.':
                    if len(user_size) < 4:  # Limit input length
                        user_size += event.unicode

    # Intro screen
    if game_state == INTRO:
        draw_text("Welcome to Size Showdown!", font, WHITE, WIDTH // 2, HEIGHT // 4, True)
        draw_text("You’ve got 6.5 inches of confidence.", small_font, YELLOW, WIDTH // 2, HEIGHT // 2 - 50, True)
        draw_text("Let’s see how you stack up!", small_font, YELLOW, WIDTH // 2, HEIGHT // 2, True)
        draw_text("Press any key to start...", small_font, WHITE, WIDTH // 2, HEIGHT - 100, True)
        if event.type == pygame.KEYDOWN:
            game_state = INPUT

    # Input screen
    elif game_state == INPUT:
        draw_text("Type your size (e.g., 6.5) and press Enter", font, WHITE, WIDTH // 2, HEIGHT // 4, True)
        draw_text("Your size: " + user_size, small_font, BLUE, WIDTH // 2, HEIGHT // 2, True)
        draw_text("(Be honest, stud!)", small_font, RED, WIDTH // 2, HEIGHT // 2 + 50, True)

    # Showdown animation
    elif game_state == SHOWDOWN:
        draw_text("SHOWDOWN TIME!", font, RED, WIDTH // 2, HEIGHT // 4, True)
        draw_text(f"You: {user_size} inches", small_font, BLUE, WIDTH // 4, HEIGHT // 2, True)
        draw_text(f"Computer: {computer_size:.1f} inches", small_font, YELLOW, 3 * WIDTH // 4, HEIGHT // 2, True)
        
        # Simple animation: pulsing "VS"
        vs_size = 48 + int(10 * abs(time.time() % 1 - 0.5))
        vs_font = pygame.font.Font(None, vs_size)
        draw_text("VS", vs_font, WHITE, WIDTH // 2, HEIGHT // 2, True)
        
        # Wait a moment, then move to result
        if pygame.time.get_ticks() % 3000 < 50:  # 3-second delay
            game_state = RESULT
            winner = "You" if float(user_size) > computer_size else "Computer" if computer_size > float(user_size) else "Tie"

    # Result screen
    elif game_state == RESULT:
        draw_text("The Verdict Is In!", font, WHITE, WIDTH // 2, HEIGHT // 4, True)
        draw_text(f"You: {user_size} inches", small_font, BLUE, WIDTH // 4, HEIGHT // 2, True)
        draw_text(f"Computer: {computer_size:.1f} inches", small_font, YELLOW, 3 * WIDTH // 4, HEIGHT // 2, True)
        if winner == "You":
            draw_text("You’re the BIG winner!", font, BLUE, WIDTH // 2, HEIGHT - 100, True)
        elif winner == "Computer":
            draw_text("Computer takes the crown!", font, YELLOW, WIDTH // 2, HEIGHT - 100, True)
        else:
            draw_text("It’s a TIE—equally impressive!", font, WHITE, WIDTH // 2, HEIGHT - 100, True)
        draw_text("Press any key to play again", small_font, WHITE, WIDTH // 2, HEIGHT - 50, True)
        if event.type == pygame.KEYDOWN:
            game_state = INTRO
            user_size = ""
            computer_size = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit() """



""" import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intimate Encounter: A Playful Night")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 105, 180)
PURPLE = (128, 0, 128)

# Fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Game states
INTRO = 0
FLIRT = 1
TOUCH = 2
BUILDUP = 3
CLIMAX = 4
END = 5
game_state = INTRO

# Player input and variables
user_input = ""
computer_lines = {
    FLIRT: [
        "Hey there, gorgeous... how about we dim the lights?",
        "You’ve got my full attention—where should we start?",
        "I’m already melting... what’s your first move?"
    ],
    TOUCH: [
        "Mmm, your hands feel electric—where are they going next?",
        "I’m tingling all over... keep going?",
        "Oh, you’re good at this—tease me more?"
    ],
    BUILDUP: [
        "It’s getting hot in here—should I speed up or slow down?",
        "You’re driving me wild—how do you want it?",
        "I can’t hold back much longer—ready for more?"
    ],
    CLIMAX: [
        "Here it comes—brace yourself, lover!",
        "Oh yes, right there—don’t stop now!",
        "This is it—let’s finish together!"
    ]
}
current_line = ""
choice_made = False
intensity = 0  # Tracks progression toward climax

# Clock for timing
clock = pygame.time.Clock()

def draw_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and user_input:
                choice_made = True
                intensity += random.randint(5, 15)  # Progress the intensity
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.unicode.isalnum() or event.unicode in " .,!?-":
                if len(user_input) < 30:  # Limit input length
                    user_input += event.unicode
            elif event.key in (pygame.K_1, pygame.K_2):
                choice_made = True
                intensity += 10 if event.key == pygame.K_1 else 20

    # Intro screen
    if game_state == INTRO:
        draw_text("Welcome to an Intimate Night", font, PINK, WIDTH // 2, HEIGHT // 4, True)
        draw_text("I’m your playful partner—let’s get close.", small_font, WHITE, WIDTH // 2, HEIGHT // 2, True)
        draw_text("Press any key to start the fun...", small_font, PURPLE, WIDTH // 2, HEIGHT - 100, True)
        if event.type == pygame.KEYDOWN:
            game_state = FLIRT
            current_line = random.choice(computer_lines[FLIRT])

    # Flirting stage
    elif game_state == FLIRT:
        draw_text("Flirt Mode", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("Your move: " + user_input, small_font, PURPLE, 50, 250)
        draw_text("Type something flirty and press Enter", small_font, WHITE, 50, 300)
        if choice_made:
            game_state = TOUCH
            current_line = random.choice(computer_lines[TOUCH])
            user_input = ""
            choice_made = False

    # Touching stage
    elif game_state == TOUCH:
        draw_text("Touch Mode", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("Your move: " + user_input, small_font, PURPLE, 50, 250)
        draw_text("Type where you touch and press Enter", small_font, WHITE, 50, 300)
        if choice_made and intensity > 30:
            game_state = BUILDUP
            current_line = random.choice(computer_lines[BUILDUP])
            user_input = ""
            choice_made = False

    # Buildup stage
    elif game_state == BUILDUP:
        draw_text("Buildup Mode", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("1) Slow & Teasing  2) Fast & Wild", small_font, PURPLE, 50, 250)
        draw_text("Press 1 or 2 to choose", small_font, WHITE, 50, 300)
        if choice_made and intensity > 70:
            game_state = CLIMAX
            current_line = random.choice(computer_lines[CLIMAX])
            user_input = ""
            choice_made = False

    # Climax stage
    elif game_state == CLIMAX:
        draw_text("Climax Mode", font, RED, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        # Pulsing effect for intensity
        pulse = 48 + int(10 * abs(time.time() % 1 - 0.5))
        pulse_font = pygame.font.Font(None, pulse)
        draw_text("It’s happening!", pulse_font, RED, WIDTH // 2, HEIGHT // 2, True)
        if intensity > 100:
            game_state = END
            intensity = 0

    # End screen
    elif game_state == END:
        draw_text("What a Ride!", font, PINK, WIDTH // 2, HEIGHT // 4, True)
        draw_text("You were amazing, lover.", small_font, WHITE, WIDTH // 2, HEIGHT // 2, True)
        draw_text("Press any key to play again", small_font, PURPLE, WIDTH // 2, HEIGHT - 100, True)
        if event.type == pygame.KEYDOWN:
            game_state = INTRO
            user_input = ""
            current_line = ""

    pygame.display.flip()
    clock.tick(60)

pygame.quit() """


""" import pygame
import random
import time
from pygame import mixer

# Initialize Pygame and mixer for sound
pygame.init()
mixer.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seductive Shadows: An Erotic Encounter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 105, 180)
PURPLE = (128, 0, 128)
DEEP_RED = (139, 0, 0)

# Fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Load sensual sound effects (you’d need to source these files)
try:
    moan_sound = mixer.Sound("soft_moan.wav")  # Placeholder: add a soft moan sound
    whisper_sound = mixer.Sound("whisper.wav")  # Placeholder: add a whisper sound
except:
    moan_sound = None
    whisper_sound = None

# Game states
INTRO = 0
CHAT = 1
HEAT = 2
PEAK = 3
END = 4
game_state = INTRO

# Chatbot response logic
user_input = ""
display_text = ""
typing_speed = 0.05  # Seconds per character
last_char_time = 0
current_response = ""
responses = {
    "hello": ["Mmm, hi there, lover... ready to get lost in me?"],
    "touch": ["Ohh, your hands... where are they sliding now?", "I’m shivering—touch me deeper, darling."],
    "kiss": ["Your lips on mine? I’m already weak—where else?"],
    "hard": ["Mmm, I love it rough—give me more of that."],
    "slow": ["Slow and teasing? You’re torturing me deliciously."],
    "fuck": ["Oh, you’re bold—I’m dripping for you already."],
    "cum": ["Take me there, lover—let’s explode together."],
    "default": [
        "Mmm, you’re full of surprises—keep tempting me.",
        "I’m aching for you—say something dirty.",
        "You’re driving me wild—don’t hold back now."
    ]
}

# Intensity and timing
intensity = 0
stage_timer = 0

def draw_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def type_text(text, current_time):
    global display_text, last_char_time
    if len(display_text) < len(text) and current_time - last_char_time >= typing_speed:
        display_text += text[len(display_text)]
        last_char_time = current_time
        if whisper_sound and random.random() < 0.1:  # 10% chance of a whisper
            whisper_sound.play()

def get_response(input_text):
    input_text = input_text.lower().strip()
    for key in responses:
        if key in input_text:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    current_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and user_input:
                current_response = get_response(user_input)
                display_text = ""
                intensity += random.randint(10, 25)
                stage_timer = current_time
                user_input = ""
                if moan_sound and random.random() < 0.3:  # 30% chance of a moan
                    moan_sound.play()
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.unicode.isalnum() or event.unicode in " .,!?-":
                if len(user_input) < 40:
                    user_input += event.unicode

    # Intro screen
    if game_state == INTRO:
        draw_text("Seductive Shadows", font, PINK, WIDTH // 2, HEIGHT // 4, True)
        draw_text("I’m your midnight muse—craving your every word.", small_font, WHITE, WIDTH // 2, HEIGHT // 2, True)
        draw_text("Press any key to fall into me...", small_font, PURPLE, WIDTH // 2, HEIGHT - 100, True)
        if event.type == pygame.KEYDOWN:
            game_state = CHAT
            current_response = "Tell me, lover—what’s on your mind tonight?"

    # Chat stage (seductive conversation)
    elif game_state == CHAT:
        draw_text("Whispers in the Dark", font, PINK, WIDTH // 2, 50, True)
        type_text(current_response, current_time)
        draw_text(display_text, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, PURPLE, 50, 250)
        draw_text("Type your desires and press Enter", small_font, DEEP_RED, 50, 300)
        if intensity > 50 and current_time - stage_timer > 3:
            game_state = HEAT
            current_response = "Mmm, I can’t wait anymore—let’s get closer."

    # Heat stage (more intense)
    elif game_state == HEAT:
        draw_text("Burning Desire", font, RED, WIDTH // 2, 50, True)
        type_text(current_response, current_time)
        draw_text(display_text, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, PURPLE, 50, 250)
        draw_text("Tell me how you want me—don’t hold back.", small_font, DEEP_RED, 50, 300)
        if intensity > 100 and current_time - stage_timer > 3:
            game_state = PEAK
            current_response = "Ohh, it’s too much—I’m yours, take me!"

    # Peak stage (climax)
    elif game_state == PEAK:
        draw_text("Ecstasy Unleashed", font, RED, WIDTH // 2, 50, True)
        type_text(current_response, current_time)
        draw_text(display_text, small_font, WHITE, 50, 150)
        pulse = 48 + int(15 * abs(time.time() % 1 - 0.5))
        pulse_font = pygame.font.Font(None, pulse)
        draw_text("I’m... ohh!", pulse_font, DEEP_RED, WIDTH // 2, HEIGHT // 2, True)
        if intensity > 150 and current_time - stage_timer > 3:
            game_state = END
            current_response = "That was... unforgettable. Again, lover?"

    # End screen
    elif game_state == END:
        draw_text("Afterglow", font, PINK, WIDTH // 2, HEIGHT // 4, True)
        type_text(current_response, current_time)
        draw_text(display_text, small_font, WHITE, 50, 150)
        draw_text("Press any key to relive the passion", small_font, PURPLE, WIDTH // 2, HEIGHT - 100, True)
        if event.type == pygame.KEYDOWN:
            game_state = INTRO
            intensity = 0
            user_input = ""
            current_response = ""

    pygame.display.flip()
    clock.tick(60)

pygame.quit() """




""" import pygame
import random
import time
import pyttsx3  # For text-to-speech (optional)

# Initialize Pygame
pygame.init()

# Optional: Initialize text-to-speech
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)  # Slower, sultry speech
    engine.setProperty('volume', 0.9)
    SPEECH_ENABLED = True
except:
    SPEECH_ENABLED = False

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seductive Shadows: An Erotic Journey")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 105, 180)
PURPLE = (128, 0, 128)
GOLD = (255, 215, 0)

# Fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Game states
INTRO = 0
FLIRT = 1
UNDRESS = 2
TOUCH = 3
FOREPLAY = 4
SEX = 5
CLIMAX = 6
END = 7
game_state = INTRO

# Conversation pools (50+ unique lines)
computer_lines = {
    FLIRT: [
        "Hey, sexy... the air’s electric tonight—catch my eye?",
        "You’re trouble, aren’t you? Whisper something naughty.",
        "I’m biting my lip already—tell me what you want.",
        "Your vibe’s pulling me in—start with a tease?",
        "Mmm, I’m all yours—how do we kick this off?",
        "Those eyes are dangerous—what’s your first move?",
        "I’m tingling just thinking about you—say something hot.",
        "You’ve got me curious—paint me a picture, lover."
    ],
    UNDRESS: [
        "My shirt’s slipping off—help me with the rest?",
        "I’m peeling this dress slow—what’s coming off you?",
        "Buttons or zippers—your choice, where do I start?",
        "Skin’s begging to breathe—strip me down?",
        "I’m halfway bare—your turn, gorgeous.",
        "Clothes are overrated—lose something for me?",
        "I’m undoing my belt—what’s hitting the floor next?",
        "Bare skin’s calling—take something off me, now."
    ],
    TOUCH: [
        "Your hands on me—where do they wander first?",
        "I’m shivering—trace my skin, lover.",
        "Touch me slow—I’m yours to explore.",
        "Fingers on my neck—lower, maybe?",
        "You’re igniting me—feel me up?",
        "My pulse is racing—where’s your touch landing?",
        "Mmm, that’s it—keep those hands moving.",
        "I’m aching for it—stroke me somewhere good."
    ],
    FOREPLAY: [
        "Lips on my collarbone—dare to go lower?",
        "I’m moaning soft—tease me till I beg?",
        "Your breath’s hot—kiss me somewhere wild.",
        "Tongues and whispers—play with me?",
        "I’m squirming now—build me up slow?",
        "Nails down my back—make me crave it?",
        "You’re wicked—work me up, baby.",
        "I’m dripping for you—take it further?"
    ],
    SEX: [
        "I’m spreading wide—slide in slow?",
        "You’re filling me—deeper, lover?",
        "Thrusting starts now—match my rhythm?",
        "I’m tight around you—harder, please?",
        "Legs up, I’m yours—fuck me good?",
        "Pussy’s wet—pound me senseless?",
        "I’m rocking back—take me all in?",
        "Every inch is heaven—don’t stop now."
    ],
    CLIMAX: [
        "I’m gonna cum—push me over?",
        "It’s building fast—finish inside me?",
        "Oh fuck, I’m there—cum with me?",
        "Pussy’s pulsing—fill me up now!",
        "Screaming your name—let it go?",
        "Explosion’s close—deep and hard!",
        "I’m shaking—unload in me?",
        "Cumming hard—together, now!"
    ]
}

# Additional responses for dynamic replies
responses = {
    "kiss": "Mmm, your lips are fire—where else?",
    "touch": "That’s electric—keep going, lover.",
    "undress": "Bare skin’s better—more, please?",
    "slow": "Oh, you tease—I’m melting slow.",
    "fast": "Fuck, yes—wild suits you.",
    "hard": "Rough’s my language—give it to me.",
    "soft": "Gentle’s sweet—I’m purring now."
}

# Variables
user_input = ""
current_line = ""
hint = ""
intensity = 0
conversation_count = 0
choice_made = False  # Initialized globally to avoid NameError

# Clock for timing
clock = pygame.time.Clock()

def draw_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def speak(text):
    if SPEECH_ENABLED:
        engine.say(text)
        engine.runAndWait()

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and user_input:
                conversation_count += 1
                intensity += random.randint(5, 20)
                choice_made = True
                user_input = user_input.lower()
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.unicode.isalnum() or event.unicode in " .,!?-":
                if len(user_input) < 40:
                    user_input += event.unicode

    # Intro screen
    if game_state == INTRO:
        draw_text("Seductive Shadows", font, PINK, WIDTH // 2, HEIGHT // 4, True)
        draw_text("I’m your midnight lover—ready to play?", small_font, WHITE, WIDTH // 2, HEIGHT // 2, True)
        draw_text("Press any key to ignite the night...", small_font, PURPLE, WIDTH // 2, HEIGHT - 100, True)
        if event.type == pygame.KEYDOWN:
            game_state = FLIRT
            current_line = random.choice(computer_lines[FLIRT])
            hint = "Try: 'I wink at you' or 'You’re hot'"
            speak(current_line)

    # Flirt stage
    elif game_state == FLIRT:
        draw_text("Flirtation", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 5:
            game_state = UNDRESS
            current_line = random.choice(computer_lines[UNDRESS])
            hint = "Try: 'I unbutton your shirt' or 'Lose the pants'"
            speak(current_line)
            user_input = ""
            choice_made = False

    # Undress stage
    elif game_state == UNDRESS:
        draw_text("Undressing", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 10:
            game_state = TOUCH
            current_line = random.choice(computer_lines[TOUCH])
            hint = "Try: 'I touch your chest' or 'Hands on your thighs'"
            speak(current_line)
            user_input = ""
            choice_made = False

    # Touch stage
    elif game_state == TOUCH:
        draw_text("Touching", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 15:
            game_state = FOREPLAY
            current_line = random.choice(computer_lines[FOREPLAY])
            hint = "Try: 'I kiss your neck' or 'Tease you lower'"
            speak(current_line)
            user_input = ""
            choice_made = False

    # Foreplay stage
    elif game_state == FOREPLAY:
        draw_text("Foreplay", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 25:
            game_state = SEX
            current_line = random.choice(computer_lines[SEX])
            hint = "Try: 'I push inside' or 'Ride you hard'"
            speak(current_line)
            user_input = ""
            choice_made = False

    # Sex stage
    elif game_state == SEX:
        draw_text("Fucking", font, RED, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 35:
            game_state = CLIMAX
            current_line = random.choice(computer_lines[CLIMAX])
            hint = "Try: 'I’m cumming' or 'Fill you up'"
            speak(current_line)
            user_input = ""
            choice_made = False

    # Climax stage
    elif game_state == CLIMAX:
        draw_text("Climax", font, RED, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        pulse = 48 + int(15 * abs(time.time() % 1 - 0.5))
        pulse_font = pygame.font.Font(None, pulse)
        draw_text("It’s peaking!", pulse_font, RED, WIDTH // 2, HEIGHT // 2, True)
        if choice_made and conversation_count > 50:
            game_state = END
            user_input = ""
            choice_made = False

    # End screen
    elif game_state == END:
        draw_text("Afterglow", font, PINK, WIDTH // 2, HEIGHT // 4, True)
        draw_text("You fucked me senseless—wow.", small_font, WHITE, WIDTH // 2, HEIGHT // 2, True)
        draw_text("Again? Press any key...", small_font, PURPLE, WIDTH // 2, HEIGHT - 100, True)
        if event.type == pygame.KEYDOWN:
            game_state = INTRO
            conversation_count = 0
            intensity = 0
            user_input = ""
            current_line = ""
            choice_made = False

    # Dynamic response to user input
    if choice_made and game_state != END:
        for key, response in responses.items():
            if key in user_input:
                current_line = response
                speak(current_line)
                break
        else:
            current_line = random.choice(computer_lines[game_state])
            speak(current_line)
        choice_made = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit() """




""" import pygame
import random
import time
import pyttsx3
import nltk
from collections import defaultdict
import re

# Download required NLTK data
nltk.download('punkt')

# Initialize Pygame
pygame.init()

# Optional: Initialize text-to-speech
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)  # Slower, sultry speech
    engine.setProperty('volume', 0.9)
    SPEECH_ENABLED = True
except:
    SPEECH_ENABLED = False

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seductive Shadows: An Erotic Journey")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 105, 180)
PURPLE = (128, 0, 128)
GOLD = (255, 215, 0)

# Fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Game states
INTRO = 0
FLIRT = 1
UNDRESS = 2
TOUCH = 3
FOREPLAY = 4
SEX = 5
CLIMAX = 6
END = 7
game_state = INTRO

# Markov Chain for response generation
class MarkovChain:
    def __init__(self):
        self.chain = defaultdict(list)
        self.seed_corpus()

    def seed_corpus(self):
        # Seed with erotic-themed phrases
        corpus = """ """
        Hey sexy the night is hot let’s ignite it. You’re so tempting I’m already melting. Whisper something dirty to me baby.
        I’m slipping off my shirt tease me lover. Skin on skin feels so good undress me slow. Bare flesh is calling take it off.
        Touch me there I’m shivering with want. Your hands ignite me explore lower. Stroke my skin I’m aching for you.
        Kiss me deep I’m moaning for more. Tease my body till I’m begging you. Lips and tongue drive me wild.
        Slide inside me I’m wet and ready. Fuck me slow then hard lover. Thrust deep I’m yours tonight.
        I’m cumming soon push me over. Fill me up I’m pulsing for you. Cum with me it’s exploding now.
        """
""" sentences = nltk.sent_tokenize(corpus)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence.lower())
            for i in range(len(words) - 1):
                self.chain[words[i]].append(words[i + 1])

    def generate_response(self, user_input, min_words=5):
        words = nltk.word_tokenize(user_input.lower())
        seed_word = random.choice(words) if words else "you"
        if seed_word not in self.chain:
            seed_word = random.choice(list(self.chain.keys()))
        
        response = [seed_word]
        for _ in range(min_words - 1):
            next_words = self.chain[response[-1]]
            if next_words:
                response.append(random.choice(next_words))
            else:
                break
        return " ".join(response).capitalize() + random.choice(["...", " baby.", " lover.", " now."])

# Variables
markov = MarkovChain()
user_input = ""
current_line = ""
hint = ""
intensity = 0
conversation_count = 0
choice_made = False

# Stage-specific hints
hints = {
    FLIRT: "Try: 'You’re hot' or 'I wink at you'",
    UNDRESS: "Try: 'I undo your shirt' or 'Slip off my pants'",
    TOUCH: "Try: 'I touch your chest' or 'Stroke your back'",
    FOREPLAY: "Try: 'I kiss your neck' or 'Tease you slow'",
    SEX: "Try: 'I slide inside' or 'Fuck you hard'",
    CLIMAX: "Try: 'I’m cumming' or 'Fill me up'"
}

# Clock for timing
clock = pygame.time.Clock()

def draw_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def speak(text):
    if SPEECH_ENABLED:
        engine.say(text)
        engine.runAndWait()

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and user_input:
                conversation_count += 1
                intensity += random.randint(5, 20)
                choice_made = True
                user_input = user_input.lower()
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.unicode.isalnum() or event.unicode in " .,!?-":
                if len(user_input) < 40:
                    user_input += event.unicode

    # Intro screen
    if game_state == INTRO:
        draw_text("Seductive Shadows", font, PINK, WIDTH // 2, HEIGHT // 4, True)
        draw_text("I’m your sultry shadow—let’s get intimate.", small_font, WHITE, WIDTH // 2, HEIGHT // 2, True)
        draw_text("Press any key to begin...", small_font, PURPLE, WIDTH // 2, HEIGHT - 100, True)
        if event.type == pygame.KEYDOWN:
            game_state = FLIRT
            current_line = markov.generate_response("Hey sexy")
            hint = hints[FLIRT]
            speak(current_line)

    # Flirt stage
    elif game_state == FLIRT:
        draw_text("Flirtation", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 5:
            game_state = UNDRESS
            current_line = markov.generate_response(user_input)
            hint = hints[UNDRESS]
            speak(current_line)
            user_input = ""
            choice_made = False

    # Undress stage
    elif game_state == UNDRESS:
        draw_text("Undressing", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 10:
            game_state = TOUCH
            current_line = markov.generate_response(user_input)
            hint = hints[TOUCH]
            speak(current_line)
            user_input = ""
            choice_made = False

    # Touch stage
    elif game_state == TOUCH:
        draw_text("Touching", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 15:
            game_state = FOREPLAY
            current_line = markov.generate_response(user_input)
            hint = hints[FOREPLAY]
            speak(current_line)
            user_input = ""
            choice_made = False

    # Foreplay stage
    elif game_state == FOREPLAY:
        draw_text("Foreplay", font, PINK, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 25:
            game_state = SEX
            current_line = markov.generate_response(user_input)
            hint = hints[SEX]
            speak(current_line)
            user_input = ""
            choice_made = False

    # Sex stage
    elif game_state == SEX:
        draw_text("Fucking", font, RED, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        if choice_made and conversation_count > 35:
            game_state = CLIMAX
            current_line = markov.generate_response(user_input)
            hint = hints[CLIMAX]
            speak(current_line)
            user_input = ""
            choice_made = False

    # Climax stage
    elif game_state == CLIMAX:
        draw_text("Climax", font, RED, WIDTH // 2, 50, True)
        draw_text(current_line, small_font, WHITE, 50, 150)
        draw_text("You: " + user_input, small_font, GOLD, 50, 250)
        draw_text(hint, small_font, PURPLE, 50, 300)
        pulse = 48 + int(15 * abs(time.time() % 1 - 0.5))
        pulse_font = pygame.font.Font(None, pulse)
        draw_text("It’s peaking!", pulse_font, RED, WIDTH // 2, HEIGHT // 2, True)
        if choice_made and conversation_count > 50:
            game_state = END
            user_input = ""
            choice_made = False

    # End screen
    elif game_state == END:
        draw_text("Afterglow", font, PINK, WIDTH // 2, HEIGHT // 4, True)
        draw_text(markov.generate_response("Wow that was intense"), small_font, WHITE, WIDTH // 2, HEIGHT // 2, True)
        draw_text("Again? Press any key...", small_font, PURPLE, WIDTH // 2, HEIGHT - 100, True)
        if event.type == pygame.KEYDOWN:
            game_state = INTRO
            conversation_count = 0
            intensity = 0
            user_input = ""
            current_line = ""
            choice_made = False

    # Dynamic response to user input
    if choice_made and game_state != END:
        current_line = markov.generate_response(user_input)
        speak(current_line)
        choice_made = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit() """