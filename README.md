🛳️ Bataille Navale

Un petit jeu de Bataille Navale en mode texte, programmé en Python. Le joueur joue contre une grille fixe dans laquelle les navires sont pré-positionnés. Le but est de trouver et couler tous les navires en tirant sur les bonnes coordonnées.

🎯 Objectif du Jeu

Le joueur entre des coordonnées de tir (par exemple : B2, E5, etc.).

Le programme indique si le tir est :

Touché

Coulé (si toutes les cases du navire sont atteintes)

À l’eau (manqué)

Une grille est affichée à chaque tir, indiquant :

X pour une case touchée

~ pour un tir raté

🧱 Grille de Départ

Grille de taille 10x10, colonnes de A à J, lignes de 1 à 10.

| Nom du navire     | Taille | Position             |
| ----------------- | ------ | -------------------- |
| Porte-avion       | 5      | B2 → F2 (horizontal) |
| Croiseur          | 3      | A4 → A6 (vertical)   |
| Contre-torpilleur | 2      | C5 → C7 (vertical)   |
| Sous-marin        | 3      | H5 → J5 (horizontal) |
| Torpilleur        | 2      | E9 → F9 (horizontal) |

🕹️ Fonctionnement du Jeu

Le programme affiche une grille vide.

Il demande une coordonnée de tir (ex : C5, H1, etc.).

Il indique si le tir :

Touche un navire

Coule un navire

Rate

Le jeu continue jusqu’à ce que tous les navires soient coulés.

La grille se met à jour après chaque tir.


Pré-requis

Python 3.13

Lancer le script : python battleship.py

🧠 À savoir

Le placement des navires est fixe (non aléatoire).

Le joueur tire à l’infini jusqu’à couler tous les navires.

Le programme valide les coordonnées pour éviter les erreurs.

Affichage visuel clair pour bien distinguer les tirs.

✅ Légende des symboles
Symbole	Signification
X	Tir ayant touché un navire
~	Tir raté (à l’eau)
.	Case non encore découverte

🚀 Améliorations possibles

Ajouter des navires placés aléatoirement
