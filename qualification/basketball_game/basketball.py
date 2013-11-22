#!/usr/bin/env python

from operator import itemgetter

def player_leave_cmp(p1, p2):
    if p1['minutes'] != p2['minutes']:
        return p2['minutes'] - p1['minutes']
    return p2['rank'] - p1['rank']

def player_enters_cmp(p1, p2):
    if p1['minutes'] != p2['minutes']:
        return p1['minutes'] - p2['minutes']
    return p1['rank'] - p2['rank']

def rank_players_cmp(p1, p2):
    if p1['shot_pct'] != p2['shot_pct']:
        return p1['shot_pct'] - p2['shot_pct']
    return p1['height'] - p2['height']    

def pick_players(players, rotations, team_size):    
    players.sort(cmp=rank_players_cmp)
    
    team_1, team_2 = [], []    
    
    for i, p in enumerate(reversed(players)):
        p['rank'] = i + 1
        
    for p in players:
        if p['rank'] % 2 == 1:
            team_1.append(p)
        else:
            team_2.append(p)

    lineup_1, lineup_2 = [], []    
    
    for i in range(0, team_size):
        lineup_1.append(team_1.pop(0))
        lineup_2.append(team_2.pop(0))
    
    if len(team_1) > 0:
        for r in range(0, rotations):
            for i in range(0, team_size):
                lineup_1[i]['minutes'] += 1
                lineup_2[i]['minutes'] += 1
            
            leaves_1 = sorted(lineup_1, cmp=player_leave_cmp)[0:1][0]
            leaves_2 = sorted(lineup_2, cmp=player_leave_cmp)[0:1][0]
            
            enters_1 = sorted(team_1, cmp=player_enters_cmp)[0:1][0]
            enters_2 = sorted(team_2, cmp=player_enters_cmp)[0:1][0] 
            
            lineup_1.remove(leaves_1)
            lineup_1.append(enters_1)
            team_1.remove(enters_1)
            team_1.append(leaves_1)
            
            lineup_2.remove(leaves_2)
            lineup_2.append(enters_2)
            team_2.remove(enters_2)
            team_2.append(leaves_2)
            
    players_in_field = []
    players_in_field.extend(lineup_1)
    players_in_field.extend(lineup_2)

    return " ".join(p['name'] for p in sorted(players_in_field, 
                                              key=itemgetter('name')))

if __name__ == "__main__":
    t = int(raw_input().strip())
   
    for i in range(1, t + 1):        
        params = raw_input().strip().split()
        n = int(params[0])
        m = int(params[1])
        p = int(params[2])
        
        players = []
        for player in range(0, n):
            player_params = raw_input().strip().split()
            players.append({
                'name': player_params[0],
                'shot_pct': int(player_params[1]),
                'height': int(player_params[2]),
                'minutes': 0
            })
        
        answer = pick_players(players, m, p)
        print "Case #{0}: {1}".format(i, answer)
        