from math import log2, log10


def split_by_mask(digits, mask):

    if mask == 0:
        return [digits]

    numbers = []

    current_mask = mask
    current_digits = digits

    while current_mask != 0:
        cut_position = int(log2(current_mask & (-current_mask)) + 1)
        divisor = 10 ** cut_position
        current_digits, number = divmod(current_digits, divisor)
        numbers.append(int(number))
        current_mask >>= cut_position

    numbers.append(int(current_digits))

    return numbers


def enumerate_signs(numbers, target_sum):

    def find_sum(numbers, number_index, current_sum, target_sum, expression, combinations):

        if number_index == len(numbers):
            if current_sum == target_sum:
                combinations.append(list(expression))
            return

        current_number = numbers[number_index]

        current_expression = ['+', current_number]
        expression.append(current_expression)
        find_sum(numbers, number_index + 1, current_sum + current_number, target_sum, expression, combinations)
        expression.pop(len(expression) - 1)

        current_expression = ['-', current_number]
        expression.append(current_expression)
        find_sum(numbers, number_index + 1, current_sum - current_number, target_sum, expression, combinations)
        expression.pop(len(expression) - 1)

    combinations = []
    expression = []
    find_sum(numbers, 0, 0, target_sum, expression, combinations)
    return combinations


def find_number_combinations(digits, target_sum):

    result = []

    digits_len = int(log10(digits)) + 1
    last_cut_position = 2 ** (digits_len - 1)

    for mask in range(0, last_cut_position):
        numbers = split_by_mask(digits, mask)
        combinations = enumerate_signs(numbers, target_sum)
        if combinations:
            result.extend(combinations)

    return result


def print_cobinations(combinations, trailer):

    for combination in combinations:
        for index, (sign, number) in enumerate(reversed(combination)):
            if index == 0 and sign == '+':
                sign = ''
            lead_space = '' if index == 0 else ' '
            trail = '' if index == 0 and sign == '-' else ' '
            print(f'{lead_space}{sign}{trail}{number}', end='')
        print(f' = {trailer}')


n = 6
combinations = find_number_combinations(1245, n)
print_cobinations(combinations, n)
