# Scryer

Program for
- querying Scryfall via the official API
- converting JSON dump files into human-readable lists

# Help

```bash
usage: scry.py [-h] [-j JSON_FILE_NAME] [-q SCRY_QUERY] [--no-names]
               [--colors] [--oracle] [--mana-cost] [--no-count] [--full]
               [--only-count]

Query Scryfall or Process JSON lists from scryfall.

options:
  -h, --help         show this help message and exit
  -j JSON_FILE_NAME  JSON file to be converted
  -q SCRY_QUERY      scryfall query
  --no-names         print names
  --colors           print colors
  --oracle           print oracle text
  --mana-cost        print oracle text
  --no-count         don't print card count
  --full             print full card info
  --only-count       print only card count
```

# Example output

```bash
> ./scry.py -q Aragorn --full
Got 4 cards:

Aragorn and Arwen, Wed {4}{G}{W} id:GW 
Vigilance
Whenever Aragorn and Arwen, Wed enters the battlefield or attacks, put a +1/+1 counter on each other creature you control. You gain 1 life for each other creature you control.

Aragorn, Company Leader {1}{G}{W} id:GW 
Whenever the Ring tempts you, if you chose a creature other than Aragorn, Company Leader as your Ring-bearer, put your choice of a counter from among first strike, vigilance, deathtouch, and lifelink on Aragorn.
Whenever you put one or more counters on Aragorn, put one of each of those kinds of counters on up to one other target creature.

Aragorn, King of Gondor {1}{U}{R}{W} id:RUW 
Vigilance, lifelink
When Aragorn, King of Gondor enters the battlefield, you become the monarch.
Whenever Aragorn attacks, up to one target creature can't block this turn. If you're the monarch, creatures can't block this turn.

Aragorn, the Uniter {R}{G}{W}{U} id:GRUW 
Whenever you cast a white spell, create a 1/1 white Human Soldier creature token.
Whenever you cast a blue spell, scry 2.
Whenever you cast a red spell, Aragorn, the Uniter deals 3 damage to target opponent.
Whenever you cast a green spell, target creature gets +4/+4 until end of turn.
```

# Known issues

- Querying for more than ~5000 cards hangs for some reason.