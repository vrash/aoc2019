from copy import deepcopy

with open("/Users/vrashabhirde/Desktop/input.txt") as f:
    lines = f.read().strip("\n")
    lines = lines.split("\n\n")
    deck1 = lines[0].split("\n")[1:]
    deck2 = lines[1].split("\n")[1:]
    deck1 = list(map(int,deck1))
    deck2 = list(map(int,deck2))
    deck1_1 = deepcopy(deck1)
    deck2_2 = deepcopy(deck2)

def printscore(deck1,deck2):
    if(deck1):
        print("Ans: ", sum((i+1)*v for i,v in enumerate(deck1[::-1])))
    else:
        print("Ans: ", sum((i+1)*v for i,v in enumerate(deck2[::-1])))

def war(deck1,deck2):
    while len(deck1)>0 and len(deck2)>0:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.extend([card1,card2])
        else:
            deck2.extend([card2,card1])

def combat(deck1,deck2):
    handseen = set()
    while len(deck1)>0 and len(deck2)>0:
        #check for hand seen previously
        if (tuple(deck1),tuple(deck2)) in handseen:
            #base
            return True
        handseen.add((tuple(deck1),tuple(deck2)))
        #print("Seen: ", seen)
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if len(deck1) >= card1 and len(deck2) >= card2:
            #sub flow
            #print("DECK1:",deck1)
            #print("DECK2:",deck2)
            winner = combat(deck1[:card1], deck2[:card2])
            if winner:
                deck1.extend([card1,card2])
            else:
                deck2.extend([card2,card1])
        else:
            #normal game flow
            if card1 > card2:
                deck1.extend([card1,card2])
            else:
                deck2.extend([card2,card1])
    return len(deck1)>0

#war, what is it good for?
war(deck1,deck2)
printscore(deck1,deck2)
combat(deck1_1,deck2_2)
printscore(deck1_1,deck2_2)