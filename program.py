from creatures import Creature, Wizard, Small_creatures,Dragon
import random
import time

def main():
    get_header()
    main_loop()


def get_header():
    print('------------------------------')
    print(' Wizard Game')
    print('------------------------------')
    print('')

def main_loop():

    creatures = [
        Small_creatures("Toad", 1),
        Creature("Tiger", 12),
        Small_creatures("wolf",9),
        Creature("crocodile",20),
        Small_creatures("dog",6),
        Creature("dwarf",30),
        Dragon("Dragon",50, 20, True),
        Wizard("Evil Wizard",1000)
    ]

    hero = Wizard("gandolf",75)

    # print(creatures)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from the foggy forest'.format(active_creature.name,active_creature.level))
        print('')

        cmd = input("What do you want to do ? [a]ttack, [r]un or [l]ookaround ")

        if cmd == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard needs to rest for a while")
                time.sleep(5)
                print("Wizard returns revitalized")
        elif cmd == "r":
            print("The Wizard runs beacuase he doesn't want to fight")
        elif cmd == "l":
            print("the wizard {} lookaround and sees :".format(hero.name))
            for c in creatures:
                print("* A {} of level {}".format(c.name, c.level))
        else:
            print("ok exiting")
            break

        if not creatures:
            print("The Wizard {} has defeated all creatures".format(hero.name))

if __name__ == '__main__':
    main()
