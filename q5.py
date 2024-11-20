N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

valid_count = 0
current_time = 0

for i in range(len(A)):
    if current_time + B[i] <= A[i]:
        valid_count += 1
        current_time += B[i]

print(valid_count)