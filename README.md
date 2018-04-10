# The Python Fortnite API Wrapper
A work in progress.

## Installation
```bash
pip install fortnite
```

## Usage

### Setup
```python
import pfaw

fortnite = pfaw.Fortnite(fortnite_token='FORTNITE_TOKEN', launcher_token='LAUNCHER_TOKEN',
                    password='PASSWORD', email='EMAIL')
```

### Get player
Creates a player object containing the attributes name and id.
```python
smitty = fortnite.player('Smitty Werbenjagermanjensen')

print(smitty.name)
print(smitty.id)

# prints:
# Smitty Werbenjagermanjensen
# 9c9212603304472d831c03d0978d2bc1
```

### Get battle royale stats
Creates an object containing various stats for a given player.
```python
smitty_solo_pc = fortnite.battle_royale_stats(username='Smitty Werbenjagermanjensen', mode='solo', platform='pc')

print(smitty_solo_pc.score)
print(smitty_solo_pc.matches)
print(smitty_solo_pc.time)
print(smitty_solo_pc.kills)
print(smitty_solo_pc.wins)
print(smitty_solo_pc.top3)
print(smitty_solo_pc.top5)
print(smitty_solo_pc.top6)
print(smitty_solo_pc.top10)
print(smitty_solo_pc.top12)
print(smitty_solo_pc.top25)

# prints:
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0

# Smitty isn't very good at Fortnite
```

### Get server status
Checks if the Fortnite servers are up or down. Returns True if up or False if down.
```python
status = fortnite.server_status()

if status:
    print('Good news! The Fortnite servers are online.')
else:
    print('Sad news. The Fortnite servers are down. :(')
```

### Get friends of a player
Returns a list of player objects. As far as I know, this method only works for the authenticated player.
```python
smittys_pals = fortnite.friends(username='Smitty Werbenjagermanjensen')

for friend in smittys_pals:
    print(friend)
```

### Hopefully more methods to come
Feel free to open an issue or submit a pull request if you have any neat ideas.

Join the [Discord](https://discord.gg/AEfWXP9) for help and suggestions.

## Contributors
A thank you to those who have helped out with this project.

- Tom ([@Douile](https://github.com/Douile))