import datetime
import os
import sys

import black

if len(sys.argv) > 1:
    day = int(sys.argv[-1])
else:
    day = datetime.date.today().day

with open(f"samples/{day}.txt", "w") as f:
    f.write("")

base_file_content = f"""
import utils
import rich

sample = utils.get_aoc_input({day})

def part_1():
    pass

    
def part_2():
    pass


if __name__ == "__main__":
    utils.perf(part_1)
    utils.perf(part_2)    
"""

base_file_content = black.format_str(base_file_content, mode=black.Mode())

with open(f"{day}.py", "w") as f:
    f.write(base_file_content)
