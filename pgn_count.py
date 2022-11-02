# -*- coding: utf-8 -*-

"""

"""


def count_result_space(line):
    results = ['1-0', '0-1', '1/2-1/2']
    if not line.startswith('[') and line.strip() != '':
        for result in results:
            if result in line:
                index = line.find(result)
                space_count = 0
                i = 1
                while line[index - i] == ' ':
                    space_count += 1
                    i += 1
                # if space_count==0:
                #     print(line)
                return space_count


def pgn_result_space(filename):
    spaces = []
    f = open(filename, 'r', encoding='windows-1252')
    lines = f.readlines()
    f.close()
    for line in lines:
        if count_result_space(line) is not None:
            spaces.append(count_result_space(line))
    return spaces


def count_list(a_list):
    count_d = {}
    for item in a_list:
        if item not in count_d:
            count_d[item] = 1
        else:
            count_d[item] += 1
    return count_d


f_input = open('pgn_file_path.txt', 'r')
count_two_space_pgn = 0
file_number_two_space = 0
file_number_other = 0
print('Other format file and their space count:')
try:
    while True:
        filepath = f_input.readline().strip()
        spaces = pgn_result_space(filepath)
        count = count_list(spaces)
        if len(count.keys()) == 1 and list(count.keys())[0] == 2:
            count_two_space_pgn += 1
        else:
            print(filepath, count_list(spaces))
            file_number_other += 1
        file_number_two_space += 1
except:
    pass
finally:
    f_input.close()
    print("not TWO space pgn file number:", file_number_other)
    print("only TWO space pgn file number:", count_two_space_pgn)
    print("total number of pgn file:", file_number_two_space)


