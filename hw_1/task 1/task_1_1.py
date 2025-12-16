import sys

def numerate_lines(lines):
    for i, line in enumerate(lines, 1):
        print(f"{i}\t{line}", end='')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                numerate_lines(f)
        except:
            print(f"No such file '{filename}'")
    else:
        numerate_lines(sys.stdin)

if __name__ == "__main__":
    main()
