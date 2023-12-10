

# Importing the necessary modules for the game
import pygame
import random
import os

# Importing the arrow keys from the pygame module
from pygame.locals import (
    K_UP,
    K_LEFT,
    K_RIGHT,
)

# Storing the score in an external .txt file
highest_score = 0
file_highest_score = "score.txt"

# Defining the number of bullets that have been fired so far
bullets_fired = 0


# Defining the class for balloon
class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # The radius of the balloon will be a random number between 5 and 20
        self.radius = random.randint(5, 20)
        # The balloon will be the shape of a circle
        self.surf = pygame.Surface((2 * self.radius, 2 * self.radius))
        # The balloon will spawn at any position at the top of the screen
        self.x = random.randint(0, 800)
        self.y = 0
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        # The balloon color will be randomly chosen
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        # Now, the balloon is drawn on the screen
        pygame.draw.circle(self.surf, (self.r, self.g, self.b), (self.radius, self.radius), self.radius)

    # The shape will move at a given speed, and when the sheep reaches the end of the board it resets to a random x
    # position back at the top
    def update(self, speed):
        self.speed = speed
        self.rect.move_ip(0, self.speed)
        if self.rect.y > 550:
            self.rect.y = 0
            self.rect.x = random.randint(0, 800)


# Making the class to do the process for the gun
class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # The gun starts at the coordinates (75,75), which is the center of the screen
        self.surf = pygame.Surface((75, 75))
        # The image of the gun (stored locally) is converted to fit the screen
        self.surf = pygame.image.load("gun-small.png").convert()
        self.x = 400
        self.y = 550
        self.rect = self.surf.get_rect(center=(self.x, self.y))

    # The function to draw this gun on the board
    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    # The gun will move left or right 10 pixels every time this function runs
    def update(self, isLeft):
        if isLeft and self.x > 10:
            self.x = self.x - 10
            self.rect.move_ip(-10, 0)
        # If the gun's x value is more than 780 or less than 10 pixels it will stop
        elif not isLeft and self.x < 780:
            self.x = self.x + 10
            self.rect.move_ip(10, 0)


# The class for the bullet is defined
class Bullet(pygame.sprite.Sprite):
    def __init__(self, startx, starty):
        # The given variables startx and starty tell the starting position of the bullet
        self.x = startx
        self.y = starty
        # The bullet moves 15 pixels every time the function runs
        self.speed = 15
        super().__init__()
        # The bullet image (stored locally) is converted to fit the screen
        self.surf = pygame.Surface((20, 20))
        self.surf = pygame.image.load("bullet-small.png").convert()
        self.rect = self.surf.get_rect(center=(self.x, self.y))

    # The bullet is drawn on the screen
    def draw(self, screen):
        screen.blit(self.surf, self.rect)
    # The function to make the bullet move 15 pixels per time it is run

    def update(self):
        self.y = self.y - self.speed
        self.rect.move_ip(0, -self.speed)
        # If the bullet reaches the top of the screen, then it die
        if self.y < 0:
            return True
        # If the bullet doesn't reach the top, it will disappear
        else:
            return False


# The score will be stored in a variable. This variable will be called later to be shown on the board.
def store_score(score):
    f = open(file_highest_score, 'w')
    f.write(str(score))
    f.close()


# The display size is set, and the title is set to "Balloon Shooter"
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Balloon Shooter")
running = True
clock = pygame.time.Clock()


# If there is a file that the score needs to be stored in, this code reads that file, and stores the variable.
if os.path.exists(file_highest_score):
    f = open(file_highest_score)
    highest_score = int(f.read())
    f.close()

# The game level is set to 1
game_level = 1

# These are 2 custom defined userevents that count seconds and the time left before the next level
LEVEL_TIME_LEFT = pygame.USEREVENT + 1
pygame.time.set_timer(LEVEL_TIME_LEFT, 30000)
COUNT_SECS = pygame.USEREVENT + 2
pygame.time.set_timer(COUNT_SECS, 1000)

# The time the game has been played for is set to 0
game_time_secs = 0
# The font for the game is sent to freesansbold
myfont = pygame.font.Font("freesansbold.ttf", 20)

