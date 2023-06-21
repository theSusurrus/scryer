import json
import argparse

def parse_json(json_file_name:str):
  with open(args.json_file_name) as json_file:
    scry_json = json_file.read()
    scry = json.loads(scry_json)
  
  return scry

def json_list_to_names(scry):
  card_names = []

  with open(args.json_file_name) as json_file:
    scry_json = json_file.read()
    scry = json.loads(scry_json)

    for card in scry["data"]:
      card_names.append(card["name"])
  
  return card_names

def print_names(card_names):
  for card_name in card_names:
    print(card_name)

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
  
  if args.json_file_name is not None:
    scry = parse_json(args.json_file_name)
  
  if args.scry_query is not None:
    scry = get_cards(args.scry_query)

  if args.print_names:
    card_names = json_list_to_names(scry)
    print_names(card_names)
