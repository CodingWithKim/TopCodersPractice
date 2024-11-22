# define high
high = [1,11,12,13]

# define a dictionary for high card, it served for both drawing and scoring
draw_score = {
    1 : 4,
    11 : 1,
    12 : 2,
    13 : 3
}

# define is_high function
def is_high(card_no):
    # return 0 if no matches
    return draw_score.get(card_no, 0)

# define scoring
def score(sub_list, drawn_card_no):
    for i in sub_list:
        if i in high:
            return 0
    return draw_score[drawn_card_no]


# define draw card
def draw_card(input_card_deck: list[int]):
    current = "A"
    counter = 0
    a_total = 0
    b_total = 0
    while input_card_deck:
        counter += 1
        drawn_card = input_card_deck.pop(0)
        need_draw = is_high(drawn_card)

        if need_draw > 0:
            # should implement one more check
            # if there is no card left to draw
            # i.e. you draw card 11 but there is no card left to draw
            drawn_more = [input_card_deck.pop(0) for _ in range(need_draw)]
            mark = score(drawn_more, drawn_card)
            if current == "A":
                a_total += mark
            else:
                b_total += mark
            if mark != 0:
                print(f"Player {current} scores: {mark} point(s)")
        # counter can be removed and replace the below section with
        # current = "B" if current == "A" else "A"
        if counter % 2 == 0:
            current = "A"
        else:
            current = "B"
    return a_total, b_total


card_deck_size = int(input())
card_deck = [int(input()) for _ in range(card_deck_size)]
result_a, result_b = draw_card(card_deck)
print(f"Player A total score: {result_a} point(s)")
print(f"Player B total score: {result_b} point(s)")
