import random

suit_list = ['trefl', 'karo', 'kier', 'pik']
rank_list = ["puste", "As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Walet", "Dama", "Krol"]
value_list= {"As":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Walet":10, "Dama":10, "Krol":10}

playing_game= True

class Card:

    def __init__(self, rank=0, suit=0):
        self.rank= rank
        self.suit= suit
        self.value= value_list[rank_list[rank]]


    def __str__(self):
        return "{} {}".format(rank_list[self.rank], suit_list[self.suit])

    def __repr__(self):
        return "Card({}, {})".format(self.rank, self.suit)



class Deck(Card):

    def __init__(self):
        self.cards= []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(rank, suit))

    def remove_cards(self, cards):
        for card in cards:
            if card in self.cards:
                self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)


    def deal(self):
        return self.cards.pop()


    def is_empty(self):
        return self.cards== []


    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def __len__(self):
        return len(self.cards)



class Hand:

    def __init__(self, name='Dealer'):
        self.name= name
        self.cards= []
        self.value= 0
        self.aces= 0

    def add_card(self, card):
        self.cards.append(card)
        self.value+= card.value
        if card.rank== 1:
            self.aces+= 1

    def ace_adjust(self):
        while self.value>21 and self.aces:
            self.value-= 10
            self.aces-= 1

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.cards)

class Chips:
    def __init__(self):
        self.total= 100
        self.bet= 0

    def win_bet(self):
        self.total+= self.bet *2




def take_bet(chips):
    while True:
        try:
            print("You have {} chips. What is your bet? ".format(chips.total))
            chips.bet= int(input(''))
            if chips.bet> chips.total:
                print("You don't have enough chips!")
                print("Max bet is {}".format(chips.total))
                continue

        except:
            print("\nAn error occured! ")
            continue
        else:
            print("You have {} chips left.\n".format(chips.total))
            break

    chips.total-= chips.bet


def hit(deck, hand):
    card= deck.deal()
    hand.add_card(card)
    return card


def hit_or_stand(deck, hand):
    print("Your turn\n")
    while True:
        result=input("Do you want to hit or stand? \n")

        if result[0].lower()== 'h':
            card= hit(deck, hand)
            print("You took {}".format(card))
            break
        elif result[0].lower()== 's':
            break
        else:
            print("\nInput HIT or STAND: ")
            continue


def show_cards(hand, show=1):
    if hand.name== 'Player':
        print("Your cards:\n")
    else:
        print("{}'s cards:\n".format(hand.name))
    if show:
        for card in hand.cards:
            print("| {} ".format(card), end=" ")
        print('|', end='')
        print('\n')
    else:
        print("| <<hidden card>> ", end='')
        for i in range(1, len(hand.cards)):
            print("| {} ".format(hand.cards[i]), end=" ")
        print('|', end='')
        print('\n')

def check_win():
    return game.player.value > game.dealer.value

def check_lose():
    return game.player.value > 21

class BlackjackGame:
    def __init__(self):
        self.deck= Deck()
        self.deck.shuffle()
        self.player= Hand('Player')
        self.dealer= Hand()

        hit(self.deck, self.player)
        hit(self.deck, self.player)
        hit(self.deck, self.dealer)
        hit(self.deck, self.dealer)


    def play(self, chips):
        print("Welcome to Blackjack Game! Your aim is to get as close to 21 as possible, sooner than dealer.")
        print("But be careful! If your cards' values will exceed 21, you'll lose!\n")
        print("Let's get started!\n")


        while True:
            take_bet(chips)
            show_cards(self.player)
            show_cards(self.dealer, 0)
            hit_or_stand(self.deck, self.player)
            show_cards(self.player)
            if check_lose() and self.player.aces:
                self.player.ace_adjust()
                print("Your ace's value is changing to 1 now! ")
            elif check_lose():
                print("You exceeded 21!\n Dealer wins")
                break
            show_cards(self.dealer)
            input("Dealer's turn. Tap to continue \n")
            if self.dealer.value<17:
                hit(self.deck, self.dealer)
            show_cards(self.player)
            show_cards(self.dealer)
            if check_win():
                print("You win!\n You earned {} chips.\n".format(chips.bet))
                chips.win_bet()
                break
            else:
                print("Dealer wins!")
                break

#GAMEPLAY

player_chips= Chips()

while playing_game:
    game= BlackjackGame()
    game.play(player_chips)
    print("The amount of your chips is {}".format(player_chips.total))
    try:
        result = input("\nDo you want to play again?")
        if result[0]== 'y':
            continue
        else:
            break
    except:
        break

print("You ended the game with {} chips".format(player_chips.total)) 













