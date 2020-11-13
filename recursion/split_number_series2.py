def number_from_digits(digits):
    number = 0

    for digit in digits:
        number *= 10
        number += digit

    return number


def all_parts(digits):

    def build_part(digits, start_index, parts, combinations):

        if start_index == len(digits):
            combinations.append(list(parts))
            return

        for i in range(len(digits) - start_index):
            end_index = start_index + i + 1
            part = digits[start_index:end_index]
            parts.append(part)
            build_part(digits, end_index, parts, combinations)
            parts.pop(len(parts) - 1)

    combinations = []
    build_part(digits, 0, [], combinations)
    return combinations


def enumerate_signs(numbers, target_sum):

    def find_sum(numbers, number_index, current_sum, target_sum, expression, combinations):

        if number_index == len(numbers):
            if current_sum == target_sum:
                combinations.append(list(expression))
            return

        current_number = numbers[number_index]
        current_number = number_from_digits(current_number)

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

    parts = all_parts(digits)

    for part in parts:
        combinations = enumerate_signs(part, target_sum)
        if combinations:
            result.extend(combinations)

    return result


def print_cobinations(combinations, trailer):

    for combination in combinations:
        for index, (sign, number) in enumerate(combination):
            if index == 0 and sign == '+':
                sign = ''
            lead_space = '' if index == 0 else ' '
            trail = '' if index == 0 and sign == '-' else ' '
            print(f'{lead_space}{sign}{trail}{number}', end='')
        print(f' = {trailer}')


n = 100
combinations = find_number_combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], n)
print_cobinations(combinations, n)
