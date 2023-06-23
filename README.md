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

# Known issues

- Querying for more than ~5000 cards hangs for some reason.