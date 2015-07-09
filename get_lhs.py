import ConfigParser
import json
import os
import sys

def main(args):
  config = ConfigParser.ConfigParser()
  config.read('yasp.cfg')
  player_id = config.get('yasp', 'player_id')
  hero_id = config.get('yasp', 'hero_id')
  wins = 0
  losses = 0

  def parse_match(match_data):
    for player in match_data['players']:
      if str(player['account_id']) == player_id and str(player['hero_id']) == hero_id:
        lasthits = player['parsedPlayer']['lh']
        won = player['isRadiant'] == match_data['radiant_win']
        if len(lasthits) > 21:
          print "{0}: {1} @10, {2} @20 {3}".format(match_data['match_id'], lasthits[10], lasthits[20], 'W' if won else 'L')
          return won
    return None

  sorted_matches = sorted(os.listdir("matches"))
  for file_name in sorted_matches:
    file = open(os.path.join("matches", file_name))
    match_data = json.load(file)
    file.close()
    res = parse_match(match_data)
    if res is not None:
      if res:
        wins += 1
      else:
        losses += 1
  print "{0}W {1}L".format(wins, losses)

if __name__ == "__main__":
  main(sys.argv)
