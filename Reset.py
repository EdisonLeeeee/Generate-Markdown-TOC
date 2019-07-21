def reset_file(input_filename):
    head_lines = 2
    triple_quote = 0
    output_file = []
    with open(input_filename, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith(('[Back to Top]', '<a class="toc"')):
                output_file.append(line)
            if line.startswith('#'):
                space_pos = line.find(' ')
                if 1 <= space_pos <= 6 and not triple_quote:
                    head_lines += 1
            elif line.startswith('```'):
                triple_quote = 1 - triple_quote
    with open(input_filename, 'w', encoding='utf-8') as f:
        for line in output_file[head_lines:]:
            f.write(line)


if __name__ == '__main__':
    output_filename = 'output.md'
    print(f'### Recovery from file: {output_filename}...')
    reset_file(output_filename)
    print('### Recovery done')
