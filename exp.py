import random
import sys
import time

from sort import registry

INTMAX = 2147483647
INTMIN = -2147483648


class Console:
    def __init__(self, debug: bool = False) -> None:
        self.debug = debug

    def log(self, *msg):
        if self.debug:
            print("[LOG]", *msg)

    def err(self, *msg):
        print("[ERR]", *msg)

    def out(self, *msg):
        print(*msg)


console = Console(debug=False)
n_elements = 1000

if len(sys.argv) > 1:
    i = 1
    try:
        while i < len(sys.argv):
            match sys.argv[i]:
                case "-n":
                    n_elements = int(sys.argv[i + 1])
                    i += 1
                case "-debug":
                    console.debug = True
                case _:
                    console.err("Invalid options")
                    exit(0)
            i += 1
    except IndexError:
        console.err("missing a integer value for option -n")
        exit(0)

nums = [random.randint(INTMIN, INTMAX) for _ in range(n_elements)]
console.log(f"created {n_elements} random numbers")

timeit = {}

console.log("start test")
for name, func in registry.items():
    t1 = time.time_ns()
    func(nums)
    t2 = time.time_ns()

    timeit[name] = (t2 - t1) / 1e6  # ms
console.log("completed test")

console.out("n_elements:", n_elements)
console.out("[RESULT]")

results = sorted(list(timeit.items()), key=lambda x: x[1])

for i, (name, time_in_ms) in enumerate(results):
    if time_in_ms < 1000:
        console.out(f"[{i}] {name} with {time_in_ms:.3f} ms")
    else:
        time_in_s = time_in_ms / 1000
        console.out(f"[{i}] {name} with {time_in_s:.3f} s")
