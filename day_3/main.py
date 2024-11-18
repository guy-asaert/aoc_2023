from utils import read_lines
from re import finditer
from collections import namedtuple

SAMPLE_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""



Symbol = namedtuple("Symbol", "row col symbol")
Number = namedtuple("Number", "row col length number")

def run():

    symbols = []
    numbers = []
    number_near_symbol = []
    # for row, row_of_data in enumerate(SAMPLE_INPUT.split('\n')):
    for row, row_of_data in enumerate(read_lines(__file__)):
        for number in finditer(r'\d+', row_of_data):
            # print(f'Number: {number} at location: {location}')
            numbers.append(Number(row, number.span()[0], number.span()[1] - number.span()[0], 
                                  int(number.group(0))))

        for symbol in finditer(r'[^.\d]', row_of_data):
            # print(f'Symbol: {symbol} at location: {location}')
            symbols.append(Symbol(row, symbol.span()[0], symbol.group(0)))

    geared_total = 0
    for symbol in symbols:
        geared_numbers = []
        for number in numbers:
            if number.col - 1 <= symbol.col <= number.col + number.length and \
               number.row - 1 <= symbol.row <= number.row + 1:
                print(f'Number: {number} is near symbol: {symbol}')
                number_near_symbol.append(number.number)
                if symbol.symbol == '*':
                    geared_numbers.append(number.number)

        if len(geared_numbers) == 2:
            geared_total += geared_numbers[0] * geared_numbers[1]

        # if not number_near_symbol or number_near_symbol[-1] != number.number:
        #     print(f'Number {number.number} on row {number.row} is not near any symbol')

    print(f'{len(number_near_symbol)} numbers near symbols: total is {len(numbers)}')
    print(f'Sum of numbers near symbols: {sum(number_near_symbol)}')

    print(f'Geared total: {geared_total}')
    # 284222 is too low
    # 300667 is too low


if __name__ == '__main__':
    run()
