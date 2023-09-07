#ALCUNI TEST PER IL MOON PATROL

import unittest

from mp_arena import Arena, Actor
from mp_rover import Rover, Bullet, Bullet_1
from mp_obstacle import Obstacle, Pit_1, Pit_1, Rock_1, Rock_2
from mp_alien import Alien, Bullet_A

class RoverTest(unittest.TestCase):

    def test_move(self):
        a = Arena((510,256))
        r = Rover(a) #x = 0, y = 205, w = 29, h = 23

        r.go_left() #Il rover non può andare più a sinistra del bordo dell'arena
        r.move()

        self.assertTrue(r.position() == (0,205,29,23))

    def test_jump(self):
        a = Arena((510,256))
        r = Rover(a) #x = 0, y = 205, w = 29, h = 23

        r.jump()
        r.move()

        self.assertTrue(r.position() == (0,200.4,29,23)) #y1 = (y-dy+g), dy = 5, g = 0.4
        

    def test_collide_rock1(self):
        a = Arena((510,256))
        r = Rover(a)
        rock = Rock_1(a)
        r.collide(rock)

        i = 0
        while i < 20: #Il rover perde la vita dopo 20 chiamate di move perchè deve cambiare gli sprite
            r.move()
            i += 1
    
        if rock.destroyed() == True: #Se la roccia è disrtutta il rover non perde vite
            self.assertTrue(r.lives() == 1)

    def test_collide_pit1(self):
        a = Arena((510,256))
        r = Rover(a)
        pit = Pit_1(a)
        r.collide(pit)

        i= 0
        while i < 20: #Il rover perde la vita dopo 20 chiamate di move perchè deve cambiare gli sprite
            r.move()
            i+=1
        self.assertTrue(r.lives() == 0)
if __name__ == '__main__':
    unittest.main()
