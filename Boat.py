#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Boat:
    boats = []

    def __init__(self, position,name):
        self.position = position
        self.name = name
        Boat.boats.append(self)