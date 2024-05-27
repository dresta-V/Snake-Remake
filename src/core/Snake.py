from pygame.math import Vector2
from Prey import Prey


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 8), Vector2(4, 8), Vector2(3, 8)]
        self.Prey = Prey()

        self.score = 0
        self.fitness = 0

        self.life_time = 0
        self.steps = 0

    def reset(self):
        self.body = [Vector2(5, 8), Vector2(4, 8), Vector2(3, 8)]

        self.score = 0
        self.fitness = 0
        self.steps = 0


    def get_x(self):
        return self.body[0].x

    def get_y(self):
        return self.body[0].y

    def get_Prey(self):
        return self.Prey.position

    def ate_Prey(self):
        if self.Prey.position == self.body[0]:
            self.score += 1
            self.life_time -= 40
            return True
        return False

    def create_Prey(self):
        self.Prey.generate_Prey()

    def add_body(self):
        last_indx = len(self.body) - 1
        tail = self.body[-1]
        before_last = self.body[-2]

        if tail.x == before_last.x:
            if tail.y < before_last.y:
                self.body.append(Vector2(tail.x, tail.y-1))
            else:
                self.body.append(Vector2(tail.x, tail.y+1))
        elif tail.y == before_last.y:
            if tail.x < before_last.x:
                self.body.append(Vector2(tail.x - 1, tail.y))
            else:
                self.body.append(Vector2(tail.x + 1, tail.y))

    def ate_body(self):
        for body in self.body[1:]:
            if self.body[0] == body:
                return True
        return False
