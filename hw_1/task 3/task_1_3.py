import sys

def calc_stats(lines):
    lines_list = list(lines)
    line_cnt = len(lines_list)
    word_cnt = sum(len(line.split()) for line in lines_list)
    byte_cnt = sum(len(line.encode('utf-8')) for line in lines_list)
    return line_cnt, word_cnt, byte_cnt

def print_stats(res, name=None):
    if name:
        print(f'{res[0]:7} {res[1]:7} {res[2]:7} {name}')
    else:
        print(f'{res[0]:7} {res[1]:7} {res[2]:7}')

def main():
    files = sys.argv[1:]
    total_res = [0, 0, 0]
    if not files:
        res = calc_stats(sys.stdin)
        print_stats(res)
    else:
        results = []
        for fname in files:
            try:
                with open(fname, encoding='utf-8') as f:
                    cnts = calc_stats(f)
                    results.append((cnts, fname))
                    for i in range(3):
                        total_res[i] += cnts[i]
            except:
                print(f"wc: No such file {fname}", file=sys.stderr)
        for stats, fname in results:
            print_stats(stats, fname)
        if len(results) > 1:
            print_stats(total_res, 'total')

if __name__ == "__main__":
    main()
