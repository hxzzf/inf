import re
s = open('24.txt').readline().strip()
pattern = r'(?:0|[1-9][0-9]*)(?:[*+](?:0|[1-9][0-9]*))*'

# Find the longest expression that equals zero
longest_zero_expr = ""
max_length = 0

for expr in arr:
    try:
        result = eval(expr)
        if result == 0 and len(expr) > max_length:
            max_length = len(expr)
            longest_zero_expr = expr
    except:
        continue

print(f"Longest expression that equals zero: '{longest_zero_expr}'")
print(f"Length: {max_length}")
