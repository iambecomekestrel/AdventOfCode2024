import pdb
import re
with open(r"/Users/redacted/Documents/Projects/AdventOfCode2024/day3/data.txt") as file:
    data = file.readlines()

def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data

clean_data = remove_line_break_char(data)

# print(clean_data[:2])

def get_multiples(aoc_data):
    multiples = []
    for item in aoc_data:
        multiples += re.findall(r"mul\((\d+),(\d+)\)", item)
    result = 0
    for tuple in multiples:
        result += int(tuple[0])*int(tuple[1])

    return result

def get_do_dont_multiples(aoc_data):
    multiples = []
    for item in aoc_data:
        for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", item):
            if match.group(0).startswith('mul'):
                num1, num2 = match.groups()
                multiples.append((num1, num2))
            elif match.group(0) == 'do()':
                multiples.append('do()')
            elif match.group(0) == "don't()":
                multiples.append("don't()")
        

    result = 0
    do = True
    for item in multiples:
        if item == "don't()":
            do = False
        if item == "do()":
            do = True
        if item != "do()" and item != "don't()" and do == True:
            result += int(item[0])*int(item[1])

    return result


print(get_do_dont_multiples(clean_data))