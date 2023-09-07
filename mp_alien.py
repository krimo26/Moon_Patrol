#ALIEN

import random

from mp_arena import Arena, Actor
from mp_obstacle import Obstacle, Pit_2
import mp_rover 

class Alien(Actor):
    def __init__(self,arena):

        self._x = random.randrange(1,60)
        self._y = random.randrange(1,60)
        
        self._w = 15
        self._h = 8

        self._dx = random.choice([-2,-1,1,2])
        self._dy = random.choice([-2,-1,1,2])

        self._count_s = 0 #Per gli sprite

        self._lives = 1
        
        self._arena = arena
        arena.add(self)

        self._arena_w, self._arena_h = self._arena.size()

        self._exploded = False

    def move(self):
        
        self._x += self._dx
        self._y += self._dy

        if self._y <= 0:
            self._dy = -self._dy
        if self._y >= 60:
            self._dy = -self._dy
        if self._x <= 0:
            self._dx = -self._dx
        if self._x >= self._arena_w - self._w:
            self._dx = -self._dx

        if self._lives <=0:
            self.explode()
            if self._count_s > 15:
                self._arena.remove(self)

        if random.choice(range(200)) == 1: #1 volta su 200 chiamate di tick l'alieno spara
            bullet = Bullet_A(self._arena,self)

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if 0 < self._count_s <= 5:
            return 125, 269, 12, 12
        if 5 < self._count_s <= 10:
            return 142, 268, 13, 13
        if 10 < self._count_s <= 15:
            return 157, 267, 16, 16
        else:
            return 67, 230, self._w, self._h

    def collide(self,other):
        if isinstance(other, mp_rover.Bullet_1):
            self._lives = self._lives - 1
    
    def explode(self):
        self._count_s += 1
        self._dx, self._dy = 0,0
    

class Bullet_A(Actor):
    def __init__(self,arena, alien: "Alien"):
        self._alien = alien
        x,y,w,h = self._alien.position()
        self._x = x + 7
        self._y = y + 4
        self._w = 5
        self._h = 8
                
        self._arena = arena
        arena.add(self)

        self._arena_w, self._arena_h = self._arena.size()

        self._dx = 0
        self._dy = 3


    def move(self):
        if self._y > self._arena_h - 30:
            if random.choice(range(10)) == 1: # 1 proiettile su 10 forma una buca             
                pit2 = Pit_2(self._arena,self._x)  
            self._arena.remove(self)
        self._y += self._dy

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 213, 231, self._w, self._h

    def collide(self,other):
        pass
            
