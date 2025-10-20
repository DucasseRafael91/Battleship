#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def create_ships():
    """
       Créer les différents bateaux
       :return: liste de bateaux
    """
    boats = []

    # Porte-avions (B2 à F2) : ligne 1, colonnes 1-5
    aircraft = [(1, col) for col in range(1, 6)]
    boats.append(aircraft)

    # Croiseur (A4 à A7)
    cruiser = [(row, 0) for row in range(3, 7)]
    boats.append(cruiser)

    # Contre-torpilleur (C5 à E5)
    destroyer = [(row, 2) for row in range(4, 7)]
    boats.append(destroyer)

    # Sous-marin (H5 à J5)
    submarine = [(4, col) for col in range(7, 10)]
    boats.append(submarine)

    # Torpilleur (E9 à F9)
    torpedo_boat = [(8, col) for col in range(4, 6)]
    boats.append(torpedo_boat)

    return boats

def create_empty_grid():
    """
        Créer la zone de jeu de 10 par 10 avec Numpy
       :return: grille de jeu
    """
    return np.full((10, 10), " ", dtype=str)

def print_grid(grid):
    """
        Affiche la zone de jeu avec Numpy
        :param grid: grille de jeu
        :return: grille de jeu
    """
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("   +" + "---+" * 10)
    print("   | " + " | ".join(letters) + " |")
    print("   +" + "---+" * 10)

    for row_num in range(10):
        row_display = f"{row_num + 1:<2} |"
        for col in range(10):
            row_display += f" {grid[row_num, col]} |"
        print(row_display)
        print("   +" + "---+" * 10)

def convert_input(coordinates):
    """
        Permet de convertir des coordonnés de la grille (B2) en tuple (1,1)
        :param coordinates: coordonnés renseignées par l'utilisateur
       :return: Tuple avec la ligne et la colonne de la grille
    """
    row = None
    letters = "ABCDEFGHIJ"
    col_letter = coordinates[0].upper()
    row_number = coordinates[1:]

    if col_letter not in letters:
        return None

    if row_number.isdigit():
        row = int(row_number)
        if not 1 <= row <= 10:
            return None

    col = letters.index(col_letter)
    return row - 1, col

def main():
    print("Début du jeu (Taper QUITTER pour quitter)")
    boats = create_ships()
    boats_names = ["Porte-avions", "Croiseur", "Contre-torpilleur", "Sous-marin", "Torpilleur"]
    grid = create_empty_grid()
    print("Grille de départ")
    print_grid(grid)

    boats_position = []
    for boat in boats:
        for pos in boat:
            if pos not in boats_position:
                boats_position.append(pos)

    hit_positions = []
    missed_positions = []
    sink_boats = []

    while True:
        coordinates = input("Coordonnées à tester :").strip().upper()
        if coordinates == "QUITTER":
            print("Fin du jeu.")
            break

        result = convert_input(coordinates)
        if result is None:
            print("Entrée invalide. Format attendu: Lettres entre A  et J avec un chiffre de 1 à 10")
            continue

        if result in hit_positions or result in missed_positions:
            print("POSITION DEJA TESTE")
        elif result in boats_position:
            print("\n TOUCHE ! \n")
            hit_positions.append(result)
            grid[result[0], result[1]] = "X"

            # Vérifier si un navire est coulé
            for index, boat in enumerate(boats):
                if all(pos in hit_positions for pos in boat) and index not in sink_boats:
                    print(f"\n {boats_names[index]} COULÉ ! \n")
                    sink_boats.append(index)

        else:
            print("\n PAS TOUCHE ! \n")
            missed_positions.append(result)
            grid[result[0], result[1]] = "~"

        print_grid(grid)

        if len(sink_boats) == len(boats):
            print("Tous les navires sont coulés")
            break

if __name__ == '__main__':
    main()
