from pfaw.core import Fortnite
from pfaw.credentials import Credentials


def main():
    """An example of using the API. The output should look something like this:

    SOME OF NICK'S STATS

    SCORE:
    	- All | 740
    	- Solo | 184
    	- Duo | 0
    	- Squad | 556

    MATCHES PLAYED:
    	- All | 10
    	- Solo | 2
    	- Duo | 0
    	- Squad | 8

    """
    # Instantiate Fortnite class
    fortnite = Fortnite(fortnite_token=Credentials.fortnite_token, launcher_token=Credentials.launcher_token,
                        password=Credentials.password, username=Credentials.username)

    # Get player ID from Epic Games username.
    nicks_username = 'Nick K'
    nick = fortnite.get_player_from_username(nicks_username)

    # These methods will return objects containing various stats from the API.
    all_time = fortnite.get_all_time_stats(nick.id)
    solo = fortnite.get_solo_stats(nick.id)
    duo = fortnite.get_duo_stats(nick.id)
    squad = fortnite.get_squad_stats(nick.id)

    # Do something with our stat objects.
    fancy_stats_string = """
    SOME OF NICK'S STATS\n
    SCORE:
    \t- All | {score_all}
    \t- Solo | {score_solo}
    \t- Duo | {score_duo}
    \t- Squad | {score_squad}\n
    MATCHES PLAYED:
    \t- All | {matches_all}
    \t- Solo | {matches_solo}
    \t- Duo | {matches_duo}
    \t- Squad | {matches_squad}
    """

    formatted_string = fancy_stats_string.format(score_all=all_time.score, score_solo=solo.score,
                                                 score_duo=duo.score, score_squad=squad.score,
                                                 matches_all=all_time.matches, matches_solo=solo.matches,
                                                 matches_duo=duo.matches, matches_squad=squad.matches)

    print(formatted_string)


if __name__ == '__main__':
    main()
