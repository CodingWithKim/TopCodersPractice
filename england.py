def print_uk_flag(num):
    row = []
    mid = num // 2
    end = num - 1
    for i in range(num):
        current = []
        for j in range(num):
            if i == j or i == mid or j == mid or j == end:
                current.append(0)
            else:
                current.append(1)
        row.append(current)
        end -= 1
    return row


number = int(input())
result = print_uk_flag(number)
for m in range(number):
    print(*result[m])
