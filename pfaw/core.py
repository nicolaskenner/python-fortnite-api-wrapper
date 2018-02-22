from . import constants
from . import models
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

    def get_player_from_username(self, username):
        try:
            request = requests.get(constants.player_lookup.format(username),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)

        return models.Player(player_dict=request.json())

    def get_all_time_stats(self, player_id):
        try:
            request = requests.get(constants.battle_royale_stats.format(player_id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)

        return models.BattleRoyale(br_dict=request.json(), mode='all')

    def get_solo_stats(self, player_id):
        try:
            request = requests.get(constants.battle_royale_stats.format(player_id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)

        return models.BattleRoyale(br_dict=request.json(), mode='solo')

    def get_duo_stats(self, player_id):
        try:
            request = requests.get(constants.battle_royale_stats.format(player_id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)

        return models.BattleRoyale(br_dict=request.json(), mode='duo')

    def get_squad_stats(self, player_id):
        try:
            request = requests.get(constants.battle_royale_stats.format(player_id),
                                   headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})
        except requests.exceptions.RequestException as e:
            sys.exit(e)

        return models.BattleRoyale(br_dict=request.json(), mode='squad')
