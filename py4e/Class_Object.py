class ParyAnimal:

    x = 0

    def __init__(self):

        print("I am constructured")

    def party(self):

        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):

        print('I am desturcted', self.x)


#an = ParyAnimal()

#an.party()
#an.party()
#an = 42
#print('an contain', an)

class PartyAnimal:

    x = 0
    name =""

    def __init__(self, z):

        self.name = z
        print(self.name, "constructed")

    def party(self):

        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):

    points = 0

    def touchdown(self):

        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()
#j = PartyAnimal("Jim")
#j.party()
#s.party()
j = FootballFan("Jim")
j.party()
j.touchdown()
j.touchdown()
j.touchdown()
j.touchdown()
