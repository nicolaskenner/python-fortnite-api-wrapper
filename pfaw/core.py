from . import constants
from . import objects
import requests


class Fortnite(object):
    def __init__(self, fortnite_token=None, launcher_token=None, password=None, email=None):
        launcher_payload = {
            'grant_type': 'password',
            'username': '{}'.format(email),
            'password': '{}'.format(password),
            'includePerms': True
        }
        request_for_access_token = requests.post(constants.token, headers={
            'Authorization': 'basic {}'.format(launcher_token)}, data=launcher_payload).json()
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
                                             headers={'Authorization': 'basic {}'.format(fortnite_token)},
                                             data=fortnite_payload).json()
        self.expires_at = request_for_fortnite['expires_at']
        self.access_token_fortnite = request_for_fortnite['access_token']
        self.refresh_token = request_for_fortnite['refresh_token']

    def player(self, username):
        """Return object containing player name and id"""
        response = requests.get(constants.player.format(username),
                                headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})

        return objects.Player(response=response.json())

    def battle_royale_stats(self, username, mode, platform):
        """Return object containing Battle Royale stats

        mode can be solo, duo, squad, or all.
        platform can be pc, ps4, or xb1.

        Example: Fortnite.battle_royale_stats('Jimmy', 'solo', 'pc')

        """

        player_id = self.player(username=username).id
        response = requests.get(constants.battle_royale.format(player_id),
                                headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite)})

        return objects.BattleRoyale(response=response.json(), mode=mode.lower(), platform=platform.lower())

    def server_status(self):
        """Check the status of the Fortnite servers. Returns True if up and False if down."""
        response = requests.get(constants.status)
        if response.json()[0]['status'] == 'UP':
            return True
        else:
            return False

    def friends(self, username):
        """Return list of Player objects. This method only works for the authenticated account."""
        player_id = self.player(username=username).id
        response = requests.get(constants.friends.format(player_id),
                                headers={'Authorization': 'bearer {}'.format(self.access_token_fortnite),
                                         'includePending': 'false'})
        friends = []
        for friend in response.json():
            friends.append({f"displayName": f"{friend.get('displayName')}", f"id": f"{friend.get('accountId')}"})
        list_of_friend_objects = [objects.Player(player) for player in friends]

        return list_of_friend_objects
