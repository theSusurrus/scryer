import json
import argparse

def parse_json(json_file_name:str):
  cards = []

  with open(args.json_file_name) as json_file:
    scry_json = json_file.read()
    scry = json.loads(scry_json)

  for card in scry["data"]:
    cards.append(card)
  
  return cards

def print_cards(cards, print_name=True):
  for card in cards:
    if print_name:
      print(card["name"])

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Process JSON lists from scryfall.')
  parser.add_argument('-j', dest="json_file_name",
                      help='JSON file to be converted')
  parser.add_argument('-q', dest="scry_query",
                      help='scryfall query')
  parser.add_argument('--names', dest="print_names",
                      help='print names',
                      action="store_true")
  args = parser.parse_args()

  if (args.json_file_name is not None) and (args.scry_query is not None):
    raise RuntimeError("Invalid parameters")
  
  if args.json_file_name is not None:
    cards = parse_json(args.json_file_name)
  
  if args.scry_query is not None:
    cards = get_cards(args.scry_query)

  if args.print_names:
    print_cards(cards)
