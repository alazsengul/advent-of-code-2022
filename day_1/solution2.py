import heapq


class Solution2:
    def __init__(self, filename):
        self.calories = self._construct_calories(filename)

    def _construct_calories(self, filename):
        result = []
        candidate = 0

        with open(filename, "r") as f:

            for line in f:
                line = line.strip()

                if line:
                    candidate += int(line)
                else:
                    result.append(candidate)
                    candidate = 0

        heapq.heapify(result)
        return result

    def get_largest_n_calories(self, n):
        return sum(heapq.nlargest(n, self.calories))


solution = Solution2(filename="./input.txt")
print(solution.get_largest_n_calories(n=3))
