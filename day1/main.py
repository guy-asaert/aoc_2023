from utils import read_lines
puzzle = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteent"""

total = 0
# for line in puzzle.split('\n'):
#     numbers = [c for c in line if c.isnumeric()]
#     total += int(numbers[0] + numbers[-1])

STRING_NUMBER = {
    'one': 'o1ne',
    'two': 't2wo',
    'three': 'th3ree',
    'four': 'fo4ur',
    'five': 'fi5ve',
    'six': 's6ix',
    'seven': 'se7ven',
    'eight': 'ei8ght',
    'nine': 'ni9ne',
}

# for line in puzzle.split('\n'):
for line in read_lines(__file__):
    for num_string, num_digit in STRING_NUMBER.items():
        line = line.replace(num_string, num_digit)
    numbers = [c for c in line if c.isnumeric()]
    total += int(numbers[0] + numbers[-1])

print(total)