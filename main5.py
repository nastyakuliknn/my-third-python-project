import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    total_sum = 0
    current_number_str = ""
    current_sign = 1  

    expression = line + "+"

    for char in expression:
        if char.isdigit():
        
            current_number_str += char
        elif char == '+' or char == '-':
        
            if current_number_str:
                total_sum += current_sign * int(current_number_str)
                current_number_str = "" 
            if char == '+':
                current_sign = 1
            else:
                current_sign = -1
    print(total_sum)

