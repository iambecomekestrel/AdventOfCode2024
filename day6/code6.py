with open(r"/Users/redacted/Documents/Projects/AdventOfCode2024/day6/data.txt") as file:
    data = file.readlines()


with open(r"/Users/redacted/Documents/Projects/AdventOfCode2024/day6/test.txt") as file:
    test = file.readlines()

def data_cleaner(data):
    result = []
    for x in range(len(data)):
        line = []
        for y in range(len(data[x])-1):
            line.append(data[x][y])
        result.append(line)
    return result

AOC_DATA = data_cleaner(data)


TEST_DATA = data_cleaner(test)


def is_valid(coordinates_and_data):
    row,col,data = coordinates_and_data
    return 0 <= row < len(data)-1 and 0 <= col < len(data[0])-1


def get_location(data):
    for irow,row in enumerate(data):
        if '^' in row:
            icol = row.index('^')
            return irow,icol


def move(guard_location,guard):
    row,col,data = guard_location
    directions = {
        '^': (-1, 0, '>'),  # up: row-1, col+0, turn to '>'
        '>': (0, 1, 'v'),   # right: row+0, col+1, turn to 'v'
        'v': (1, 0, '<'),   # down: row+1, col+0, turn to '<'
        '<': (0, -1, '^')   # left: row+0, col-1, turn to '^'
        }   
    row_change,col_change,turn = directions[guard]
    row_dif = row + row_change
    col_dif = col + col_change
    move = data[row_dif][col_dif]
    count = 0
    new_progress = True
    if move == '.':
        count += 1
        move = data[row_dif][col_dif] = guard
        curr_position = data[row][col] = 'X'
    if move == 'X':
        move = data[row_dif][col_dif] = guard
        new_progress = False
    if move == '#':
        curr_position = data[row][col] = turn
        new_progress = False
        return row,col,count,turn,new_progress
    return row_dif,col_dif,count,guard,new_progress

def move_forward(row,col,data):
    # figure out the direction to more
    # move that direct until '#'
    # turn all the '.' into 'X'
    # count x's for running total
    curr_row = row
    curr_col = col
    count = 0
    guard = data[curr_row][curr_col] #a direction
    guard_location = curr_row,curr_col,data
    progress = bool   
    while is_valid(guard_location): 
        # print(f"cur_row== {curr_row}, curr_col= {curr_col}, count == {count}, guard == {guard}, progress == {progress}")
        
        new_row,new_col,count_update,guard_moved,new_progess = move(guard_location,guard)
        count += count_update
        curr_row = new_row
        curr_col = new_col
        guard = guard_moved
        progress = new_progess
        guard_location=curr_row,curr_col,data

    if progress == True:
        count += 1

    return count




# print(get_location(TEST_DATA))
row,col = (get_location(AOC_DATA))
print(move_forward(row,col,AOC_DATA))
# print(test[:2])
# print(clean_data[:4])
