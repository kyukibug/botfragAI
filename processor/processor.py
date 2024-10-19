from utils.riot import get_players
from utils.logger import print_json

# Configuration
YEARS = [2023, 2024]

LEAGUES = ["game-changers", "vct-challengers", "vct-international"]


def build_player_map():
    map = {}
    
    players = []
    for league in LEAGUES:
        players.extend(get_players(league))
    
    print(f"\nPlayer Count: {len(players)}")
    # print_json(players[0])
    for player in players:
        # Add player if not in map, and update if player entry is newer than current
        if player["id"] not in map or player["updated_at"] > map[player["id"]]["updated_at"]:
            map[player["id"]] = player
        
    return map

def build_game_mapping():
    games = []
    
    return games

if __name__ == "__main__":
    player_map = []
    player_map = build_player_map()
    print(f"\nMap Count: {len(player_map)}")
    print_json(player_map["106525489805459472"])
    
    # Download mapping data to match players with matches played
    
    
'''
Processor Steps:
    1. Create Player Map from players.json
        - key: id
        - value: {
            id,
            
        }
    
    2. Parse through each game, updating player stats via participantMapping id's
    
    
Scenarios need to handle for:
- Multiple player entries, only record latest entry
    - Maintains current team & league status
'''
