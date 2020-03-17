from player import Player
from enemy import Enemy, Troll, Vampire, VampireKing

if __name__ == "__main__":

    print("Starting program")

    tim = Player("tim")
    john = Player("john")

    print(tim)
    print(john)

    tim.level = 5
    print(tim)

    print("TIM SCORE BEFORE -> {}".format(tim.player_score))
    tim.player_score = 2000
    print("TIM SCORE -> {}".format(tim.player_score))

    john.level = 8
    print(john)

    print(john.lives)
    john.level = 3
    print(john)

    tim.lives = -1
    tim.level = 0

    print("-" * 40)

    enemy = Enemy("Ogre")
    print(enemy)

    bigogre = Enemy("BigOgre", 25, 1)
    print(bigogre)
    bigogre.take_damage(10)

    troll = Troll("Ug")
    print(troll)
    print("troll taking damage 30 ")
    troll.take_damage(30)

    print("-" * 40)

    vamp = Vampire("dracula")
    print(vamp)
    print("dracula taking damage 15 ")
    vamp.take_damage(15)

    vamp2 = Vampire("dracula_2")
    print(vamp2)
    print("dracula_2 taking damage 55 ")
    vamp2.take_damage(55)
    print("dracula_2 again taking damage 35 ")
    vamp2.take_damage(35)

    print("dracula_2 again taking damage 25 ")
    vamp2.take_damage(25)

    print("dracula_2 again taking damage 165 ")
    vamp2.take_damage(165)

    print("-" * 40)
    print("New Vamp King created")
    vamp_king = VampireKing("DraculaKing")

    print("DraculaKing again taking damage 165 ")
    vamp_king.take_damage(165)

    print("\nEnding program")
