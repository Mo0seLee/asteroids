# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
import player
import asteroid
import asteroidfield
import shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # players
    player.Player.containers = (updateable, drawable)
    my_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # asteroids
    asteroid.Asteroid.containers = (asteroids, updateable, drawable)
    
    # asteroidfields
    asteroidfield.AsteroidField.containers = (updateable)
    asteroid_1 = asteroidfield.AsteroidField()

    # shots
    shot.Shot.containers = (shots, updateable, drawable)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updateable.update(dt)
        
        for ast in asteroids:
            if ast.is_colliding(my_player):
                sys.exit("Game over!")

        for ast in asteroids:
            for bullet in shots:
                if ast.is_colliding(bullet):
                    ast.split()
                    bullet.kill()

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
