from collections import Counter

CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}

HAND_VALUES = {
    'five_of_a_kind': 7,
    'four_of_a_kind': 6,
    'full_house': 5,
    'three_of_a_kind': 4,
    'two_pair': 3,
    'one_pair': 2,
    'high_card': 1
}


def rank_hands(hands: list[str]) -> str:
    hand_types = {}
    for hand in hands:
        adjusted_hand = get_joker_adjusted_hand(hand)
        hand_types[hand] = match_hand_to_type(adjusted_hand)
    hands.sort(key=lambda x: (HAND_VALUES[hand_types[x]], [CARD_VALUES[y] for y in x]))

    return hands


def get_joker_adjusted_hand(hand: str) -> str:
    if 'J' in hand:
        # Identify most frequent card and match joker to that
        # If two or more equally frequent numbers, match joker to highest number
        counts = Counter([n for n in hand if n != 'J'])
        most_frequent_cards = [k for k, v in counts.items() if v == max(counts.values())]
        if not len(most_frequent_cards):
            hand = 'A'*5
        elif len(most_frequent_cards) >= 1:
            hand = hand.replace("J", max(most_frequent_cards, key= lambda x: CARD_VALUES[x]))

    return hand


def match_hand_to_type(hand: str) -> str:
    card_counts = sorted(Counter(hand).values(), reverse=True)
    match card_counts:
        case [5]:
            return "five_of_a_kind"
        case [4, 1]:
            return "four_of_a_kind"
        case [3, 2]:
            return "full_house"
        case [3, 1, 1]:
            return "three_of_a_kind"
        case [2, 2, 1]:
            return "two_pair"
        case [2, 1, 1, 1]:
            return "one_pair"
        case _:
            return "high_card"


def get_winnings(hands: list[str], bids: dict) -> list[int]:
    winnings = []

    for i in range(len(hands)):
        bid = bids[hands[i]]
        winnings.append(bid*(i + 1))

    return winnings


def presort_hands_and_bids(hand_list: list[list]) -> list[list]:
    sorted_hand_list = []
    for hand in hand_list:
        hand, bid = hand
        hand = "".join(sorted(hand, key=lambda x: (Counter(hand)[x], CARD_VALUES[x]), reverse=True))
        sorted_hand_list.append([hand, bid])
        
    return sorted_hand_list


def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n")
            hand_list = [n.split(" ") for n in data]
            bids = {k:int(v) for k, v in hand_list}
            hands = [n[0] for n in hand_list]

        ranked_hands = rank_hands(hands)
        winnings = get_winnings(ranked_hands, bids)
        solution = sum(winnings)

        solutions.append(solution)
    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[1]}")

    return solutions


if __name__ == "__main__":
    main()