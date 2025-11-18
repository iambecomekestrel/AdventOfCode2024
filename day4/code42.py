with open(r"/Users/redacted/Documents/Projects/AdventOfCode2024/day4/data.txt") as file:
    data = file.readlines()

def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data


clean_data = [list(line) for line in data]

clean_data1 = remove_line_break_char(data)

def is_valid(text, row, col):
    return 0 <= row < len(text) and 0 <= col < len(text[0])


def get_first_diagonal(row, col): 

    diagonals = []
    
    diagonals.append([[row -1, col -1], [row +1, col + 1]])
    return diagonals

def get_diagonal_x_set(list_of_tuples):
    # item = [[pair1_row_value, pair1_colum_value], [pair2_row_value, pair2_column_value]]
    item = list_of_tuples
    diagonal = [[item[0][0], item[0][1]], [item[1][0], item[1][1]]]
    counter_diagonal = [[item[0][0], item[1][1]], [item[1][0], item[0][1]]]

    # result = [[[pair1_row_value, pair1_colum_value], [pair2_row_value, pair2_column_value]], [[pair1_row_value, pair1_colum_value], [pair2_row_value, pair2_column_value]]]
    # result[0] (diagonal) = [[pair1_row_value (row), pair1_colum_value (col)], [pair2_row_value, pair2_column_value]]
    # result[1] (cross-diagonal) = [[pair1_row_value, pair1_colum_value], [pair2_row_value, pair2_column_value]]
    return diagonal,counter_diagonal

def check_for_MAS(text, list_of_list):
    # item = [[pair1_row_value, pair1_colum_value], [pair2_row_value, pair2_column_value]]
    count = 0
    first = ['M', 'S']
    second = ['M', 'S']
    for item in list_of_list:
        diagonals,cross_diagonals = get_diagonal_x_set(item)
        if is_valid(text,diagonals[0][0],diagonals[0][1]) and text[diagonals[0][0]][diagonals[0][1]] in first:
             first.remove(text[diagonals[0][0]][diagonals[0][1]])
             if is_valid(text,diagonals[1][0],diagonals[1][1]) and text[diagonals[1][0]][diagonals[1][1]] in first:
                    if is_valid(text,cross_diagonals[1][0], cross_diagonals[1][1]) and text[cross_diagonals[0][0]][cross_diagonals[0][1]] in second:
                        second.remove(text[cross_diagonals[0][0]][cross_diagonals[0][1]])
                        if is_valid(text,cross_diagonals[1][0], cross_diagonals[1][1]) and text[cross_diagonals[1][0]][cross_diagonals[1][1]] in second:
                            count += 1
    return count


def find_cross_strings(text): 
    count = 0
    for index_line, line in enumerate(text): 
        for index_char, char in enumerate(line):
            if char == 'A': 
                neighbors = get_first_diagonal(index_line, index_char)
                count += check_for_MAS(text,neighbors)
    return count


test =[
'MMMSXXMASM',
'MSAMXMSMSA',
'AMXSXMAAMM',
'MSAMASMSMX',
'XMASAMXAMM',
'XXAMMXXAMA',
'SMSMSASXSS',
'SAXAMASAAA',
'MAMMMXMMMM',
'MXMXAXMASX']


print(find_cross_strings(clean_data1))
