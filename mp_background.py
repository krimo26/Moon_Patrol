#BACKGROUND

from mp_arena import Arena, Actor
ARENA_W, ARENA_H = 510, 256

class Background(Actor):  
    def move(self):
        raise NotImplementedError("Abstract method")

    def stay(self):
        raise NotImplementedError("Abstract method")
    
    def position(self):
        raise NotImplementedError("Abstract method")
    
    def symbol(self):
        raise NotImplementedError("Abstract method")

    def collide(self, other: 'Actor'):
        raise NotImplementedError('Abstract method')


class Background_1(Background):
    def __init__(self,arena,x):
        self._x = x
        self._y = -80
        self._w = 512
        self._h = 256
        self._dx = -1

        self._arena = arena
        arena.add_bg(self)      

    def move(self):
        if self._x + self._dx < -512: # "Riciclo" dello stesso sfondo
            self._x = 512
        self._x = self._x + self._dx

    def stay(self):
        self._dx = 0

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol (self):
        return 0, 0, self._w, self._h

    def collide(self,other):
        pass



class Background_2(Background):
    def __init__(self,arena,x):
        self._x = x
        self._y = 110
        self._w = 512
        self._h = 127
        self._dx = -2

        self._arena = arena
        arena.add_bg(self)       
        
    def move(self):
        if self._x + self._dx < -512:
            self._x = 512
        self._x = self._x + self._dx

    def stay(self):
        self._dx = 0
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol (self):
        return 0, 256, self._w, self._h

    def collide(self,other):
        pass

class Land(Background):
    def __init__(self,arena,x):
        self._x = x
        self._y = 220
        self._w = 512
        self._h = 128
        self._dx = -3
        
        self._arena = arena
        arena.add_bg(self)
        
    def move(self):
        if self._x + self._dx <= -500:
            self._x = 500
        self._x = self._x + self._dx

    def stay(self):
        self._dx = 0
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol (self):
        return 0, 512, self._w, self._h

    def collide(self,other):
        pass

