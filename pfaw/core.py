import epic_games_endpoint
import credentials
import requests
import sys


class FortniteApi(object):
    def __init__(self, credentials):
        self.launcher_token = credentials['launcher_token']
        self.fortnite_token = credentials['fortnite_token']
        self.username = credentials['username']
        self.password = credentials['password']
        launcher_payload = {
            'grant_type': 'password',
            'username': '{}'.format(self.username),
            'password': '{}'.format(self.password),
            'includePerms': True
        }
        request_for_access_token = requests.post(epic_games_endpoint.token, headers={
            'Authorization': 'basic {}'.format(self.launcher_token)}, data=launcher_payload).json()
        access_token = request_for_access_token['access_token']
        request_for_code = requests.get(epic_games_endpoint.exchange,
                                        headers={'Authorization': 'bearer {}'.format(access_token)}).json()
        code = request_for_code['code']
        fortnite_payload = {
            'grant_type': 'exchange_code',
            'exchange_code': '{}'.format(code),
            'includePerms': True,
            'token_type': 'egl'
        }
        request_for_fortnite = requests.post(epic_games_endpoint.token,
                                             headers={'Authorization': 'basic {}'.format(self.fortnite_token)},
                                             data=fortnite_payload).json()
        self.expires_at = request_for_fortnite['expires_at']
        self.access_token_fortnite = request_for_fortnite['access_token']
        self.refresh_token = request_for_fortnite['refresh_token']

    def print_credentials(self):
        print(self.launcher_token)
        print(self.fortnite_token)
        print(self.username)
        print(self.password)

    def lookup_player(self, username):
        """Check if the username exists. If it does, return dict containing player id and username."""
        try:
            request = requests.get(epic_games_endpoint.player_lookup.format(username),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        if request.status_code == 200:
            print(request.json())
            return request.json()
        elif request.status_code == 404 and 'errorCode' in request.json() and request.json()['errorCode'] == 'errors.com.epicgames.persona.account_not_found':
            print(request.json()['errorMessage'])
            return request.json()['errorMessage']
        else:
            pass

    def get_battle_royale_stats_from_id(self, id):
        try:
            request = requests.get(epic_games_endpoint.battle_royale_stats.format(id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        print(request.json())

    def get_battle_royale_stats_from_name(self, username):
        id = self.lookup_player(username)['id']
        try:
            request = requests.get(epic_games_endpoint.battle_royale_stats.format(id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        print(request.json())
        return request.json()

    @staticmethod
    def create_stats_dict(data):
        all_modes = {
            'score': 0,
            'matches': 0,
            'time': 0,
            'kills': 0,
            'wins': 0,
            'top3': 0,
            'top5': 0,
            'top6': 0,
            'top10': 0,
            'top12': 0,
            'top25': 0,
        }
        for i in data:
            if 'score' in i['name']:
                all_modes['score'] += i['value']
            elif 'matchesplayed' in i['name']:
                all_modes['matches'] += i['value']
            elif 'minutesplayed' in i['name']:
                all_modes['time'] += i['value']
            elif 'kills' in i['name']:
                all_modes['kills'] += i['value']
            elif 'placetop1' in i['name']:
                all_modes['wins'] += i['value']
            elif 'placetop3' in i['name']:
                all_modes['top3'] += i['value']
            elif 'placetop5' in i['name']:
                all_modes['top5'] += i['value']
            elif 'placetop6' in i['name']:
                all_modes['top6'] += i['value']
            elif 'placetop10' in i['name']:
                all_modes['top10'] += i['value']
            elif 'placetop12' in i['name']:
                all_modes['top12'] += i['value']
            elif 'placetop25' in i['name']:
                all_modes['top25'] += i['value']

        for k, v in all_modes.items():
            print('--------------------\n{}: {}'.format(k, v))
        print('--------------------')


if __name__ == '__main__':
    pass