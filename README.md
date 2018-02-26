# The Python Fortnite API Wrapper
A work in progress.

## Example

```python
from pfaw.core import Fortnite

fortnite = Fortnite(fortnite_token='FORTNITE_TOKEN', launcher_token='LAUNCHER_TOKEN', password='PASSWORD', email='EMAIL')
player = fortnite.player('Smitty Werbenjagermanjensen')
print(f'His name is {player.name} and his id is {player.id}')
```

Join the [Discord](https://discord.gg/eFBk3wZ) for help and suggestions.
