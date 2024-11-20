class Solution:
    def generate_vietnam_country_flag(self, n):
        """
        :param n: int (odd)
        :return: list[list]
        """
        complete_list = []
        for i in range(n):
            one_row = ["~"] * n
            complete_list.append(one_row)

        mid = n // 2
        complete_list[mid][mid] = "*"
        return complete_list


solution = Solution()
answer = solution.generate_vietnam_country_flag(7)

for i in range(len(answer)):
    print(*answer[i])



