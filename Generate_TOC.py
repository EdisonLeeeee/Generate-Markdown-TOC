from collections import defaultdict


def parse_input_file(input_filename):
    table_of_contents = ['<a class="toc" id="table-of-contents"></a>\n# Table of Contents\n']
    primary_title_count = 0
    output_file = []
    triple_quote = 0
    with open(input_filename, 'r', encoding='utf-8') as f:
        for line in f:

            if line.startswith("#"):
                space_pos = line.find(' ')
                if space_pos == -1 or space_pos > 6 or triple_quote:
                    # for some statements that startwith '#' but not title
                    # or '#' more than six
                    output_file.append(line)
                    continue
                if space_pos == 1:
                    # primary_title
                    title_dict = defaultdict(int)
                    primary_title_count += 1
                    index = str(primary_title_count)
                    title_dict[1] = primary_title_count
                else:
                    # secondary title, level 3 title and so on
                    title_dict[space_pos] += 1
                    index = str(primary_title_count)
                    for i in range(2, space_pos+1):
                        index += '-' + str(title_dict[i])

                tab = (space_pos-1) * '\t'
                title = line[space_pos+1:-1] if line[-1] == '\n' else line[space_pos+1:]
                table_of_contents.append(f'{tab}+ [{title}](#{index})\n')
                # add anchor above the header line
                line_above = f'<a class="toc" id ="{index}"></a>\n'
                output_file.append(line_above)
                output_file.append(line)
                if space_pos == 1:
                    output_file.append('[Back to Top](#table-of-contents)\n')
            else:
                output_file.append(line)
                if line.startswith('```'):
                    triple_quote = 1 - triple_quote
    return table_of_contents, output_file


def write_back(output_filename, table_of_contents, output_file):
    with open(output_filename, 'w', encoding='utf-8') as f:
        for line in table_of_contents:
            f.write(line)
        # for pretty, add two lines
        f.write('\n\n')
        for line in output_file:
            f.write(line)


if __name__ == '__main__':
    input_filename = 'input.md'
    output_filename = 'output.md'
    print(f'### Generating markdown toc from{input_filename}, and wtite back to {output_filename}...')

    table_of_contents, output_file = parse_input_file(input_filename)
    write_back(output_filename, table_of_contents, output_file)
    print('### Already generating markdown toc')
