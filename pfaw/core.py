from . import constants
from . import objects
import requests


class Fortnite:
    def __init__(self, fortnite_token, launcher_token, password, email):
        password_response = requests.post(constants.token, headers={'Authorization': f'basic {launcher_token}'},
                                          data={'grant_type': 'password', 'username': '{}'.format(email),
                                                'password': '{}'.format(password), 'includePerms': True}).json()
        access_token = password_response.get('access_token')

        exchange_response = requests.get(constants.exchange,
                                         headers={'Authorization': 'bearer {}'.format(access_token)}).json()
        code = exchange_response.get('code')

        token_response = requests.post(constants.token, headers={'Authorization': 'basic {}'.format(fortnite_token)},
                                       data={'grant_type': 'exchange_code', 'exchange_code': '{}'.format(code),
                                             'includePerms': True, 'token_type': 'egl'}).json()

        self.access_token = token_response.get('access_token')
        self.refresh_token = token_response.get('refresh_token')
        self.expires_at = token_response.get('expires_at')
        self.session = Session(self.access_token)

    def player(self, username):
        """Return object containing player name and id"""
        response = self.session.get(constants.player.format(username))
        return objects.Player(response)

    def battle_royale_stats(self, username, platform):
        """Return object containing Battle Royale stats"""
        player_id = self.player(username).id
        response = self.session.get(constants.battle_royale.format(player_id))
        return objects.BattleRoyale(response=response, platform=platform)

    def friends(self, username):
        """Return list of player ids. This method only works for the authenticated account."""
        player_id = self.player(username).id
        response = self.session.get(constants.friends.format(player_id))
        return [friend.get('accountId') for friend in response]

    def store(self, rw=-1):
        """Return current store items. This method only works for the authenticated account."""
        response = self.session.get(constants.store.format(rw))
        return objects.Store(response)

    @staticmethod
    def news():
        """Get the current news on fortnite."""
        response = requests.get(constants.news, headers={'Accept-Language': 'en'})
        return objects.News(status=response.status_code, response=response.json())

    @staticmethod
    def server_status():
        """Check the status of the Fortnite servers. Returns True if up and False if down."""
        response = requests.get(constants.status)
        if response.json()[0]['status'] == 'UP':
            return True
        else:
            return False


class Session:
    def __init__(self, access_token):
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'bearer {access_token}'})

    def get(self, endpoint):
        response = self.session.get(endpoint)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()
