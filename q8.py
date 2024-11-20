def validate(a, b, c):
    is_a_close_b = abs(a - b) <= 2
    is_a_close_c = abs(a - c) <= 2
    is_b_close_c = abs(b - c) <= 2

    is_c_far = abs(c - a) >= 3 and abs(c - b) >= 3
    is_b_far = abs(b - a) >= 3 and abs(b - c) >= 3
    is_a_far = abs(a - b) >= 3 and abs(a - c) >= 3

    return (is_a_close_b and is_c_far) or (is_a_close_c and is_b_far) or (is_b_close_c and is_a_far)


num = [int(input()) for _ in range(3)]
print(validate(*num))



