import random
import sys
import time

from sort import registry

if len(sys.argv) == 1:
    n_elements = 1000
elif len(sys.argv) == 3:
    match sys.argv[1]:
        case "-n":
            n_elements = int(sys.argv[2])
        case _:
            print("[ERR] Invalid options", " ".join(sys.argv[1:]))
            exit(0)
else:
    print("[ERR] Invalid options", " ".join(sys.argv[1:]))
    exit(0)

print("[LOG] n_elements:", n_elements)
