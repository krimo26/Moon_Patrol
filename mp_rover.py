#ROVER

import random

from mp_arena import Arena, Actor
from mp_obstacle import Obstacle, Pit_1, Pit_2, Rock_1, Rock_2
from mp_alien import Alien, Bullet_A

    
class Rover(Actor):
    def __init__(self,arena: "Arena"):

        self._arena = arena
        arena.add(self)

        self._arena_w, self._arena_h = self._arena.size()
        self._land_h = self._arena_h - 28 #Altezza del terreno
            
        self._w = 29
        self._h = 23
        self._x = 0
        self._y = self._land_h - self._h 
        self._dx = 0
        self._dy = 0
        self._speed = 5
        self._s_jump = 5

        self._lives = 1
        
        self._jumping = False
        self._fallen = False
        self._exploded = False

        self._count = 0

    def lives(self):
        return self._lives

    def move(self):
  
        g = 0.4
        self._dy += g
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        if self._y > self._land_h - self._h and self._fallen == False:
            self._y = self._land_h - self._h
        if self._y + self._dy >= self._land_h - self._h:
            self._dy = 0
            self._g = 0
        if self._dy == 0:
            self._jumping = False

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        if self._x > self._arena_w - self._w:
            self._x = self._arena_w - self._w

        if self._fallen == True:
            self.fall()
            
        if self._exploded == True:
            self.explode()

        if random.choice(range(200)) == 1: #Genera alieni casualmente
            alien = Alien(self._arena)

        if random.choice(range(500)) == 1: #Genera buche grandi casualmente
            pit1 = Pit_1(self._arena)

        if random.choice(range(500)) == 1: #Genera buche piccole casualmente
            pit2 = Pit_2(self._arena,750)
            
        if random.choice(range(500)) == 1: #Genera rocce piccole casualmente
            rock1 = Rock_1(self._arena)
            
        if random.choice(range(500)) == 1: #Genera rocce grandi casualmente
            rock2 = Rock_2(self._arena)

    def jump(self):
        if self._fallen == False and self._exploded == False:
            if self._y == self._land_h - self._h:
             self._dy = -self._s_jump
             self._jumping = True

             
    def go_left(self):
        if self._fallen == False and self._exploded == False:
            self._dx, self._dy = -self._speed, 0

    def go_right(self):
        if self._fallen == False and self._exploded == False:
            self._dx, self._dy = self._speed, 0

    def go_down(self):
        if self._fallen == False and self._exploded == False:
            self._dx, self._dy = 0, +self._speed

    def stay(self):
        if self._y > self._arena_h - self._h:
            self._dx = self._speed
        else:   
            self._dx = 0

    def collide(self, other):
        if isinstance(other, Pit_1):
            x,y,w,h = other.position()
            self._x = x
            self._fallen = True
            fr = Falling_Rover(self._arena,self)
            
        if isinstance(other, Pit_2):
            x,y,w,h = other.position()
            self._x = x
            self._fallen = True
            fr = Falling_Rover(self._arena, self)
        if isinstance(other, Rock_1):
            if other.destroyed() == False:
                self._exploded = True
        if isinstance(other, Rock_2):
            if other.destroyed() == False:
                self._exploded = True
        if isinstance(other, Bullet_A):
            self._exploded = True
            
            
    def position(self):   
        return self._x, self._y, self._w , self._h

    def fall(self):
        self._y += 1
        self._x -= 3
        self._count += 1
        if self._count >= 20:
            self._lives = self._lives-1

    def explode(self):
        self._dx = -3
        self._dy = 0
        self._count += 1
        if self._count >= 20:
            self._lives = self._lives-1
        

    def symbol(self):
        if self._jumping and self._dy < 0 and self._dx >= 0 and self._count ==0:
            return 47,104,29,26
        elif self._jumping and self._dy > 0 and self._dx >= 0 and self._count == 0:
            return 80, 103,29,26
        
        elif 0 < self._count <= 5:    #Sprite dell'esplosione
            return 113, 103, 46, 32
        elif 5 < self._count <= 10:
            return 165, 101, 46, 32
        elif 10 < self._count <= 15:
            return 214, 103, 41, 29
        elif 15 < self._count <= 20:
            return 263, 117, 32, 16
        
        else:
            return 212, 158, 32, self._h

    def shoot(self): #Il rover spara 2 proiettili
        bullet = Bullet(self._arena,self)
        bullet1 = Bullet_1(self._arena,self)

    def lives(self):
        return self._lives

