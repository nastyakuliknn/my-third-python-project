expression = input()

numbers = expression.split('*')

result = int(numbers[0])

for i in range(1, len(numbers)):
    result *= int(numbers[i])

print(result)