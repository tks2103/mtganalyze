import json
from pprint import pprint

class Library:
  def __init__(self, library):
    self.library = library
    self.cards = library['cards']

  def search(self, search):
    for item in self.cards:
      if 'text' in item and search in item['text']:
        pprint(item['name'])

f = open('ORI.json', 'r')
text = f.read()
lib = Library(json.loads(text))

print lib.search('Renown')
