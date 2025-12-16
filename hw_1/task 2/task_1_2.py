import sys

def tail_lines(lines, n):
    lines = list(lines)
    return lines[-n:]

def main():
    files = sys.argv[1:]
    if not files:
        for line in tail_lines(sys.stdin, 17):
            print(line, end='')
    else:
        for i, filename in enumerate(files):
            if len(files) > 1:
                if i > 0:
                    print()
                print(f"==> {filename} <==")
            try:
                with open(filename, encoding='utf-8') as f:
                    for line in tail_lines(f, 10):
                        print(line, end='')
            except:
                print(f"tail: No such file '{filename}'")

if __name__ == "__main__":
    main()