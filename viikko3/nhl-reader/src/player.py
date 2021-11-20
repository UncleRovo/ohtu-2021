class Player:
    def __init__(self, playerdict):
        self.playerdict = playerdict
        
    def __str__(self):
        row = self.playerdict["team"] +" " + str(self.playerdict["goals"]) + " + " + str(self.playerdict["assists"]) + " = " + str(self.getPoints())
        rowjust = 23 - len(self.playerdict["name"]) + len(row)
        name = self.playerdict["name"]
        return name + row.rjust(rowjust)
        
        
        
    def get(self, value):
        return self.playerdict[value]
        
    def getPoints(self):
        return self.playerdict["goals"] + self.playerdict["assists"]
