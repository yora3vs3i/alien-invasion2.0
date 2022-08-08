import pygame
from pygame.sprite import Group
from bullet import Bullet
from settings import Settings   
from game_stats import GameStatistics
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize pygame, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion by Walter")

    play_button = Button(ai_settings, screen, "Play")

    #create an instance to store game settings
    stats = GameStatistics(ai_settings)

    #make a ship, group of bullets and group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the mwain loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
run_game()
   