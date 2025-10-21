# Grid.py
import numpy as np


class Grid:
    def __init__(self):
        self.grid = self.create_empty_grid()

    def create_empty_grid(self):
        """
        Créer la zone de jeu de 10 par 10 avec Numpy
        :return: grille de jeu (numpy array)
        """
        return np.full((10, 10), " ", dtype=str)

    def print_grid(self):
        """
        Affiche la zone de jeu avec Numpy
        """
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("   +" + "---+" * 10)
        print("   | " + " | ".join(letters) + " |")
        print("   +" + "---+" * 10)

        for row_num in range(10):
            row_display = f"{row_num + 1:<2} |"
            for col in range(10):
                row_display += f" {self.grid[row_num, col]} |"
            print(row_display)
            print("   +" + "---+" * 10)

    def convert_input(self, coordinates):
        """
        Permet de convertir des coordonnés de la grille (B2) en tuple (1,1)
        :param coordinates: coordonnés renseignées par l'utilisateur
        :return: Tuple avec la ligne et la colonne de la grille, ou None si invalide
        """
        letters = "ABCDEFGHIJ"
        if len(coordinates) < 2:
            return None
        col_letter = coordinates[0].upper()
        row_number = coordinates[1:]

        if col_letter not in letters:
            return None

        if not row_number.isdigit():
            return None

        row = int(row_number)
        if not 1 <= row <= 10:
            return None

        col = letters.index(col_letter)
        return row - 1, col
