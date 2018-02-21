from . import constants
import requests
import sys


class Fortnite(object):
    def __init__(self, fortnite_token=None, launcher_token=None, password=None, username=None):
        self.fortnite_token = fortnite_token
        self.launcher_token = launcher_token
        self.password = password
        self.username = username
        launcher_payload = {
            'grant_type': 'password',
            'username': '{}'.format(self.username),
            'password': '{}'.format(self.password),
            'includePerms': True
        }
        request_for_access_token = requests.post(constants.token, headers={
            'Authorization': 'basic {}'.format(self.launcher_token)}, data=launcher_payload).json()
        access_token = request_for_access_token['access_token']
        request_for_code = requests.get(constants.exchange,
                                        headers={'Authorization': 'bearer {}'.format(access_token)}).json()
        code = request_for_code['code']
        fortnite_payload = {
            'grant_type': 'exchange_code',
            'exchange_code': '{}'.format(code),
            'includePerms': True,
            'token_type': 'egl'
        }
        request_for_fortnite = requests.post(constants.token,
                                             headers={'Authorization': 'basic {}'.format(self.fortnite_token)},
                                             data=fortnite_payload).json()
        self.expires_at = request_for_fortnite['expires_at']
        self.access_token_fortnite = request_for_fortnite['access_token']
        self.refresh_token = request_for_fortnite['refresh_token']

    def get_player(self, username):
        """Return player id and name"""
        try:
            request = requests.get(constants.player_lookup.format(username),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)
        player_id = request.json()['id']
        return player_id

    def get_all_time_stats(self, id):
        try:
            request = requests.get(constants.battle_royale_stats.format(id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)
        stats = request.json()
        all_time_stats = BattleRoyale(stats, 'all')
        return all_time_stats

    def get_solo_stats(self, id):
        try:
            request = requests.get(constants.battle_royale_stats.format(id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)
        stats = request.json()
        solo_stats = BattleRoyale(stats, 'solo')
        return solo_stats

    def get_duo_stats(self, id):
        try:
            request = requests.get(constants.battle_royale_stats.format(id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)
        stats = request.json()
        duo_stats = BattleRoyale(stats, 'duo')
        return duo_stats

    def get_squad_stats(self, id):
        try:
            request = requests.get(constants.battle_royale_stats.format(id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)
        stats = request.json()
        squad_stats = BattleRoyale(stats, 'squad')
        return squad_stats


class BattleRoyale(object):
    def __init__(self, data, mode):
        self.data = data
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
