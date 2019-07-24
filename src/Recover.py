import argparse


def recovery_file(recovery_filename, back_to_toc='Back to'):
    head_lines = 2
    # head_lines = 3 since add 2 blank lines when generated TOC
    output_file = []
    last_line = ''
    with open(recovery_filename, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith(('<a class="toc"', f'[{back_to_toc}')):
                # Because I add 1 blank line above when generated [Back to TOC]
                if not last_line.startswith(f'[{back_to_toc}') or line.strip():
                    output_file.append(line)
            elif line.startswith('<a class="toc"'):
                head_lines += 1
            last_line = line
    toc_pos = output_file.index('# Table of Contents\n')
    with open(recovery_filename, 'w', encoding='utf-8') as f:
        if toc_pos:
            f.writelines(output_file[:toc_pos])
        f.writelines(output_file[toc_pos+head_lines+1:])


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
