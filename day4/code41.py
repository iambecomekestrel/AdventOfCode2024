with open(r"/Users/redacted/Documents/Projects/AdventOfCode2024/day4/data.txt") as file:
    data = file.readlines()

def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data

clean_data = remove_line_break_char(data)


def is_valid(text, row, col):
    return 0 <= row < len(text) and 0 <= col < len(text[0])
        

def get_neighbors_locations(row, col): 
    """returns coordinates for the 8 adjacent neighbors, if inside matrix"""
    neighbors = []
    change = [-1, 0, 1] 
    for row_change in range(len(change)):
        for col_change in range(len(change)):
            neighbors.append([row + change[row_change], col + change[col_change], change[row_change],change[col_change]])
    return neighbors

def count_xmas_from_neighbors(text, neighbors):
    count = 0
    for neighbor in neighbors:
        row, col, row_change, col_change = neighbor
        if not (is_valid(text,row,col) and text[row][col] == 'M'):
            continue
        if not (is_valid(text,row+row_change,col+col_change) and text[row+row_change][col+col_change] == 'A'):
            continue
        if is_valid(text,row+2*row_change,col+2*col_change) and text[row+2*row_change][col+2*col_change] == 'S':
            count += 1
    return count

    
def count_xmas_patterns(text): 
    count = 0
    for index_line, line in enumerate(text): 
        for index_char, char in enumerate(line): 
            if char == 'X': 
                neighbors = get_neighbors_locations(index_line, index_char)
                count += count_xmas_from_neighbors(text,neighbors)
    return count

print(count_xmas_patterns(clean_data))
