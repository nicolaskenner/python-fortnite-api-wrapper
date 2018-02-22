class Player(object):
    def __init__(self, player_dict):
        self.name = player_dict['playerName']
        self.id = player_dict['id']


class BattleRoyale(object):
    def __init__(self, br_dict, mode):
        self.data = br_dict
        self.score = 0
        self.matches = 0
        self.time = 0
        self.kills = 0
        self.wins = 0
        self.top3 = 0
        self.top5 = 0
        self.top6 = 0
        self.top10 = 0
        self.top12 = 0
        self.top25 = 0

        mode = mode.lower()
        if mode == 'solo':
            mode = '_p2'
        elif mode == 'duo':
            mode = '_p10'
        elif mode == 'squad':
            mode = '_p9'
        elif mode == 'all':
            mode = '_p'

        for i in self.data:
            if mode in i['name']:
                if 'score' in i['name']:
                    self.score += i['value']
                elif 'matchesplayed' in i['name']:
                    self.matches += i['value']
                elif 'minutesplayed' in i['name']:
                    self.time += i['value']
                elif 'kills' in i['name']:
                    self.kills += i['value']
                elif 'placetop1' in i['name']:
                    self.wins += i['value']
                elif 'placetop3' in i['name']:
                    self.top3 += i['value']
                elif 'placetop5' in i['name']:
                    self.top5 += i['value']
                elif 'placetop6' in i['name']:
                    self.top6 += i['value']
                elif 'placetop10' in i['name']:
                    self.top10 += i['value']
                elif 'placetop12' in i['name']:
                    self.top12 += i['value']
                elif 'placetop25' in i['name']:
                    self.top25 += i['value']
