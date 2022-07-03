import sys
import re

cli_arg_pattern = sys.argv[1]

re_pattern = re.compile(cli_arg_pattern)

for line in sys.stdin:
    if re_pattern.search(line):
        sys.stdout.write(line)
