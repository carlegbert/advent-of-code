import importlib
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        result = "ERROR: Specify day & part 1 or 2 (e.g. python aoc24/main.py 8 2)."

    day = sys.argv[1]
    if len(day) == 1:
        day = f"0{day}"

    solution_mod = importlib.import_module(f"solutions.p{day}")
    filename = f"aoc24/inputs/day_{day}.txt"

    if sys.argv[2] == "1":
        result = solution_mod.solve_p1(filename)
    elif sys.argv[2] == "2":
        result = solution_mod.solve_p2(filename)
    else:
        result = "ERROR: Specify part 1 or 2."

    print(result)
