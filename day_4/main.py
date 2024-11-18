from utils import read_lines
from re import finditer
from collections import defaultdict, namedtuple

SAMPLE_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

CardDetails = namedtuple("CardDetails", "card_number results numbers")

def run():

    points = 0

    cards = list()
    cards_count = defaultdict(lambda: 1)
    # for row_of_data in SAMPLE_INPUT.split('\n'):
    for row_of_data in read_lines(__file__):
        card_name, card_numbers = row_of_data.split(':')
        card_number = int(card_name.split()[1])
        results, numbers = card_numbers.split('|')
        result_numbers = set([int(num) for num in results.split()])
        number_numbers = set([int(num) for num in numbers.split()])
        cards.append(CardDetails(card_number, result_numbers, number_numbers))

    for card in cards:
        matching = card.results.intersection(card.numbers)

        if not cards_count.get(card.card_number):
            cards_count[card.card_number] = 1

        for i in range(1, len(matching) + 1):
            if card.card_number + i <= len(cards):
                cards_count[card.card_number + i] += cards_count[card.card_number]

        if matching:
            points += pow(2, len(matching) - 1)
            pass


    print(points)
    print(sum(cards_count.values()))
    # 14406053is too low

if __name__ == '__main__':
    run()
