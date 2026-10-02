#sequence of lines to lowercase
lines = []
while True:
    l=input()
    if l:
        lines.append(l.upper())
def to_lowercase(lines):
    lowercase_lines = []
    for line in lines:
        lowercase_lines.append(line.lower())
    return lowercase_lines