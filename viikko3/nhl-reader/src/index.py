from playerstats import PlayerStats
from datetime import datetime
from player import Player
from playerreader import PlayerReader

def main():
    
    playreader = PlayerReader("https://nhlstatisticsforohtu.herokuapp.com/players")
    stats = PlayerStats(playreader)
    players = stats.top_scorers_by_nationality("FIN")
    print("Players from FIN: " + str(datetime.now()))
    
    for player in players:
       print(player)

if __name__ == "__main__":
    main()
