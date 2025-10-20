class Boat:
    boats = []

    @classmethod
    def nb_boats(cls):
        return len(cls.boats)


    def __init__(self, position,name):
        self.position = position
        self.name = name
        Boat.boats.append(self)


    def __repr__(self):
        boat_name = self.name
        return f"{boat_name}{self.position}"