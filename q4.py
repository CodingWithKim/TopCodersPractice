class Solution:
    def max_leftover(self, num):
        """
        :param num: int
        :return: int
        """
        max_leftover = 0
        optimal_pack_size = 1

        for i in range(1, num+1):
            leftover = num % i
            if leftover >= max_leftover:
                max_leftover = leftover
                optimal_pack_size = i

        return optimal_pack_size


# Test case
solution = Solution()

num1 = int(input("Enter number:"))
print(solution.max_leftover(num1))
