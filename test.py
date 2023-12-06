original_string = "Hello"
width = 10

left_padded = original_string.ljust(width, '-')
right_padded = original_string.rjust(width, '*')
center_padded = original_string.center(width, '=')

print(left_padded)
print(right_padded)
print(center_padded)