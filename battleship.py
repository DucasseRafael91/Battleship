from Grid import Grid
from Boat import Boat

def create_ships():
    """
       Créer les différents bateaux
       :return: liste de bateaux
    """
    boats = []

    # Porte-avions (B2 à F2) : ligne 1, colonnes 1-5
    aircraft = Boat([(1, i) for i in range(1, 6)], "Aircraft")
    boats.append(aircraft)

    # Croiseur (A4 à A7) : ligne 3, colonnes 0-3
    cruiser = Boat([(3, i) for i in range(0, 4)], "Cruiser")
    boats.append(cruiser)

    # Contre-torpilleur (C5 à E5) : lignes 2-4, colonne 4
    destroyer = Boat([(i, 4) for i in range(2, 5)], "Destroyer")
    boats.append(destroyer)

    # Sous-marin (H5 à J5) : lignes 7-9, colonne 4
    submarine = Boat([(i, 4) for i in range(7, 10)], "Submarine")
    boats.append(submarine)

    # Torpilleur (E9 à F9) : lignes 4-5, colonne 8
    torpedo_boat = Boat([(i, 8) for i in range(4, 6)], "Torpedo Boat")
    boats.append(torpedo_boat)

    return boats

def main():
    grid_obj = Grid()   # instance de la classe Grid
    boats = create_ships()
    boats_names = ["Porte-avions", "Croiseur", "Contre-torpilleur", "Sous-marin", "Torpilleur"]

    print("Grille de départ")
    grid_obj.print_grid()

    boats_position = []
    for boat in boats:
        for pos in boat.position:
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

        result = grid_obj.convert_input(coordinates)
        if result is None:
            print("Entrée invalide. Format attendu: Lettres entre A et J avec un chiffre de 1 à 10")
            continue

        if result in hit_positions or result in missed_positions:
            print("POSITION DEJA TESTÉE")
        elif result in boats_position:
            print("\n TOUCHE ! \n")
            hit_positions.append(result)
            grid_obj.grid[result[0], result[1]] = "X"

            for index, boat in enumerate(boats):
                if all(pos in hit_positions for pos in boat.position) and index not in sink_boats:
                    print(f"\n {boats_names[index]} COULÉ ! \n")
                    sink_boats.append(index)
        else:
            print("\n PAS TOUCHE ! \n")
            missed_positions.append(result)
            grid_obj.grid[result[0], result[1]] = "~"

        grid_obj.print_grid()

        if len(sink_boats) == len(boats):
            print("Tous les navires sont coulés")
            break

if __name__ == '__main__':
    main()
