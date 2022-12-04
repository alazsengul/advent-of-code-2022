def solution1(filename):
    result, candidate = 0, 0

    with open(filename, "r") as f:

        for line in f:
            line = line.strip()

            if line:
                candidate += int(line)
            else:
                result = max(result, candidate)
                candidate = 0

    return result


print(solution1("./input.txt"))
