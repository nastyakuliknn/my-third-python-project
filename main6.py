text = input()

frequencies = [0] * 26

for char in text:
    if char.isalpha():
        upper_char = char.upper()
        index = ord(upper_char) - ord('A')
        if 0 <= index < 26:
            frequencies[index] += 1

max_count = max(frequencies)

result_letters = ""
for i in range(26):
    if frequencies[i] == max_count and max_count > 0:

        result_letters += chr(i + ord('A'))

print(result_letters)
print(max_count)

