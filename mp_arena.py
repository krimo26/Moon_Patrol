#ARENA

class Actor():
    def move(self):
        raise NotImplementedError('Abstract method')

    def collide(self, other: 'Actor'):
        raise NotImplementedError('Abstract method')

    def position(self) -> (int, int, int, int):
        raise NotImplementedError('Abstract method')

    def symbol(self) -> (int, int, int, int):
        raise NotImplementedError('Abstract method')

class Arena():
    def __init__(self, size: (int, int)):
        self._w, self._h = size
        self._actors = []
        self._backgrounds = []

    def add(self, a: Actor):
        if a not in self._actors:
            self._actors.append(a)

    def add_bg(self, b: Actor):
        if b not in self._backgrounds:
            self._backgrounds.append(b)

    def remove(self, a: Actor):
        if a in self._actors:
            self._actors.remove(a)

    def move_all(self):
        actors = list(reversed(self._actors))
        for a in actors:
            previous_pos = a.position()
            a.move()
            if a.position() != previous_pos:
                for other in actors:
                    if other is not a and self.check_collision(a, other):
                            a.collide(other)
                            other.collide(a)

    def move_bg(self):
        backgrounds = list(reversed(self._backgrounds))
        for b in backgrounds:
            b.move()

    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        x1, y1, w1, h1 = a1.position()
        x2, y2, w2, h2 = a2.position()
        return (y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2
            and a1 in self._actors and a2 in self._actors)

    def actors(self) -> list:
        return list(self._actors)

    def backgrounds(self) -> list:
        return list(self._backgrounds)

    def size(self) -> (int, int):
        return (self._w, self._h)


            




