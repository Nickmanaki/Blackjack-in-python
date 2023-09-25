import random

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

playing = True


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
        print "Player's cards:", player
        if playersum < 21:
            answer = raw_input("HIT or STAND ???: ")
        elif playersum == 21:
            print "BLACKJACK!!!"
            answer = "Stand"

    playing = False

#=================================================================
dealing = True


while dealing:
    print dealer
    if dealersum < 17:
        random6 = random.randint(0, L-1)
        dealer3 = decks[random6]
        decks.pop(random6)
        L = len(decks)
        dealersum += dealer3
    dealing = False

print dealer


