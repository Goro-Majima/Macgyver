# Macgyver escape game

Dans le cadre de ce projet, j’ai pour but de créer un jeu de labyrinthe en 2D où Macgyver doit s'en échapper. Il doit pour cela ramasser des objets pour endormir un gardien qui bloque la sortie. 

Cela peut paraître facile car ce jeu est d’apparence simple, mais la conception demande une certaine technique et architecture qui seront déployées méthodiquement. J’ai opté pour l’approche en programmation objet.  J’ai eu pendant le projet quelques blocages dus à un algorithme pas assez complet ou encore des variables non définies. Mais ce que je retiendrai est surtout le moment de joie quand je trouve finalement la solution à mon cas.
Ce projet est développé avec Sublime text 3 sous Windows 10, versionné sur github et respecte les recommandations de la PEP8.

## Version de python

Python 3.7

Pygame 

## Structure du programme:

escape.py: Fichier qui organise la structure et le déroulement du programme.

classes.py: Emplacement des classes et des fonctions créés pour apporter plus de clarté.

        Classes : Level(fonctions create, build) : pour la création du niveau 
                  Stargate(fonction moveto) : pour créér et positionner les mouvements de Macgyver.
                  Items(fonctions shuffle, showobjects) pour afficher les objets de manière aléatoire et les faire disparaître dans le jeu.

Constants.py:  Définition des constantes telles que les titres, dimensions, images afin de pouvoir les utiliser/modifier plus simplement.  

Images: stockage des images qui représentent visuellement le jeu

Maze: fichier qui représente le labyrinthe en format .txt.
