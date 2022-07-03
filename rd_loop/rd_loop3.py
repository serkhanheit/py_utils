import sys
import re

# regex_pattern = "(" + sys.argv[1] + ")"
regex_pattern = sys.argv[1]

pattern = re.compile(regex_pattern)

for line in sys.stdin:
    m = pattern.search(line)
    if m:
        # sys.stdout.write(m.group(1) + "\n")
        sys.stdout.write(str(m.groups()))
