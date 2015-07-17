import ConfigParser
import json

def get_player_id():
  config = ConfigParser.ConfigParser()
  config.read('yasp.cfg')
  return config.get('yasp', 'player_id')

def get_hero_id():
  config = ConfigParser.ConfigParser()
  config.read('yasp.cfg')
  return config.get('yasp', 'hero_id')

def get_hero_data():
  file = open("heroes.json")
  data = json.load(file)
  file.close()
  return dict([hero['id'], hero] for hero in data['heroes'])

