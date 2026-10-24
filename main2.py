text = input()

letters_count = 0
digits_count = 0

for char in text:
    if char.isalpha():      
        letters_count += 1
    elif char.isdigit():    
        digits_count += 1

print("Letters", letters_count)
print("Digits", digits_count)