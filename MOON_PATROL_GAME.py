from time import time
import random

from mp_arena import Arena, Actor
from mp_rover import Rover, Bullet, Bullet_1
from mp_obstacle import Obstacle, Pit_1, Pit_2, Rock_1, Rock_2
from mp_alien import Alien, Bullet_A
from mp_background import Background, Background_1, Background_2, Land

class MPgame:
    def __init__(self):
        self._arena = Arena((510,256))

        bg_11 = Background_1(self._arena,0)
        bg_12 = Background_1(self._arena,512)
        bg_21 = Background_2(self._arena,0)
        bg_22 = Background_2(self._arena,512)
        l1 = Land(self._arena,0)
        l2 = Land(self._arena,500)
        
        self._hero = Rover(self._arena)
        
        self._start = time()
        self._playtime = 120

    def arena(self) -> Arena:
        return self._arena

    def hero(self) -> Rover:
        return self._hero

    def game_over(self) -> bool:
        return self._hero.lives() <= 0

    def game_won(self) -> bool:
        return time() - self._start > self._playtime

    def remaining_time(self) -> int:
        return int(self._start + self._playtime - time())
