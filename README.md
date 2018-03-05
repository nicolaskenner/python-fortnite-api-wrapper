# The Python Fortnite API Wrapper
A work in progress.

## Example

```python
import pfaw

fortnite = pfaw.Fortnite(fortnite_token='FORTNITE_TOKEN', launcher_token='LAUNCHER_TOKEN',
                    password='PASSWORD', email='EMAIL')
player = fortnite.player('Smitty Werbenjagermanjensen')
print(f'His name is {player.name} and his id is {player.id}')

# prints:
# His name is Smitty Werbenjagermanjensen and his id is 9c9212603304472d831c03d0978d2bc1
```

Join the [Discord](https://discord.gg/eFBk3wZ) for help and suggestions.
