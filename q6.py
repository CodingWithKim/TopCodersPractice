class Solution:
    def judge(self, b_string):
        """
        :param b_string: str
        :return: str
        """
        input_list = list(b_string)
        count_dict = {}
        for i in input_list:
            if i in count_dict.keys():
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        return "Win" if count_dict["1"] > count_dict["0"] else "Lose"


solution = Solution()
print(solution.judge("0101111111111"))
print(solution.judge("11100000000000"))