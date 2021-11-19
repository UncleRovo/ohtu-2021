import requests
from datetime import datetime
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict
        )
        
        if player.get("nationality") == "FIN":
            players.append(player)
    
    currentdate = datetime.now()
    
    print("Players from FIN: " + str(currentdate))
    players.sort(key=lambda player: player.getPoints(), reverse=True)

    for player in players:
        row = player.get("team") +" " + str(player.get("goals")) + " + " + str(player.get("assists")) + " = " + str(player.getPoints())
        rowjust = 23 - len(player.get("name")) + len(row)
        
        print(player.get("name") + row.rjust(rowjust))

if __name__ == "__main__":
    main()
