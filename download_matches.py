import ConfigParser
import os
import requests
from subprocess import call
import sys

def main(args):
  config = ConfigParser.ConfigParser()
  config.read('yasp.cfg')
  player_id = config.get('yasp', 'player_id')
  hero_id = config.get('yasp', 'hero_id')

  req = requests.get("http://yasp.co/players/{0}/matches?json=1".format(player_id))
  json = req.json()

  def valid(match):
    return match['parse_status'] == 2 and str(match['players'][0]['hero_id']) == hero_id

  valid_matches = filter(valid, json['matches'])

  for match in valid_matches:
    match_id = match['match_id']
    file_name = 'matches/{0}.json'.format(match_id)
    if not os.path.isfile(file_name):
      print 'grabbing {0}'.format(match_id)
      call(['curl', '-o', file_name, 'http://yasp.co/matches/{0}?json=1'.format(match_id)])

if __name__ == "__main__":
  main(sys.argv)
