from pfaw.core import Fortnite


def main():
    """The output of this example should look something like this
    Ol' Smitty Werbenjagermanjensen killed 0 people across 0 solo matches.

    """

    # Api Credentials
    fortnite_token = 'some_token'
    launcher_token = 'some_token'
    password = 'epic_games_password'
    email = 'epic_games_email'

    # Instantiate Fortnite class
    fortnite_instance = Fortnite(fortnite_token=fortnite_token, launcher_token=launcher_token,
                                 password=password, email=email)

    # Get player object
    smitty = fortnite_instance.player('smitty werbenjagermanjensen')

    # Get Battle Royale stats object for the solo game-mode on the pc platform
    smitty_solo_pc = fortnite_instance.battle_royale_stats(username=smitty.name, mode='solo', platform='pc')

    tale_of_smitty = f"Ol' {smitty.name} killed {smitty_solo_pc.kills} people across {smitty_solo_pc.matches} solo matches."

    print(tale_of_smitty)


if __name__ == '__main__':
    main()
