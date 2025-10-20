"""
Classe permettant de définir les informations d'un bateau
"""

class Boat:
    boats = []

    def __init__(self, position,name):
        self.position = position
        self.name = name
        Boat.boats.append(self)