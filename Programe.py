
def left_shift(binary, positions):
    num = int(binary, 2)

    print("Original Number:", binary)
    print("Left Shift Process:")

    for i in range(positions):
        num = (num << 1) & 0xFF
        print("Step", i + 1, ":", format(num, '08b'))

    print("Final Result:", format(num, '08b'))


def right_shift(binary, positions):
    num = int(binary, 2)

    print("Original Number:", binary)
    print("Right Shift Process:")

    for i in range(positions):
        num = num >> 1
        print("Step", i + 1, ":", format(num, '08b'))

    print("Final Result:", format(num, '08b'))


print("a) Logical Left Shift")
left_shift("10110110", 3)

print("\nb) Logical Right Shift")
right_shift("11010100", 3)
