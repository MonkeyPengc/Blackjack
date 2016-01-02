
# brief: BlackJack poker game, enjoy! (Command-line only)
# author: Cheng Peng

# -----------------------------------------------------------------------------
# define a class that contains poker methods

class BlackJack:
    def __init__(self, chips, name=None, mydeck=None):
        self.chips = chips
        self.name = str(name)
        self.deck = mydeck
        self.point = 0
        self.hands = []
        self.new_value = []
        
    def new_hands(self):
        self.hands.append(self.deck.pop())
        self.point = self.face_value()
        self.hands.append(self.deck.pop())
        self.point = self.face_value()
    
    def isAce(self, card):
        return card == 1
    
    def face_value(self):
        value = ['-A23456789TJQK'.index(r) for r,s in self.hands]
        if len(value) == 1 and self.isAce(value[0]):
            self.new_value.append(11)
        elif len(value) >= 2 and self.isAce(value[-1]) and (sum(self.new_value)+11) <= 21:
            self.new_value.append(11)
        elif value[-1] > 10:
            self.new_value.append(10)
        else:
            self.new_value.append(value[-1])
    
        return sum(self.new_value)
    
    def add_card(self):
        self.hands.append(self.deck.pop())
        self.point = self.face_value()
        
    def __str__(self):
        return self.name + "'s cards " + str(self.hands) + " has " + str(self.point) + " points."


# -----------------------------------------------------------------------------
# deine a function that implements blackjack following the poker rule

def PokerRule(mychips=50, name='Jack', chipin=10):
    
    import random
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    random.shuffle(deck)
    player = BlackJack(chips=mychips, name=name, mydeck=deck)
    player.new_hands() 
    print(player)

    if player.point > 21:
        player.chips -= chipin
        return "You lose! Now you have " + str(player.chips) + " dollars.", player.chips
    elif player.point == 21:
        player.chips += chipin
        return "You win! Now you have " + str(player.chips) + " dollars.", player.chips
    else:
        while(int(input('Do you want an extra card? (yes:1, no:0)'))):
            player.add_card()
            print(player)
            if player.point >= 21:
                break
            else:
                continue
        if player.point < 21:
            print("Now, it's my turn...")
            house = BlackJack(chips=500, name='House', mydeck = player.deck)
            house.add_card()
            print(house)
            while house.point < player.point:
                print("I need an extra card...")
                house.add_card()
                print(house)
            if house.point <= 21 and house.point >= player.point:
                player.chips -= chipin
                return "You lose! Now you have " + str(player.chips) + " dollars.", player.chips
            else:
                player.chips += chipin
                return "You win! Now you have " + str(player.chips) + " dollars.", player.chips
        elif player.point == 21:
            player.chips += chipin
            return "You win! Now you have " + str(player.chips) + " dollars.", player.chips
        else:
            player.chips -= chipin
            return "You lose! Now you have " + str(player.chips) + " dollars.", player.chips


# -----------------------------------------------------------------------------
# define a function that works as a House of the poker game

def PlayPoker():
    
    player_name = input('Welcome to BlackJack! What\'s your name? ')
    player_chips = int(input('Hello, ' + player_name + '! The smallest chip to play is 5, how much do you have? '))
    while player_chips >= 5:
        chip_in = int(input('How much chips do you want to play this time? '))
        if chip_in > player_chips:
            print("Sorry, you don't have enough chips to play, please buy more chips...")
            continue
        print("Ok, let's start the game...")
        game, my_current_chip = PokerRule(mychips=player_chips, name=player_name, chipin=chip_in)
        player_chips = my_current_chip
        print(game)
        asktoplay = int(input('Want to play another game? (yes:1, no:0)'))
        if asktoplay == 0:
            print("Byebye...")
            break
        else:
            if player_chips < 5:
                print("Sorry, you don't have enough chips to play, please buy more chips...")
                break
            continue

# -----------------------------------------------------------------------------
# run script

if __name__ == "__main__":

    PlayPoker()




