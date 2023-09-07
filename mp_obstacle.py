#OBSTACLE

import random

from mp_arena import Arena, Actor
import mp_rover

class Obstacle(Actor):
    def move(self):
        raise NotImplementedError("Abstract method")
    def position(self):
        raise NotImplementedError("Abstract method")
    def symbol(self):
        raise NotImplementedError("Abstract method")    
    def collide(self, other: 'Actor'):
        raise NotImplementedError("Abstract method")
    
class Pit_1(Actor):
    def __init__(self,arena:"Arena"):

        self._arena = arena
        arena.add(self)

        self._arena_w, self._arena_h = self._arena.size()
        self._land_h = self._arena_h - 28 #ALTEZZA DEL TERRENO

        self._x = 750
        self._y = self._land_h - 7 #Per evitare imprecisioni nel disegno
        self._dx = -3
        self._w = 45
        self._h = 39


    def move(self):
         if self._x < -100:
             self._arena.remove(self)
         self._x = self._x + self._dx

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 155, 140, 24, 21

    def collide(self,other):
        if isinstance(other,Rock_1):
            self._arena.remove(self)
        if isinstance(other,Rock_2):
            self._arena.remove(self) 

class Pit_2(Actor):
    
    def __init__(self,arena: "Arena",x):      
        self._arena = arena
        arena.add(self)

        self._arena_w, self._arena_h = self._arena.size()
        self._land_h = self._arena_h - 28 #Altezza del terreno

        self._x = x
        self._y = self._land_h - 7 #Per evitare imprecisioni nel disegno
        self._dx = -3
        self._w = 30
        self._h = 30

    def move(self):
        if self._x < -100:
            self._arena.remove(self)
        self._x = self._x + self._dx

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 131, 167, 26, 26

    def collide(self,other):
        pass
 

class Rock_1(Actor):
    
    def __init__(self,arena: "Arena"):
        self._arena = arena
        arena.add(self)

        self._arena_w, self._arena_h = self._arena.size()
        self._land_h = self._arena_h - 28 #Altezza del terreno

        self._w = 15
        self._h = 15

        self._x = 750
        self._y = self._land_h - self._h 
        self._dx = -3

        self._lives = 1

        self._destroyed = False

        self._count = 0

    def move(self):
        if self._lives <=0:
            self.explode()
            self._destroyed = True
        if self._x < -100:
            self._arena.remove(self)
        self._x = self._x + self._dx

    def position(self): 
        return self._x, self._y, self._w, self._h

    def symbol(self):
        
        if 0 < self._count <= 5:
            return 89, 304, 16, 16
        if 5 < self._count <= 10:
            return 106, 302, 16, 16
        if 10 < self._count <= 15:
            return 123, 302, 16, 16
        if 15 < self._count <= 20:
            return 106, 302, 16, 16
        if 20 < self._count <= 25:
            return 143, 196, 25, 22
        if 25 < self._count <= 30:
            return 174, 287, 28, 31

        if self._count > 30: #Lo sprite dell'esplosione non colpisce il rover
            return 1,0,0,0
        
        
        else:
            return 80, 203, 13, 13

    def collide(self,other):
        if isinstance (other, mp_rover.Bullet):
            if self in self._arena.actors():
                self._lives = self._lives-1
        if isinstance (other, Pit_2): #Evito rocce sopra le buche
            self._arena.remove(self)

    def destroyed(self):
        return self._destroyed

    def explode(self):
        self._count += 1

class Rock_2(Actor):
    
    def __init__(self,arena: "Arena"):      
        self._arena = arena
        arena.add(self)

        self._arena_w, self._arena_h = self._arena.size()
        self._land_h = self._arena_h - 28 #Altezza del terreno
        
        self._w = 30
        self._h = 30

        self._x = 750
        self._y = self._land_h - self._h 
        self._dx = -3

        self._lives = 2

        self._destroyed = False

        self._count = 0

    def move(self):
        if self._lives <= 0:
            self.explode()
            self._destroyed = True
        if self._x < -100:
            self._arena.remove(self)
        self._x = self._x + self._dx

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        
        if 0 < self._count <= 5:
            return 89, 304, 16, 16
        if 5 < self._count <= 10:
            return 106, 302, 16, 16
        if 10 < self._count <= 15:
            return 123, 302, 16, 16
        if 15 < self._count <= 20:
            return 106, 302, 16, 16
        if 20 < self._count <= 25:
            return 143, 196, 25, 22
        if 25 < self._count <= 30:
            return 174, 287, 28, 31

        if self._count > 30: #Lo sprite dell'esplosione non colpisce il rover
            return 1,0,0,0
        
        else:
            return 96, 200, 15, 15

    def collide(self,other):
        if isinstance (other, mp_rover.Bullet):
            if self in self._arena.actors():
                self._lives = self._lives-1
        if isinstance (other, Pit_2): #Evito rocce sopra le buche
            self._arena.remove(self)
    
    def destroyed(self):
        return self._destroyed

    def explode(self):
        self._count += 1
                
                

