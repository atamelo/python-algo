def generate_all_parens(target_len):

    def generate_parens(string, disbalance_count, next_index, target_len):

        if next_index == target_len:
            print(''.join(string))
            return

        if disbalance_count > 0:
            string[next_index] = ')'
            generate_parens(string, disbalance_count - 1, next_index + 1, target_len)
            string[next_index] = '*'

        characters_left = target_len - next_index
        if disbalance_count < characters_left:
            string[next_index] = '('
            generate_parens(string, disbalance_count + 1, next_index + 1, target_len)
            string[next_index] = '*'

    if target_len & 1 == 1:
        print("Can't be odd.")
        return

    string = ['*'] * target_len
    string[0] = '('
    generate_parens(string, 1, 1, target_len)


generate_all_parens(80)





