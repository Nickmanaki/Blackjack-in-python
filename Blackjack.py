import random
import time

def dealerdef(deal):
    for i in range(len(deal)):
        if i == 0:
           print "Dealer's card:",;
        print str(deal[i])

def playerdef(play):
    for i in range(len(play)):
        if i == 0:
           print "Player's card:",;
        print str(play[i])

decks = []

for i in range (1,11):
    for j in range (4):
        decks.append(i)

for i in range (4):
    decks.append("K")
    decks.append("Q")
    decks.append("J")

L= len(decks)
dealer = []
player = []


random1 = random.randint(0, L-1)  #MAKE INTO FUCKING FUNCTION RETARD
player1 = decks[random1]
decks.pop(random1)
L = len(decks)
random2 = random.randint(0, L-1)
player2 = decks[random2]
decks.pop(random2)
L = len(decks)
random3 = random.randint(0, L-1)
dealer1 = decks[random3]
decks.pop(random3)
L = len(decks)
random4 = random.randint(0, L-1)
dealer2 = decks[random4]
decks.pop(random4)
L = len(decks)
player.append(player1)
player.append(player2)
dealer.append(dealer1)
dealer.append(dealer2)

print "Dealer's cards:", dealer[0], "x"
print "Player's cards:", player



for i in range(2):
    if player[i] == "Q" or player[i] == "K" or player[i] == "J":
        player[i] = 10
    if dealer[i] == "Q" or dealer[i] == "K" or dealer[i] == "J":
        dealer[i] = 10

playersum = player[0] + player[1]
dealersum = dealer[0] + dealer[1]

playing = True

while playing:
    answer = raw_input("Hit or Stand???: ")

    while answer == "Hit" and playersum < 21:
        random5= random.randint (0, L-1)
        player3 = decks[random5]
        addition = player3
        decks.pop(random5)
        L = len(decks)
        if addition == "Q" or addition == "K" or addition == "J":
            addition = 10
        player.append(player3)
        playersum += addition
        print "Dealer's cards:", dealer[0], "X"
        playerdef(player)
        if playersum < 21:
            answer = raw_input("HIT or STAND ???: ")
        elif playersum == 21:
            print "BLACKJACK!!!"
            answer = "Blackjack"
        else:
            print "BUST"
            answer = "Bust"
    playing = False


#=================================================================
    
dealing = True

while dealing:
    while dealersum < 17:
        random6 = random.randint(0, L-1)
        dealer3 = decks[random6]
        addition = dealer3
        decks.pop(random6)
        L = len(decks)
        if addition == "Q" or addition == "K" or addition == "J":
            addition = 10
        dealer.append(dealer3)
        dealersum += addition
        dealerdef(dealer)
        playerdef(player)
        time.sleep(1.5)   
    dealing = False

if playersum > dealersum and answer != "Bust":
    print "WINNER WINNER!"
elif playersum == dealersum and answer == "Stand":
    print "PUSH!"
elif playersum == dealersum and answer == "Blackjack":
    print "PUSH :("
else:
    print "You lose!"


