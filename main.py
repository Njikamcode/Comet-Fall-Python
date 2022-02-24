import pygame
import math
from game import Game

pygame.init()

# générer la fenêtre de notre jeu
pygame.display.set_caption("Monster and The Comet Fall ")
screen = pygame.display.set_mode((1080, 720))

# Importer charger l'arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

# importer charger la banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# impoter ou charger le bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencé ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verfier si le jeu n'a pas commencé
    else:
        # ajouter l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    print(game.player.rect.x)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'évenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # détecter si un joueur enclenche une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.start()
