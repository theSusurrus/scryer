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
  parser.add_argument('json_file_name', metavar='JSON', type=str,
                      help='JSON file to be converted')
  parser.add_argument('--names', dest="print_names",
                      help='print names',
                      action="store_true")
  args = parser.parse_args()
  
  scry = parse_json(args.json_file_name)

  if args.print_names:
    card_names = json_list_to_names(scry)
    print_names(card_names)

