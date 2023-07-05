import re

def PatternCount(Text, Pattern):
    p = re.compile(rf"(?=({Pattern}))")
    return len(p.findall(Text))


a = ["1","2","3"]

print(a[0:1])
