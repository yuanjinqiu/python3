import difflib
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as f1, open(file2, "r") as f2:
    diff = difflib.unified_diff(f1.readlines(), f2.readlines())

    for line in diff:
        print(line)
