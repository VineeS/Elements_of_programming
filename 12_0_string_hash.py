
import functools

def string_hash(s, modulus):
    MULT = 997
    return functools.reduce(lambda v, c: (v * MULT + ord(c)) % modulus, s, 0)

input_string = "Hello, World!"
modulus = 1000000  # Choose an appropriate modulus

hash_code = string_hash(input_string, modulus)

print("Input string:", input_string)
print("Modulus:", modulus)
print("MULT constant:", 997)
print()

# Initialize v to 0
v = 0

# Process each character in the input string
for c in input_string:
    print(f"Character: {c}")
    print(f"Current v: {v}")
    v = (v * 997 + ord(c)) % 1000000
    print(f"Updated v: {v}")
    print("-" * 20)

print(f"Final hash code for '{input_string}': {hash_code}")
