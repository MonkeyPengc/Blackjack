
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


def PlayPoker():
    
    player_name = input('Welcome to BlackJack! What\'s your name? ')
    try:
       player_chips = int(input('Hello, ' + player_name + '! The smallest chip to play is 5, how much do you have? '))
    except ValueError:
       print('Please type a valid number!')
       player_chips = int(input('Hello, ' + player_name + '! The smallest chip to play is 5, how much do you have? '))
    while player_chips >= 5:
        try:
           chip_in = int(input('How many chips do you want to play this time? '))
        except ValueError:
           print('Please type a valid number!')
           chip_in = int(input('How many chips do you want to play this time? '))
        else:
           if chip_in > player_chips:
              print("Sorry, you don't have enough chips to play, please buy more chips...")
              continue
        print("Ok, let's start the game...")
        game, my_current_chip = PokerRule(mychips=player_chips, name=player_name, chipin=chip_in)
        player_chips = my_current_chip
        print(game)
        try:
           asktoplay = int(input('Want to play another game? (yes:1, no:0)'))
        except ValueError:
           print('Please type 1/0!')
           asktoplay = int(input('Another game? (yes:1, no:0)'))
        if asktoplay == 1:
            if player_chips < 5:
                print("Sorry, you don't have enough chips to play, please buy more chips...")
                break
            continue
        else:
            print("Byebye...")
            break


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


