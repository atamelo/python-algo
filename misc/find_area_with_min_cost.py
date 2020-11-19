# given a field split into cells each of which has a cost
# find a RECT_WIDTH x RECT_HEIGHT subarea with minimal cost

def find_area(field, row_count, column_count):
    RECT_WIDTH = 3
    RECT_HEIGHT = 3

    def get_sum_for(field, upper_left_row, upper_left_column):
        s = 0
        for row in range(upper_left_row, upper_left_row + RECT_HEIGHT):
            for column in range(upper_left_column, upper_left_column + RECT_WIDTH):
                s += field[row][column]

        return s

    def move_right(field, current_row, current_column, current_sum):
        old_column_sum = 0
        for row in range(current_row, current_row + RECT_HEIGHT):
            old_column_sum += field[row][current_column]

        new_sum = current_sum - old_column_sum
        new_column_sum = 0
        for row in range(current_row, current_row + RECT_HEIGHT):
            new_column_sum += field[row][current_column + RECT_WIDTH]

        new_sum += new_column_sum

        return new_sum

    def move_down(field, curent_row, current_column, current_sum):
        old_row_sum = 0
        for column in range(current_column, current_column + RECT_WIDTH):
            old_row_sum += field[curent_row][column]

        new_sum = current_sum - old_row_sum
        new_row_sum = 0
        for column in range(current_column, current_column + RECT_WIDTH):
            new_row_sum += field[curent_row + RECT_HEIGHT][column]

        new_sum += new_row_sum

        return new_sum

    min_sum = get_sum_for(field, 0, 0)
    curr_sum = min_sum
    first_row_sum = curr_sum
    for row in range(0, row_count - RECT_HEIGHT + 1):
        for column in range(0, column_count - RECT_WIDTH):
            curr_sum = move_right(field, row, column, curr_sum)
            min_sum = min(min_sum, curr_sum)

        # we need to skip 'move_down' if we're scanning the 'last row'
        if row + RECT_HEIGHT < row_count:
            curr_sum = move_down(field, row, 0, first_row_sum)
            min_sum = min(min_sum, curr_sum)
            first_row_sum = curr_sum

    return min_sum


size = 9
field = ['x'] * size

field[0] = [4, 3, 6, 3, 7, 1, 5, 2, 1]
field[1] = [1, 2, 5, 2, 4, 2, 6, 4, 2]
field[2] = [6, 6, 5, 1, 4, 3, 7, 3, 1]
field[3] = [3, 5, 4, 1, 2, 4, 3, 5, 3]
field[4] = [3, 2, 1, 1, 1, 5, 4, 2, 2]
field[5] = [3, 3, 1, 2, 1, 6, 3, 2, 1]
field[6] = [2, 1, 1, 1, 2, 4, 2, 3, 3]
field[7] = [1, 2, 1, 2, 1, 5, 4, 4, 2]
field[8] = [1, 2, 1, 3, 2, 6, 3, 4, 1]

print(find_area(field, len(field), len(field[0])))
