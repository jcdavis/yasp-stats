import math
import requests
import sys
import yasp_util

def score(hero):
  wins = hero['win']
  games = hero['games']
  if games == 0:
    return 0
  z = 2.57 # 99% confidence?
  phat = 1.0*wins/games
  return (phat + z*z/(2*games) - z*math.sqrt((phat*(1-phat)+z*z/(4*games))/games))/(1+z*z/games)

def main(args):
  player_id = args[1] if len(args) > 1 else yasp_util.get_player_id()
  req = requests.get("http://yasp.co/players/{0}?json=1".format(player_id))
  json = req.json()
  sorted_heroes = sorted(json['aggData']['heroes'].values(), key=score)
  sorted_heroes.reverse()

  hero_data = yasp_util.get_hero_data()

  for data in sorted_heroes[:10]:
    wins = data['win']
    games = data['games']
    losses = games - wins
    hero_info = hero_data[int(data['hero_id'])]
    print "{0}: {1}W {2}L {3}%".format(hero_info['localized_name'], wins, losses, 100.0*wins/games)


if __name__ == "__main__":
  main(sys.argv)
