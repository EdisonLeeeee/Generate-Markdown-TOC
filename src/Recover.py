import argparse


def recovery_file(recovery_filename):
    head_lines = 2  # head_lines = 3 since add 2 blank lines when generated TOC
    output_file = []
    back_to_top = False
    with open(recovery_filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('<a class="toc"'):
                head_lines += 1
            elif line.startswith('[Back to Top]'):
                back_to_top = True
            else:
                # Because I add 1 blank line above when generated [Back to Top]
                if not back_to_top:
                    output_file.append(line)
                else:
                    back_to_top = False

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
