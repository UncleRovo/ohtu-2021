from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def top_scorers_by_nationality(self, nat):
        players = self.reader.getPlayers(nat)
        
        players.sort(key=lambda player: player.getPoints(), reverse=True)
        
        return players
        
