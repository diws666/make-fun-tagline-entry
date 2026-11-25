import os

ENTRY_LINE = "Build an agent. Enter a bounty. Win the reward."
OUTPUT_FILENAME = "entry.txt"


def write_entry(output_dir, line, filename=OUTPUT_FILENAME):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir, ENTRY_LINE)


if __name__ == "__main__":
    main()
