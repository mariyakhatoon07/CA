
def to_binary(n):
    return format(n & 0xFF, '08b')

def to_decimal(binary):
    n = int(binary, 2)
    if n >= 128:
        return n - 256
    return n

def addition(a, b):
    binary_a = to_binary(a)
    binary_b = to_binary(b)

    result = (a + b) & 0xFF
    binary_result = to_binary(result)

    print("First Number:", binary_a)
    print("Second Number:", binary_b)
    print("Binary Addition:", binary_result)
    print("Decimal Result:", to_decimal(binary_result))

    if a + b > 127 or a + b < -128:
        print("Arithmetic Overflow: Yes")
    else:
        print("Arithmetic Overflow: No")

print("a) (120 + 62)")
addition(120, 62)

print("\nb) (-120 + -62)")
addition(-120, -62)
