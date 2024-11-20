import random

def calculate_score(card_dict):
    score = 0
    for card_type, count in card_dict.items():
        if card_type == 'R':
            score += count * 10
        elif card_type == 'Q':
            score += count * 10
        elif card_type == 'P':
            score += count * 7
        elif card_type == 'S':
            score += count * 5
    return score

def create_deck():
    deck = []
    for card_type in ['R', 'Q', 'P', 'S']:
        for card_num in range(1, 5):
            deck.append((card_type, card_num))
    return deck

num_flips = int(input("Enter number of time player can flip the card\n"))

arun_cards = {'R' : 0, 'Q' : 0, 'P' : 0, 'S' : 0}
arya_cards = {'R' : 0, 'Q' : 0, 'P' : 0, 'S' : 0}
card_deck = create_deck()
random.shuffle(card_deck)

for i in range(num_flips):
    print("Arun flip the card")
    card_type, card_num = card_deck.pop(0)
    print(card_type)
    print(card_num)
    arun_cards[card_type] += int(card_num)

    print("Arya flip the card")
    card_type, card_num = card_deck.pop(0)
    print(card_type)
    print(card_num)
    arya_cards[card_type] += int(card_num)

arun_score = calculate_score(arun_cards)
arya_score = calculate_score(arya_cards)

print(f"Total scores {arun_score} {arya_score}")

if arun_score > arya_score:
    print("Arun won the game")
elif arya_score > arun_score:
    print("Arya won the game")
else:
    print("Game tied")
