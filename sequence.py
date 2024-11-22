def get_sequence():
    sequence_length = int(input())
    input_sequence = input().split()
    if len(input_sequence) > sequence_length:
        print(f"Error: Too many input values. Expected {sequence_length}, got {len(input_sequence)}")
    else:
        returned_sequence = [i for i in input_sequence]
        return returned_sequence


default_sequence = get_sequence()
favourite_sequence = get_sequence()

if "".join(favourite_sequence) in "".join(default_sequence):
    print("Yes")
else:
    print("No")

