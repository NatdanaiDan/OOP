from random import randint, random
import time


class Novice:
    _hp = 0
    _atk = 0

    _exp = 0
    _level = 0

    _location_x = None
    _location_y = None

    _status = ""

    _map = None

    _exp_gain = 13

    def __init__(self, map):
        self._hp = 10
        self._atk = 1
        self._exp = 0
        self._level = 1
        self._status = "alive"

        self._map = map

        self._map.addPlayer(self)

    def spawn(self):
        self._location_x = randint(0, self._map.get_wall_x())
        self._location_y = randint(0, self._map.get_wall_y())

        print("\nSystem: Player is spawned at ({self._location_x},{self._location_y})")

    def walk(self):
        self._location_x += randint(-1, 1)
        self._location_y += randint(-1, 1)

        old_location_x = int(str(self._location_x))
        old_location_y = int(str(self._location_y))

        while not (self._location_x < self._map.get_wall_x() and self._location_x > 0):
            self._location_x += randint(-1, 1)

        while not (self._location_y < self._map.get_wall_y() and self._location_y > 0):
            self._location_y += randint(-1, 1)

        print(f"\nSystem: Walk to ({self._location_x+1},{self._location_y+1})")

        self.findMonster()

    def sit(self):
        print("\nPlayer: you are sitting now !")

    def attack(self):
        print("\nPlayer: Attack monster!!")
        monster = self._map.getMonsters()
        monster.getDamaged(self._atk)
        player.addEXP(self._exp_gain)

    def death(self):
        if self._hp <= 0:
            self._status = "death"
            print("\nSystem: Game Over !")

    def getDamaged(self, value):
        self._hp -= value
        print(f"\nSystem: You hurt {value} damage")

        self.death()

    def addEXP(self, value):
        self._exp += value
        print(f"\nSystem: You gain {value} exp !")

        self.levelUp()

    def levelUp(self):
        if self._exp >= 100:
            self._exp -= 100
            self._level += 1

        print("\nSystem: Level UP !!!!")

    def findMonster(self):
        monster = self._map.getMonsters()

        if monster != None:
            if (
                abs(self._location_x - monster.location_x) <= 3
                and abs(self._location_y - monster.location_y) <= 3
            ):
                self._status = "Found Monster"
                print(f"\n\n\n\nPlayer: Found the monster nearly !!!!!")
            else:
                self._status = "alive"

    def getDetail(self):
        print("\n=======[ Player Detail ]=======")
        print("")
        print("HP: ", self._hp)
        print("ATK: ", self._atk)
        print("")
        print("EXP: ", self._exp)
        print("LEVEL: ", self._level)
        print("")
        print(
            f"LOCATION (X,Y): {self._location_x+1} {self._location_y+1}",
        )
        print("")
        print(f"STATUS: {self._status}")
        print("")
        print("===============================")

    @property
    def location_x(self):
        return self._location_x

    @property
    def location_y(self):
        return self._location_y

    @property
    def status(self):
        return self._status

    @property
    def hp(self):
        return self._status

    @hp.setter
    def hp(self, value):
        self._hp = value


class Monster:
    _hp = 0
    _atk = 0

    _location_x = 0
    _location_y = 0

    _status = "alive"

    def __init__(self, map):

        self._map = map

        self._map.addMonster(self)

    def attack(self):
        pass

    def spawn(self):
        self._location_x = randint(0, self._map.get_wall_x())
        self._location_y = randint(0, self._map.get_wall_y())

        self._hp = 3
        self._atk = 1
        self._status = "alive"

        print(
            f"\nSystem: Monster is spawned at ({self._location_x},{self._location_y})"
        )

    def death(self):
        if self._hp <= 0:
            self._status = "death"
            print("\nSystem: Monster is dead")

    def getDetail(self):
        print("\n=======[ Monster Detail ]======")
        print("")
        print("HP: ", self._hp)
        print("ATK: ", self._atk)
        print("")
        print(
            f"LOCATION (X,Y): {self._location_x+1} {self._location_y+1}",
        )
        print("")
        print(f"STATUS: {self._status}")
        print("")
        print("===============================")

    def getDamaged(self, value):
        self._hp -= value
        print(f"\nMonster: Hurt {value} damage")

        self.death()

    @property
    def location_x(self):
        return self._location_x

    @property
    def location_y(self):
        return self._location_y

    @property
    def status(self):
        return self._status


class Map:
    _player = None
    _monster = None

    def __init__(self, limit_x, limit_y):
        self._size_x = limit_x
        self._size_y = limit_y

    def addMonster(self, monster):
        self._monster = monster

    def addPlayer(self, player):
        self._player = player

    def getMonsters(self):
        return self._monster

    def get_wall_x(self):
        return self._size_x

    def get_wall_y(self):
        return self._size_y

    def generate_map(self):
        print("\n==============================")
        for y in range(0, self._size_y):
            row = ""
            for x in range(0, self._size_x):
                if (
                    self._monster != None
                    and self._monster.location_x == x
                    and self._monster.location_y == y
                ):
                    row += " M "
                elif (
                    self._player != None
                    and self._player.location_x == x
                    and self._player.location_y == y
                ):
                    row += " P "
                else:
                    row += " - "

            print(row)
        print("==============================\n")


MonsterStack = 0

map1 = Map(10, 10)

player = Novice(map1)
player.spawn()
player.getDetail()

monster = Monster(map1)
monster.spawn()
monster.getDetail()

map1.generate_map()

while True:
    if player.status != "Found Monster":
        player.walk()
        map1.generate_map()
    else:
        if monster.status == "death":
            monster.spawn()
            player.findMonster()
            map1.generate_map()

            MonsterStack += 1
            if MonsterStack == 3:
                break

        else:
            player.attack()
            player.getDetail()
            monster.getDetail()

    time.sleep(0.2)


print("================ Game End ===================")
