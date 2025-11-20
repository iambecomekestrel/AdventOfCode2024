with open(r"/Users/redacted/Documents/Projects/AdventOfCode2024/day4/data.txt") as file:
    data = file.readlines()

def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data

clean_data = remove_line_break_char(data)

def is_valid(text, row, col):
    return 0 <= row < len(text) and 0 <= col < len(text[0])


def get_first_cross(row, col): 

    crosses = []
    crosses.append([[row -1, col -1], [row +1, col + 1]])

    return crosses

def get_criss_cross(cross_coordinates_as_tuple):

    [[Top1,Top2],[Bot1,Bot2]] = cross_coordinates_as_tuple
    diagonal = [[Top1, Top2], [Bot1, Bot2]]
    counter_diagonal = [[Top1, Bot2], [Bot1, Top2]]

    return diagonal,counter_diagonal

def check_for_X_MAS(text, list_of_cross_coordinates_as_tuples):
    count = 0
    for cross in list_of_cross_coordinates_as_tuples:
        first = ['M', 'S']
        second = ['M', 'S']
        diagonals,counter_diagonals = get_criss_cross(cross)
        [[D1, D2], [D3, D4]] = diagonals
        [[CD1, CD2], [CD3, CD4]] = counter_diagonals
        if is_valid(text,D1,D2) and text[D1][D2] in first:
            first.remove(text[D1][D2])
            if not (is_valid(text,D3,D4) and text[D3][D4] in first):
                continue
            if is_valid(text,CD3, CD4) and text[CD1][CD2] in second:
                second.remove(text[CD1][CD2])
                if is_valid(text,CD3, CD4) and text[CD3][CD4] in second:
                        count += 1

    return count


def find_cross_strings(text): 
    count = 0
    for index_line, line in enumerate(text): 
        for index_char, char in enumerate(line):
            if char == 'A': 
                neighbors = get_first_cross(index_line, index_char)
                count += check_for_X_MAS(text,neighbors)
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


print(find_cross_strings(clean_data))
