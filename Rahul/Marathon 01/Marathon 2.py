# Question 2
class FrenchDeck:
    def __init__(self):
        self.deck = []
        self.rank = [str(n) for n in range(2, 11)] + list('JQKA')
        self.suit = ["spades", "diamonds", "club", "hearts"]

    def adding(self):
        for i in self.suit:
            for j in self.rank:
                self.deck.append((j, i))
        return self.deck

    def __getitem__(self, n):
        return self.deck[n]

    def __len__(self):
        return len(self.deck)


Taash = FrenchDeck()
Deck = Taash.adding()

#  Fetch the length of cards
print(len(Deck))

# Fetch the first card in the deck
print(Deck[0])

# Fetch the last card in the deck
print(Deck[-1])

# Fetch the random card in the deck
print(Deck[:7])












