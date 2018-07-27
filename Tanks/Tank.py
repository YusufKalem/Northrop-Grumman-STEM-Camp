#A template for creating tank objects

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.armor = 20
        self.ammo = 10
        self.alive = True
    #this is how we represent out tank as a string
    def __str__(self):
        if self.alive:
            return "%s, (%i ammo, %i armor)" % (self.name, self.ammo, self.armor)
        else:
            return "%s (DEAD)" %self.name
    def fire_at(self,enemy):
            if self.ammo >= 1:
                self.ammo = self.ammo - 1
                print (self.name, "fires at", enemy.name)
                enemy.hit()
            else:
                print(self.name, "has no ammo")
# We take a hit, if it breaks our shields, the tank explodes.
    def hit(self):
        self.armor -= 5
        print(self.name, "is hit")
        if(self.armor <= 0):
            self.explode()
    def explode(self):
        print(self.name, "explodes")
        self.alive = False
