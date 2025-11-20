import re
with open(r"/Users/taylorhood/Documents/Projects/AdventOfCode2024/day5/data.txt") as file:
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

def pages_to_print(text):
    pages_strings = re.findall(r"(?m)^(?!.*\|)\d+(?:,\d+)*$",text)
    pages = [page.split(',') for page in pages_strings]
     
    return pages

def get_median(pages):
    median = int((len(pages)/2) - .5)
  
    return pages[median]

def get_int_print_list(print_list):
    ints=[int(item) for item in print_list]
    return ints

def good_print_check(rules_dict, print_list):
    for x in range(1,len(print_list)):
        for y in range(0, x):
            try:
                if print_list[y] in rules_dict[print_list[x]]:
                    return False
            except KeyError as e:
                continue
    return True



def fix_bad_print(rules_dict, print_list):
    """takes the bad print list, and isolates all the values that were causing it fail, and reorders them
    """
    new_print_list = []
    issue_store = []
    new_print_list.append(print_list[0])

    """finds all the bad values and their indexes, and separates them from the 'good' list"""
    for x in range(1,len(print_list)):
        for y in range(0, x):
            if print_list[y] in rules_dict.get(print_list[x],[]):
                if [x,print_list[x]] not in issue_store:
                    issue_store.append([x,print_list[x]])
                    
        if print_list[y] not in rules_dict.get(print_list[x],[]):
            new_print_list.append(print_list[x])

    """reinsters the bad values to the first index before they broke"""
    for item in issue_store:
        if item[1] in new_print_list:
            new_print_list.remove(item[1])
        new_print_list.insert(int(item[0]-1), item[1])
        
    """re-runs the list, and repeats the cycle until there are no more fails"""
    if good_print_check(rules_dict, new_print_list)==True:
        return new_print_list
    else:
        return fix_bad_print(rules_dict,new_print_list)

# 61,13,29 becomes 61,29,13
# 97,13,75,29,47 becomes 97,75,47,29,13.


def check_prints_1(text):
    rules = get_rules(text)
    pages = pages_to_print(text)
    total = 0
    
    for item in pages:
        if good_print_check(rules,item):
            total += int(get_median(item))
    return total

def check_prints_2(text):
    rules = get_rules(text)
    pages = pages_to_print(text)
    total = 0
    
    for item in pages:
        if good_print_check(rules,item)==False:
            new_item = fix_bad_print(rules,item)
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

# print(check_prints_1(data))
print(check_prints_2(data))


