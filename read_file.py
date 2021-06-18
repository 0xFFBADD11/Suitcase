import sys

#  Read filename argv[1]
try:
    with open(sys.argv[1], 'r') as f:
        for line in f:
            sys.stdout.write(line)      # Actions, not words, here.
        f.close
except FileNotFoundError as e:
    print(e)
finally:
    pass                                #  Cleanup