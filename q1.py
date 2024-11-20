class Solution:
    def generate_series(self, n):
        """
        :param n: int
        :return: list[int]
        """
        base_num = 21
        base_multiplier = 4
        result_list = [base_num]
        if n == 1:
            return result_list
        else:
            for i in range(1, n):
                base_num = base_num + base_multiplier
                base_multiplier *= 2
                result_list.append(base_num)
            return result_list


solution = Solution()
print(*solution.generate_series(1))
print(*solution.generate_series(3))
print(*solution.generate_series(6))
print(solution.generate_series(8))

