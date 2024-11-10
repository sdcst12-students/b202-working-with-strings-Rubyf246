#!python3

"""
Strings are iterable.  Use for loops to iterate through both strings to create a list to represent a deck of cards. Note: We can also use list comprehension as strings are still iterable!
"""

ranks = "A23456789TJQK"
suits = "CDHS"
deck = []
def createDeck():
  for char_of_rank in ranks:
    for char_of_suit in suits:
      deck.append(char_of_rank + char_of_suit)
  return deck

def main():
  deck = createDeck()
  print(deck)
  assert "AS" in deck
  assert "KC" in deck
  assert deck.count("TC") == 1


if __name__ == "__main__":
  main()
