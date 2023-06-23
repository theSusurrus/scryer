#!/usr/bin/python3

import sys
import json
import argparse
import urllib.request
import time

def parse_json(json_text:str):
  json_object = json.loads(json_text)

  if json_object is dict:
    # get card list from API response
    api_mode = True
    card_list = json_object["data"]
  else:
    # get card list from Scryfall dump
    card_list = json_object
    api_mode = False

  cards = []
  for card in card_list:
    cards.append(card)

  has_more = False
  next_page = ""

  if api_mode:
    try:
      has_more = json_object["has_more"]
      next_page = json_object["next_page"]
    except KeyError:
      pass

  meta = (has_more, next_page)
  
  return (cards, meta)

def parse_json_file(json_file_name:str):
  with open(args.json_file_name) as json_file:
    json_text = json_file.read()
  
  (cards, meta) = parse_json(json_text)

  return cards

def query_scryfall(scry_query:str):
  sanitized_query = urllib.parse.quote(scry_query, safe='/', encoding=None, errors=None)
  scry_http_get = f"https://api.scryfall.com/cards/search?q={sanitized_query}"
  json_text = urllib.request.urlopen(scry_http_get).read()

  (cards, meta) = parse_json(json_text)

  while meta[0]:
    next_page = urllib.request.urlopen(meta[1]).read()
    (new_cards, meta) = parse_json(next_page)
    cards.extend(new_cards)
    time.sleep(0.1) #rate limiting, as per Scryfall API rules
  
  return cards

def print_cards(cards, name=True, color=False, oracle=False, mana_cost=False):
  for card in cards:
    if name:
      print(card["name"], end=' ')
    if mana_cost:
      try:
        print(card["mana_cost"], end=' ')
      except KeyError:
        pass
    if color:
      print(f"id:{''.join(card['color_identity'])}", end=' ')
    if oracle:
      try:
        print(f"\n{card['oracle_text']}")
      except KeyError:
        pass
    print()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Query Scryfall or Process JSON lists from scryfall.')
  parser.add_argument('-j', dest="json_file_name",
                      help='JSON file to be converted')
  parser.add_argument('-q', dest="scry_query",
                      help='scryfall query')
  parser.add_argument('--no-names', dest="print_no_names",
                      help='print names',
                      action="store_true")
  parser.add_argument('--colors', dest="print_colors",
                      help='print colors',
                      action="store_true")
  parser.add_argument('--oracle', dest="print_oracle",
                      help='print oracle text',
                      action="store_true")
  parser.add_argument('--mana-cost', dest="print_mana_cost",
                      help='print oracle text',
                      action="store_true")
  parser.add_argument('--no-count', dest="print_no_count",
                      help='don\'t print card count',
                      action="store_true")
  parser.add_argument('--full', dest="print_full",
                      help='print full card info',
                      action="store_true")
  parser.add_argument('--only-count', dest="print_only_count",
                      help='print only card count',
                      action="store_true")

  args = parser.parse_args()

  if not len(sys.argv) > 1:
    parser.print_help()
    exit()

  if (args.json_file_name is not None) and (args.scry_query is not None):
    raise RuntimeError("Invalid parameters")
  
  if args.json_file_name is not None:
    cards = parse_json_file(args.json_file_name)
  
  if args.scry_query is not None:
    cards = query_scryfall(args.scry_query)

  if not args.print_no_count:
    print(f"Got {len(cards)} cards:")

  if args.print_full:
    args.print_oracle = True
    args.print_colors = True
    args.print_mana_cost = True
  elif args.print_only_count:
    exit()

  print()
  print_cards(cards,
              name=(not args.print_no_names),
              color=args.print_colors,
              oracle=args.print_oracle,
              mana_cost=args.print_mana_cost)
