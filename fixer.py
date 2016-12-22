import sys

with open(sys.argv[1], "r") as infile:
    with open(sys.argv[2], "w") as outfile:
        for line in infile:
            correct_line = line[14:]
            outfile.write(correct_line)
