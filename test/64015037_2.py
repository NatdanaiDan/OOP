from random import randint, choice
from time import sleep


class Monster:
    def __init__(self):
        self._Atk = 1
        self._hp = 3
        self._level = 50
        self._status = True
        self._x_pos = randint(0, 9)
        self._y_pos = randint(0, 9)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def level(self):
        return self._level

    @property
    def x_pos(self):
        return self._x_pos

    @property
    def y_pos(self):
        return self._y_pos

    def attack(self, target):
        x, y = self._x_pos, self._y_pos
        direction_x, direction_y = choice([x - 1, x, x + 1]), choice([y - 1, y, y + 1])
        if target.x_pos == direction_x and target.y_pos == direction_y:
            target.hp -= self._Atk
            if target.hp <= 0:
                target.status = False


class Novice:
    def __init__(self):
        self._hp = 10
        self._atk = 1
        self._Exp = 0
        self._level = 1
        self._status = True
        self._x_pos = 0
        self._y_pos = 0

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def atk(self):
        return self._atk

    @property
    def level(self):
        return self._level

    @property
    def x_pos(self):
        return self._x_pos

    @property
    def y_pos(self):
        return self._y_pos

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    def walk(self):
        while True:
            self._x_pos = self._x_pos + choice([-1, 0, 1])
            if -1 < self._x_pos < 10:
                break

        while True:
            self._y_pos = self._y_pos + choice([-1, 0, 1])
            if -1 < self._y_pos < 10:
                break

    def find_monster(self, target):
        if target.x_pos - self._x_pos == 1 or target.x_pos - self._x_pos == -1:
            if target.y_pos - self._y_pos == 1 or target.y_pos - self._y_pos == -1:
                return True
        return False

    def attack(self, target):
        target.hp = target.hp - self.atk
        print("Novice attacks!")
        self._Exp += target.level
        if target.hp <= 0:
            target.status = False
            print("Monster is dead!")

    def level_up(self):
        if self._Exp >= 100:
            self._level += 1
            self._Exp = 0


class Swordman(Novice):
    def __init__(self):
        super().__init__()
        self._atk = 10

    @property
    def atk(self):
        return self._atk

    @atk.setter
    def atk(self, value):
        self._atk = value

    def attack(self, target):
        self._atk = choice([self._atk, self._atk + 10])
        super().attack(target)
        self._atk = 10


class Acolyte(Novice):
    def __init__(self):
        super().__init__()
        self._atk = 5

    def attack(self, target):
        random = randint(0, 1)
        if random == 0:
            super().attack(target)
        else:
            self._hp = self._hp + 5


class Game:
    def __init__(self):
        self._player = Novice()
        self._monster = Monster()
        print(f"{self._player.x_pos}, {self._player.y_pos}")
        print(f"{self._monster.x_pos}, {self._monster.y_pos}")  # monster position
        self._monster_count = 0

    @property
    def player(self):
        return self._player

    @property
    def monster(self):
        return self._monster

    def game_run(self):

        if self.player.find_monster(self.monster):
            self.player.attack(self.monster)
            self.monster.attack(self.player)
            self.player.level_up()
            self.print()
        else:
            self.player.walk()
            self.print()
        if self.monster.status == False:
            self._monster = Monster()
            self._monster_count += 1
        if self._monster_count == 3 or self._player.status == False:
            print("You win!")
            exit()

    def print(self):
        print(
            f"Player X {self._player.x_pos}, Y {self._player.y_pos} Lv.{self._player.level} HP {self._player.hp} EXP {self._player._Exp}"
        )
        print(
            f"Monster X {self._monster.x_pos}, Y{self._monster.y_pos} HP{self._monster.hp}\n"
        )


game1 = Game()
i = 0
while True:
    game1.game_run()
    i += 1
