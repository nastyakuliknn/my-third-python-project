import sys

for line in sys.stdin:
    line = line.strip() 
    if not line:
        continue
        
    max_zeros = 0      
    current_zeros = 0  
    
    for char in line:
        if char == '0':
            current_zeros += 1
            if current_zeros > max_zeros:
                max_zeros = current_zeros
        else:
            current_zeros = 0

    print(max_zeros)