# The bullet and balloon sprites are grouped
bullet_sprites = pygame.sprite.Group()
balloon_sprites = pygame.sprite.Group()

# The player's score is set to 0
score = 0

# For every number between 0 and 10 add a balloon to the balloon group. This essentially adds 10 balloons to the group.
for x in range(0, 10):
    b = Balloon()
    balloon_sprites.add(b)

# Define a variable named gun that calls the gun function
gun = Gun()

# The welcome sign, which tells the high score, is shown
show_welcome_screen = True
x = 7
y = 10
# A random speed is set
random_speed = random.randint(x, y)
print(random_speed)

# This is the main function. Everything that occurs on the board is written here. All the functions are called here too.
while running:
    # Checks if the welcome screen is currently being shown
    if show_welcome_screen:
        # This for loop checks if the user wants to quit. If they do, it exits the game safely.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # When the up key is pressed, then the welcome screen disappears
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            show_welcome_screen = False
        # The screen background is set to be black
        screen.fill((0, 0, 0))
        # This is the welcome screen. It wlecome the user to the game, and tells them the high score. It is centered.
        mytext = myfont.render("Welcome to Balloon Shooter. Last high score: %d" % highest_score, True, (255, 0, 0))
        mytext_rect = mytext.get_rect(center=(400, 300))
        screen.blit(mytext, mytext_rect)
    # If the welcome screen is not being shown currently
    else:
        # For each event that is caused by the user
        for event in pygame.event.get():
            # This for loop checks if the user wants to quit. If they do, it exits the game safely.
            if event.type == pygame.QUIT:
                running = False
                # If this score is higher than the locally stored highest score, it replaces the highest score text
                if score > highest_score:
                    store_score(score)
            # This counts the seconds and displays them
            elif event.type == COUNT_SECS:
                game_time_secs = game_time_secs + 1
            # This whole statement is used to move on to the next level after a certain amount of time
            elif event.type == LEVEL_TIME_LEFT:
                if score >= 50:
                    game_level = game_level + 1
                    bullets_fired = 0
                    game_time_secs = 0
                    x = x+3
                    y = y+3
                    random_speed = random.randint(x, y)
                else:
                    game_level = game_level
                    bullets_fired = 0
                    game_time_secs = 0
        # If the left key gets pressed, move the gun left (set gun upfate true),
        # and if the right key is pressed move the gun right (set gun update false)
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            gun.update(True)
        if keys[K_RIGHT]:
            gun.update(False)
        # If the up key is pressed, increase the bullets fired by one, and call the bullet function.
        if keys[K_UP]:
            b = Bullet(gun.x, gun.y)
            bullet_sprites.add(b)
            bullets_fired = bullets_fired + 1
        screen.fill((0, 0, 0))
        gun.draw(screen)
        # For every value in the bullets group, draw that bullet on the screen
        for b in bullet_sprites:
            b.draw(screen)
            b.update()
        # For every value in the balloon group, assign a speed to that bullet and then place that balloon on the screen
        for balloon in balloon_sprites:
            balloon.update(random_speed)
            screen.blit(balloon.surf, balloon.rect)
        # For every value in the bullets group
        for bullet in bullet_sprites:
            # Check if any sprites have collided with one another on the screen
            collided_balloon = pygame.sprite.spritecollideany(bullet, balloon_sprites)
            # If the sprites have collided, increase the score by one and remove that balloon from that screen
            if collided_balloon is not None:
                score = score + 1
                collided_balloon.kill()
                b = Balloon()
                balloon_sprites.add(b)
        # Have text stating the time, level, number of bullets shot, and score in the color red
        myscoretext = myfont.render("time=%d, level=%d, bullets shot=%d, score=%d" % (game_time_secs, game_level, bullets_fired, score), True, (255, 0, 0))
        # Have this text in the corner of the screen
        myscoretext_rect = myscoretext.get_rect(center=(560, 20))
        screen.blit(myscoretext, myscoretext_rect)
    # Update the display
    pygame.display.flip()
    # Count 30 milliseconds before running this loop again.
    clock.tick(30)
