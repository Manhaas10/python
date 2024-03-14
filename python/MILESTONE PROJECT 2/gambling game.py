import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing=True
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.all_cards)
    def __str__(self):
        dec=''
        for card in self.all_cards:
            dec+='\n'+card.__str__()
        return 'deck is'+dec
    def grab_one_card(self):
        return self.all_cards.pop()
class Hand:
    def __init__(self):
        self.ace=0
        self.value=0
        self.cards=[]
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.ace+=1
    def firefist_ace(self):
        while self.value>21 and self.ace>=1:
            self.value-=10
            self.ace-=1
class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
def take_bet():
    bet=int(input("enter the bet you r going to put:"))
    return bet
def hit(deck,hand):
    hand.add_card(deck.grab_one_card())
    hand.firefist_ace()
def hit_or_stand(deck,hand):
    global playing
    while True:
        scam=input("hit or stand:")
        scam.lower()
        if scam=='hit':
            return hit(deck,hand)
        elif scam=='stand':
            playing=False
        else:
            print('try again')
            continue
        break
def show_some(player,dealer):
    print("Dealers Hand:")
    print("First card hidden!")
    print(dealer.cards[1])
    print("player's hand:") 
    for card in player.cards:
        print(card)
def show_all(player,dealer):
    print("Dealers Hand:")
    for card in dealer.cards:
        print(card)
    print(f'total count is {dealer.value}')
    print("player's hand:") 
    for card in player.cards:
        print(card)
def player_busts(chips):
    print("player lost the bet")
    chips.lose_bet()
def player_wins(chips):
    print("player won the bet")
    chips.win_bet()
def dealer_busts(chips):
    print("dealer lost")
    chips.win_bet()
def dealer_wins(chips):
    print("dealer won")
    chips.lose_bet()
def push(chips):
    print("tie!push")
hanger=True
while hanger:
    chips=Chips()
    chips.bet=take_bet()
    player=Hand()
    dealer=Hand()
    deck=Deck()
    deck.shuffle()
    player.add_card(deck.grab_one_card())
    player.add_card(deck.grab_one_card())
    dealer.add_card(deck.grab_one_card())
    dealer.add_card(deck.grab_one_card())
    print(player.value)
    while playing:
        hit_or_stand(deck,player)
        show_some(player,dealer)
        print(player.value)
        if player.value>=21:
            player_busts(chips)
            print('bet amount:',chips.total)
            break
        elif playing==False:
            show_all(player,dealer)
            while dealer.value<=player.value:
                hit(deck,dealer)
            print("dealer's hand:")
            for card in dealer.cards:
                print(card)
            if dealer.value>20:
                dealer_busts(chips)
                print('bet amount:',chips.total)
                break
            elif dealer.value>player.value:
                dealer_wins(chips)
                print('bet amount:',chips.total)
                break

    tot=input('do you want to play again Y or N :')
    ans=tot.upper()
    if ans=='Y':
        hanger=True
        playing=True
    elif ans=='N':
        hanger=False
    else:
        print("valid input")
        
            
                
        
        
            













    
        





