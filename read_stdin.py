import sys

#  Read filename argv[1], or stdin if no args or argv[1] is "-"
with open(sys.argv[1], 'r') if (len(sys.argv) > 1 and sys.argv[1] != "-") else sys.stdin as f:
    for line in f:
        sys.stdout.write(line)    # Actions, not words, here.
    f.close