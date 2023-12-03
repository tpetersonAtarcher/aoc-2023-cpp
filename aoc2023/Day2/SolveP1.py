class num_color:

    def __init__(self, num, color):
        self.num = num
        self.color = color


games = []


def solve_puzzle_line(line, marks):
    game_idx, hfulls = line.replace("Game", "").strip().split(":", 1)
    hfulls = hfulls.split(";")
    game_idx = int(game_idx)
    games.append([True, game_idx, []])

    for i, hfull in enumerate(hfulls):
        games[-1][-1].append([])
        block_counts = hfull.split(",")
        for block_count in block_counts:
            num, color = block_count.strip().split(" ")
            num_col = num_color(int(num), color.strip())

            for i, mark in enumerate(marks):
                if num_col.color == mark.color:
                    if num_col.num > mark.num:
                        games[-1][0] = False
                        print(
                            f"{num_col.color} {num_col.num} > {mark.color} {mark.num} = Game {game_idx} is not possible")
            games[-1][-1][-1].append(num_col)


def solve_puzzle_two(line):
    game_idx, hfulls = line.replace("Game", "").strip().split(":", 1)
    hfulls = hfulls.split(";")
    game_idx = int(game_idx)
    games.append([game_idx, [num_color(0, "green"),
                 num_color(0, "blue"), num_color(0, "red")], 1, []])

    for i, hfull in enumerate(hfulls):
        games[-1][-1].append([])
        block_counts = hfull.split(",")
        for block_count in block_counts:
            num, color = block_count.strip().split(" ")
            num_col = num_color(int(num), color.strip())

            for i, mark in enumerate(games[-1][1]):
                if num_col.color == mark.color:
                    if num_col.num > mark.num:
                        games[-1][1][i].num = num_col.num
            games[-1][-1][-1].append(num_col)

    k = f"Game {game_idx}: "
    for i, max in enumerate(games[-1][1]):
        if i == 0:
            k += f"max {max.color} {max.num}".strip()
        else:
            k += f", max {max.color} {max.num}".strip()
        games[-1][2] = games[-1][2]*max.num
    k += f", prime = {games[-1][2]}"
    print(k)


if __name__ == "__main__":
    file = "C:\\Users\\tpeterson\\Documents\\AdventOfCode\\aoc-2023-cpp\\aoc2023\\Day2\\input.txt"
    sum = 0
    marks = []
    marks.append(num_color(12, "red"))
    marks.append(num_color(13, "green"))
    marks.append(num_color(14, "blue"))

    # with open("out.txt", 'wt') as out_file:
    #     with open(file, "rt") as in_file:
    #         for line in in_file:
    #             solve_puzzle_line(line, marks)
    # sum = 0
    # for game in games:
    #     if game[0] is True:
    #         sum += game[1]
    #     else:
    #         print(f"Game {game[1]} not possible")
    # print(sum)
    with open("out.txt", 'wt') as out_file:
        with open(file, "rt") as in_file:
            for line in in_file:
                solve_puzzle_two(line)
    sumpow = 0
    for game in games:
        sumpow += game[2]

    print(sumpow)
