import argparse


def recovery_file(recovery_filename):
    head_lines = 2
    triple_quote = 0
    output_file = []
    with open(recovery_filename, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith(('[Back to Top]', '<a class="toc"')):
                output_file.append(line)
            if line.startswith('#'):
                pos = 0
                # pos is the position of first letter that isn't '#' in line
                while pos < len(line) and line[pos] == '#':
                    pos += 1
                if 1 <= pos <= 6 and not triple_quote:
                    head_lines += 1
            elif line.startswith('```'):
                triple_quote = 1 - triple_quote
    with open(recovery_filename, 'w', encoding='utf-8') as f:
        for line in output_file[head_lines:]:
            f.write(line)


def parse_args():
    parser = argparse.ArgumentParser(description='Recover your Markdown file than has generated TOC by Generate_TOC.py.')
    parser.add_argument('recovery_filename', metavar='recovery_filename', type=str,
                        help='The file that need to recover.')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    recovery_filename = args.recovery_filename
    confirm = input(f'### Recover from file: {recovery_filename} [Yes/No]\n')
    if confirm.strip().lower() == 'yes':
        recovery_file(recovery_filename)
        print('### Recovery done')
    else:
        print('### Terminate the recovery.\nThe program has finished.')
