class Player:
    def __init__(self, playerdict):
        self.playerdict = playerdict
        
    def get(self, value):
        return self.playerdict[value]
        
    def getPoints(self):
        return self.playerdict["goals"] + self.playerdict["assists"]
