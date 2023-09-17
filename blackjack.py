import random
class BlackJack():
    def __init__(self, deck = []):
        self.deck = deck
        self.startingDeck = []
        self.playerHand = []
        self.dealerHand = []
        
    def unshuffeld (self):    
        for i in ['Spade','Heart','Dimond','Club']:
            for h in range (2,11):
                self.deck.append(f'{h} of {i}')
        
            for j in ['Jack','Queen','King','Ace']:
                self.deck.append(f'{j} of {i}')
        return self.deck

    def shuffeld (self):    
        
        for i in range (len(self.deck)-1,0,-1):
            j = random.randint(0, i+1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        self.startingDeck = self.deck
        return self.startingDeck
    
    def player (self):

        for i in self.startingDeck:
            if len(self.playerHand) < 3:
                self.playerHand.append(i)
                self.startingDeck.remove(i)
        print (self.startingDeck)
        return f'player hand is {self.playerHand[0]} and {self.playerHand[1]}'
    
    def dealer (self):
        for i in self.startingDeck:
            if len(self.dealerHand) < 3:
                self.dealerHand.append(i)
                self.startingDeck.remove(i)
        print (self.startingDeck)
        return f'dealer hand is {self.dealerHand[0]} and XXXXXX'
    
    def playerhit (self):
        if len(self.playerHand) < 4:
            self.playerHand.append(self.startingDeck[0])
            self.startingDeck.remove(self.startingDeck[0])
            return f'player hand is {self.playerHand[0]}, {self.playerHand[1]}, {self.playerHand[2]}'
        
    def dealerhit(self):
        if len(self.dealerHand) < 4:
            self.dealerHand.append(self.startingDeck[0])
            self.startingDeck.remove(self.startingDeck[0])
            return f'Dealer hand is {self.dealerHand[0]}, {self.dealerHand[1]}, {self.dealerHand[2]}'

        
    
   

game = BlackJack()
print(game.unshuffeld())
print(game.shuffeld())
print(game.player())
print (game.dealer())
print (game.playerhit())
print (game.dealerhit())




    
    