import re

l = '0123+456*0+78'
pattern = r'(?:0|[1-9][0-9]*)(?:[*+](?:0|[1-9][0-9]*))*'


if match := re.fullmatch(pattern, l) is None:
    print("z")
else:
    print("y")