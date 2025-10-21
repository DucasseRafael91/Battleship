import numpy as np

class Grid:
    def __init__(self, boats):
        self.grid = np.full((10, 10), " ", dtype=str)
        self.boats = boats
        self.hit_positions = []
        self.missed_positions = []
        self.sunk_boats = []
        self.boats_positions = self._gather_boat_positions()

    def _get_boat_positions(self):
        positions = []
        for boat in self.boats:
            for pos in boat.position:
                if pos not in positions:
                    positions.append(pos)
        return positions


