import numpy
from utils import read_lines

puzzle = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

max_colours = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# RED = 12
# GREEN = 13
# BLUE = 14

possible_games_sum_ids = 0
minimum_game_pow = 0

# for game_info in puzzle.split('\n'):
for game_info in read_lines(__file__):
    min_colours = dict()
    game_number, game = game_info.split(':')
    game_number = int(game_number.split(' ')[-1])

    possible_game = True
    for selection_from_bag in game.split(';'):
        for colour_count in selection_from_bag.split(','):
            count, colour = colour_count.strip().split(' ')
            count = int(count)

            if count > max_colours[colour]:
                possible_game = False

            if colour not in min_colours:
                min_colours[colour] = count
            elif count > min_colours[colour]:
                min_colours[colour] = count

        # if not possible_game:
        #     break
    if possible_game:
        possible_games_sum_ids += game_number

    minimum = numpy.prod(list(min_colours.values()))
    print(f'xxxx {minimum}')
    minimum_game_pow += minimum

print(f'possible {possible_games_sum_ids}')
print(f'min {minimum_game_pow}')
