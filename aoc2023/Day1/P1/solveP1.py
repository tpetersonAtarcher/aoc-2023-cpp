DEBUG = True


word_to_num = {"one": '1', "two": '2', "three": '3', "four": '4',
               "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}


def debug_print(debug_str, file=None):
    if DEBUG is True:
        if file is not None:
            file.write(debug_str)
        else:
            print(debug_str)


def solve_puzzle_line(input_line):
    value = ["0", "0"]
    i = 0
    word = ""
    for c in input_line:
        if str.isnumeric(c) is True:
            word = ""
            if (i == 0):
                value[0] = c
                value[1] = c
                i += 1
            else:
                value[1] = c
        else:
            word = word + c
            idx = []
            for k in word_to_num.keys():
                val = word.rfind(k)
                if val > -1:
                    index = 0
                    for list_idx in idx:
                        if val > list_idx[0]:
                            break
                        else:
                            index += 1
                    idx.insert(index, (val, k))
            if len(idx) > 0:
                debug_print(idx)
                t_val = word_to_num[idx[0][1]]
                if (i == 0):
                    value[0] = str(t_val)
                    value[1] = str(t_val)
                    i += 1
                else:
                    value[1] = str(t_val)

    val = str(value[0]) + str(value[1])
    debug_print(val)
    return int(val)


if __name__ == "__main__":
    file = "C:\\Users\\tpeterson\\Documents\\AdventOfCode\\aoc-2023-cpp\\aoc2023\\Day1\\P1\\input.txt"
    sum = 0
    with open("out.txt", 'wt') as out_file:
        with open(file, "rt") as in_file:
            for line in in_file:
                sum += solve_puzzle_line(line)
                debug_print(line.strip("\n")+" " +
                            str(solve_puzzle_line(line))+"\n", out_file)
        debug_print(str(sum), out_file)
    print(sum)
