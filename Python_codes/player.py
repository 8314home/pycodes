class Player:

    def __init__(self, name):
        self._name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def __str__(self):
        return "Player : {0._name} Level: {0._level} Score: {0._score} Lives: {0._lives} ".format(self)

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives can not be less than 0")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._level = level
            self._score += delta * 1000
        else:
            print("level can not be less than 1")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def player_score(self):
        return self._score

    @player_score.setter
    def player_score(self, x):
        if x > 0:
            self._score = x



