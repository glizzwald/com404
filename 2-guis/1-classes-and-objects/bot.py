class Bot :
    #constructor
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.energy = 100
        self.shield = 100

    #method
    def display_name(self):
        print(" _______")
        print("|       |")
        print("|",self.name, " |")
        print("|       |")
        print("|_______|")


    def display_age(self):
        print(" _______")
        print("|_______|")
        print("|",self.age, "    |")
        print("|_______|")
        print("|_______|")


    def display_energy(self):
        print("my energy level is","♦"*self.energy)


    def display_shield(self):
        print("my shield level is", "♦"*self.shield)


    #make some bots

beep = Bot ("Beep")
beep.display_name()
beep.display_age()
beep.display_energy()
beep.display_shield()
