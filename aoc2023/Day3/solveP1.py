IS_PRD = 0
IS_NUM = 1
IS_SYM = 2
IS_STR = 3

types = {IS_PRD: "IS_PRD", IS_NUM: "IS_NUM",
         IS_SYM: "IS_SYM", IS_STR: "IS_STR"}


class num_char:
    def __init__(self, char, num):

        self.char = char
        self.sub_char = char
        self.num = num
        self.sum = 0
        self.gear = 0
        self.group = []

    def __str__(self):
        return f"char={types[self.char]}, sub_char={types[self.sub_char]}, num={self.num}, sum={self.sum}, gear={self.gear}, group={self.group}"


DEBUG = True


def debug_print(debug_str, file=None):
    if DEBUG is True:
        if file is not None:
            file.write(debug_str)
        else:
            print(debug_str)


if __name__ == "__main__":
    file = "C:\\Users\\tpeterson\\Documents\\AdventOfCode\\aoc-2023-cpp\\aoc2023\\Day3\\input.txt"

    arrays = []
    with open("out.txt", 'wt') as out_file:
        with open(file, "rt") as in_file:
            for line in in_file:
                arrays.append(list(line.strip()))
                # debug_print(list(line))
    height = len(arrays)
    for i in range(0, height, 1):
        num_start = -1
        num_end = -1
        width = len(arrays[i])
        for j in range(0, width, 1):
            combine = False
            if arrays[i][j].isnumeric():
                if num_start >= 0:
                    num_end = j
                else:
                    num_start = j
                    num_end = j
                if j == (width-1):
                    combine = True

            else:
                if num_end >= 0:
                    combine = True
                if arrays[i][j] == '.':
                    arrays[i][j] = num_char(IS_PRD, 0)
                elif arrays[i][j] == '*':
                    arrays[i][j] = num_char(IS_SYM, 0)
                    arrays[i][j].sub_char = IS_STR
                else:
                    arrays[i][j] = num_char(IS_SYM, 0)

            if combine is True:
                k = ""
                for ii in range(num_start, num_end+1, 1):
                    k += arrays[i][ii]
                val = int(k)
                for ii in range(num_start, num_end+1, 1):
                    arrays[i][ii] = num_char(IS_NUM, val)
                num_start = -1
                num_end = -1

    sum = 0
    for i in range(0, height, 1):
        width = len(arrays[i])
        for j in range(0, width, 1):
            if arrays[i][j].char == IS_SYM:
                if j > 0:
                    if arrays[i][j-1].char == IS_NUM:
                        arrays[i][j].group.append(arrays[i][j-1].num)
                if j < (width-1):
                    if arrays[i][j+1].char == IS_NUM:
                        arrays[i][j].group.append(arrays[i][j+1].num)
                if i > 0:
                    if arrays[i-1][j].char == IS_NUM:
                        arrays[i][j].group.append(arrays[i-1][j].num)
                    elif j == 0:
                        if arrays[i-1][j+1].char == IS_NUM:
                            arrays[i][j].group.append(arrays[i-1][j+1].num)
                    elif j == (width-1):
                        if arrays[i-1][j-1].char == IS_NUM:
                            arrays[i][j].group.append(arrays[i-1][j-1].num)
                    else:
                        if arrays[i-1][j+1].char == IS_NUM:
                            arrays[i][j].group.append(arrays[i-1][j+1].num)
                        if arrays[i-1][j-1].char == IS_NUM:
                            arrays[i][j].group.append(arrays[i-1][j-1].num)

                if i < (height):
                    if arrays[i+1][j].char == IS_NUM:
                        arrays[i][j].group.append(arrays[i+1][j].num)
                    elif j == 0:
                        if arrays[i+1][j+1].char == IS_NUM:
                            arrays[i][j].group.append(arrays[i+1][j+1].num)
                    elif j == (width-1):
                        if arrays[i+1][j-1].char == IS_NUM:
                            arrays[i][j].group.append(arrays[i+1][j-1].num)
                    else:

                        if arrays[i+1][j+1].char == IS_NUM:
                            arrays[i][j].group.append(arrays[i+1][j+1].num)
                        if arrays[i+1][j-1].char == IS_NUM:
                            arrays[i][j].group.append(arrays[i+1][j-1].num)
    gear_sum = 0
    for row in arrays:
        for column in row:

            if column.char == IS_SYM:
                for val in column.group:
                    column.sum += val
                sum += column.sum
            if column.sub_char == IS_STR:
                if len(column.group) == 2:
                    column.gear = column.group[0]*column.group[1]
                gear_sum += column.gear
            if len(column.group) > 0:
                print(str(column))

    print(sum)
    print(gear_sum)
