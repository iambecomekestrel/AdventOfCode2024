with open(r"/Users/taylorhood/Documents/Projects/AdventOfCode2024/day4/data.txt") as file:
    data = file.readlines()

def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data

clean_data = remove_line_break_char(data)


def is_valid(text, row, col):
    return 0 <= row < len(text) and 0 <= col < len(text[0])
        

def get_neighbors(row, col): 

    neighbors = []
    change = [-1, 0, 1] 
    row_index = 0
    col_index = 0 # check top row 
    for row_index in range(len(change)):
        for col_index in range(len(change)):
            neighbors.append([row + change[row_index], col + change[col_index], change[row_index],change[col_index]])
    return neighbors

def check_for_MAS(text, list_of_list):
    # item = [updated_row_value, updated_colum_value, row_change, column_change]
    count = 0
    for item in list_of_list:
        if is_valid(text,item[0],item[1]) and text[item[0]][item[1]] == 'M':
            if is_valid(text,(item[0]+item[2]),(item[1]+item[3])) and text[(item[0]+item[2])][(item[1]+item[3])] == 'A':
                if is_valid(text,(item[0]+2*item[2]),(item[1]+2*item[3])) and text[(item[0]+2*item[2])][(item[1]+2*item[3])] == 'S':
                    count += 1
    return count

    
def find_strings(text): 
    count = 0
    for index_line, line in enumerate(text): 
        for index_char, char in enumerate(line): 
            if char == 'X': 
                neighbors = get_neighbors(index_line, index_char)
                count += check_for_MAS(text,neighbors)
    return count

# print(find_strings(clean_data))