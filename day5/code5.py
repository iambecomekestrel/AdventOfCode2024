import re
import functools
with open(r"/Users/redacted/Documents/Projects/AdventOfCode2024/day5/data.txt") as file:
    data = file.read()


def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data

def get_rules(text):
    rules = re.findall(r"(\d+)\|(\d+)",text)
    rules_dict = {}
    for rule in rules:
        if rules_dict.get(rule[0]):
            rules_dict[rule[0]].append(rule[1])
        else:
            rules_dict[rule[0]] = [rule[1]]
    return rules_dict

RULES = get_rules(data)

def pages_to_print(text):
    pages_strings = re.findall(r"(?m)^(?!.*\|)\d+(?:,\d+)*$",text)
    pages = [page.split(',') for page in pages_strings]
     
    return pages

def get_median(pages):
    median = len(pages) // 2
  
    return pages[median]


def good_print_check(rules_dict, print_list):
    for x in range(1,len(print_list)):
        for y in range(0, x):
                if print_list[y] in rules_dict.get(print_list[x],[]):
                    return False

    return True

def check_prints_1(text):
    rules = get_rules(text)
    pages = pages_to_print(text)
    total = 0
    
    for item in pages:
        if good_print_check(rules,item):
            total += int(get_median(item))
    return total

#Part 2 section
def compare_pages(page_x, page_y):
    page_x_rules = RULES.get(page_x,[])
    page_y_rules = RULES.get(page_y, [])
    if page_y in page_x_rules:
    #page_x must come before page_y, they must be swapped
        return -1
    if page_x in page_y_rules:
    #page_x is in the rules of the page after it, so they must swap 
        return +1
    else:
        return 0
    
def fix_bad_print(print_list):
    return sorted(print_list, key=functools.cmp_to_key(compare_pages))


def check_prints_2(text):
    RULES = get_rules(text)
    pages = pages_to_print(text)
    total = 0
    
    for item in pages:
        if good_print_check(RULES,item)==False:
            new_item = fix_bad_print(item)
            total += int(get_median(new_item))
    return total



test = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

61,13,29
97,13,75,29,47
75,97,47,61,53
75,47,61,53,29
97,61,53,29,13
75,29,13
"""
RULES_TEST = get_rules(test)

# print(check_prints_1(data))
print(check_prints_2(data))


