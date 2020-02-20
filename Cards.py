import random

class Card:
    suit_list=['trefl', 'karo', 'kier', 'pik']
    rank_list=["As","2","3","4","5","6","7","8","9","10","Walet","Dama","Krol"]

    def __init__(self, rank, suit):
        self.rank= rank
        self.suit= suit

    def __str__(self):
        return "{} {}".format(self.rank, self.suit)



class Deck(Card):

    def __init__(self):
        # Stworzenie talii kart
        self.cards= []
        for suit in suit_list:
            for rank in rank_list:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        pass

    def remove_card(self):
        pass


class Player:

    def __init__(self, money=100):
        #Stworzenie "ręki" gracza z 2 losowymi kartami z talii
        self.hand=[self.cards[random.randint(0, len(self.cards))], self.cards[random.randint(0, len(self.cards))] ]







