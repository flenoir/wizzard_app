import random

class Creature():
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(self.name,self.level)

    def get_defensive_roll(self):
        return random.randint(1,12) * self.level

class Wizard(Creature):
    
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def attack(self,creature):
        print('The wizard {} attack {}'.format(self.name,creature.name))

        my_roll = self.get_defensive_roll() #self pour que le roll appartienne au Wizard
        creature_roll = creature.get_defensive_roll()

        print("The wizard {} rolled the value : {}".format(self.name, my_roll))
        print("{} rolled the value : {}".format(creature.name,creature_roll))

        if my_roll >= creature_roll:
            print("the wizard won")
            return True #to make attack if/else work
        else:
            print("The wizard loses")
            return False #to make attack if/else work

class Small_creatures(Creature):
    # on ne recré pas de __init__ methode car ce sera exactement la même
    def get_defensive_roll(self):
        small_roll = super().get_defensive_roll()
        return small_roll /2

class Dragon(Creature):
    # on recré une  méthode __init__ car on y ajoute un paramètre
    def __init__(self, name, level, scaliness, breath_fire):
        super().__init__(name,level)
        self.scaliness = scaliness
        self.breath_fire = breath_fire

    def get_defensive_roll(self):
        big_roll = super().get_defensive_roll()
        # lambda = VALUE IF TRUE if TEST else VALUE IF FALSE
        fire_modifier = 5 if self.breath_fire else 1
        scaliness_modifier = self.scaliness / 10
        return big_roll * fire_modifier * scaliness_modifier
