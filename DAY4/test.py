import re

text = "XMASAMX"

pattern = re.compile(r"(?=(XMAS|SAMX))")
print(pattern.findall(text)) 