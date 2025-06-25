def rightmost_set_bit_position(n):
    if n == 0:
        return 0  # No set bit
    position = 1
    while (n & 1) == 0:
        n = n >> 1
        position += 1
    return position

# Get input from user
num = int(input("Enter number: "))

# Print binary form without "0b"
binary = bin(num)[2:]  # Remove the '0b' prefix
print("Binary form of the number:", binary)

# Find position of rightmost set bit
pos = rightmost_set_bit_position(num)

# Show result
print("Position of the first bit set:", pos)