class Falling_Rover(Actor): #Solo per disegnare l'esplosione sopra la buca quando il rover cade
    
    def __init__(self,arena:"Arena",rover:"Rover"):
        x,y,w,h = rover.position()
        self._x = x
        self._y = y
        self._w = w
        self._h = h

        self._arena = arena
        arena.add(self)
        
        self._count = 0
        
    def move(self):
        self._y += 1
        self._x -= 3
        self._count += 1

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if 0 < self._count <= 5:    #Sprite dell'esplosione
            return 113, 103, 46, 32
        elif 5 < self._count <= 10:
            return 165, 101, 46, 32
        elif 10 < self._count <= 15:
            return 214, 103, 41, 29
        elif 15 < self._count <= 20:
            return 263, 117, 32, 16
        else:
            return 1,0,0,0

    def collide(self,other):
        pass
        
        

class Bullet(Actor):
    def __init__(self,arena, rover: "Rover"):
        self._rover = rover
        x,y,w,h = self._rover.position()
        self._x = x + 32 #Il proiettile parte dalla sagoma del rover
        self._y = y + 10         
        self._count = 0
        
        self._arena = arena
        arena.add(self)


        self._dx = 6
        self._dy = 0
      
        if 0 <= self._count <= 4: #Per ogni sprite del proiettile anche le dimensioni cambiano
            self._w = 10
            self._h = 4
    
        if 4 < self._count <= 8:
            self._w = 10
            self._h = 4
            
        if 8 < self._count <= 12:
            self._w = 6
            self._h = 7

        if 12 < self._count <= 16:
            self._w = 8
            self._h = 10
            
        if 16 < self._count <= 20:
            self._w = 12
            self._h = 14

        if 20 < self._count <= 24:
            self._w = 12
            self._h = 14
               
        if 24 < self._count <= 28:
            self._w = 12
            self._h = 14

    def move(self):
        self._x += self._dx
        self._count += 1
        
        if self._count >= 28:
            self._arena.remove(self)

    def position(self):
        
        if 0 <= self._count <= 4 :
            return self._x, self._y, 10, 4 
         
        if 4 < self._count <= 8 :
            return self._x, self._y, 10, 4
            
        if 8 < self._count <= 12:
            return self._x, self._y, 6, 7
            
        if 12 < self._count <= 16:
            return self._x, self._y, 8, 10
            
        if 16 < self._count <= 20:
             return self._x, self._y, 12, 14
            
        if 20 < self._count <= 24:
             return self._x, self._y, 8, 8
            
        if 24 < self._count <= 28:
             return self._x, self._y, 10, 12
            
    def symbol(self):
        if 0 <= self._count <= 4:
            return 193,143,10,4
        
        elif 4 < self._count <= 8:
            return 204,143,10,4
        
        elif 8 < self._count <= 12:
            return 225,142,6,7
        
        elif 12 < self._count <= 16:
            return 239,140,8,10
        
        elif 16 < self._count <= 20:
            return 253,138,12,14
        
        elif 20 < self._count <= 24:
            return 269,142,8,8
        
        elif 24 < self._count <= 28:
            return 283,140,10,12
        
        else:
            return 0,0,0,0


    def collide(self,other):
        if isinstance (other, Rock_1):
            if self in self._arena.actors():
                self._arena.remove(self)
    
        if isinstance (other, Rock_2):
            if self in self._arena.actors():
                self._arena.remove(self)


class Bullet_1(Actor):
    def __init__(self,arena, rover: "Rover"):
        self._rover = rover
        x,y,w,h = self._rover.position()
        self._x = x + 9 
        self._y = y
        self._w = 2
        self._h = 7
        
        self._count = 0
        
        self._arena = arena
        arena.add(self)

        self._dx = 0
        self._dy = -6

    def move(self):
        if self._y < 0:
            self._arena.remove(self)
        self._y += self._dy

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 127,63, self._w, self._h

    def collide(self,other):
        pass

