class Enemy:
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True
        self._initial_hit_points = hit_points

    def take_damage(self, damage):
        lives_hit_points = (self._lives * self._initial_hit_points) + self._hit_points
        if 0 <= damage < lives_hit_points:
            lives_hit_points -= damage
            self._lives = lives_hit_points // self._initial_hit_points
            self._hit_points = lives_hit_points % self._initial_hit_points

            print("{0._name} took damage of {1}.".format(self, damage), end=' ')
            print(self)
        else:
            self._hit_points = 0
            self._lives = 0
            self._alive = False
            print("{0._name} took damage of {1}.".format(self, damage), end=' ')
            print("{0._name} is dead".format(self))

    def __str__(self):
        return "Name: {0._name} Hit_points: {0._hit_points} Lives: {0._lives}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        super(Troll, self).__init__(name=name, hit_points=20, lives=1)
        self.grunt()

    def grunt(self):
        print("I am  big ugly troll, my name {0._name}".format(self))


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=40, lives=3)

    @staticmethod
    def dodge():
        import random
        d = random.randint(1, 3)
        if d == 3:
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage)
        else:
            print("**** {0._name} dodged attack".format(self))


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140
        self._initial_hit_points = 140
        print(self)

    def take_damage(self, damage):
        print("Vampire king takes only 1/4 th of damage")
        super(Vampire, self).take_damage(damage//4)
