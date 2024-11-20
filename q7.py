memo = {}

def summation(n, m):
    if (n,m) in memo:
        return memo[(n,m)]

    if m == 1:
        result = n * (n+1) // 2
    else:
        previous_sum = summation(n, m-1)
        result = summation(previous_sum, 1)

    memo[(n,m)] = result
    return result

n = int(input())
m = int(input())

print(summation(n,m))