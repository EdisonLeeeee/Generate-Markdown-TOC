import argparse
from collections import defaultdict


def parse_input_file(input_filename, back_to_toc='Back to TOC'):
    table_of_contents = ['<a class="toc" id="table-of-contents"></a>\n# Table of Contents\n']
    primary_title_count = 0
    output_file = []
    # to judge whether within the triple_quotes ``` ```
    triple_quote = False
    with open(input_filename, 'r', encoding='utf-8') as f:
        for line in f:
            # if [toc] command exits, ignore it
            if line == '[toc]\n':
                continue
            if line.startswith('#'):
                # pos is the position of first letter that isn't '#' in line
                pos = line[:7].rfind('#') + 1
                if triple_quote or pos > 6:
                    # for some statements that startwith '#' but not head line
                    # or '#' more than six
                    output_file.append(line)
                    continue
                if pos == 1:
                    # primary_title
                    title_dict = defaultdict(int)
                    primary_title_count += 1
                    index = str(primary_title_count)
                    title_dict[1] = primary_title_count
                else:
                    # dict of secondary title, level 3 title and so on
                    title_dict[pos] += 1
                    index = str(primary_title_count)
                    for i in range(2, pos+1):
                        index += '-' + str(title_dict[i])

                tab = (pos-1) * '\t'
                title_pos = pos + 1 if line[pos] == ' ' else pos
                title = line[title_pos:-1] if line[-1] == '\n' else line[title_pos:]
                table_of_contents.append(f'{tab}+ [{title}](#{index})\n')
                # add anchor above the header line
                line_above = f'<a class="toc" id ="{index}"></a>\n'
                output_file.append(line_above)
                output_file.append(line)
                if pos == 1:
                    output_file.append(f'[{back_to_toc}](#table-of-contents)\n\n')
            else:
                output_file.append(line)
                if line.startswith('```'):
                    triple_quote = 1 - triple_quote
    return table_of_contents, output_file


def write_back(output_filename, table_of_contents, output_file, placeholder):
    # for pretty, add two lines
    table_of_contents.append('\n' * 2)
    placeholder += '\n'
    toc_pos = output_file.index(placeholder) if placeholder in output_file else 0
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.writelines(output_file[:toc_pos])
        f.writelines(table_of_contents)
        f.writelines(output_file[toc_pos+1:])


def parse_args():
    parser = argparse.ArgumentParser(description='Generate TOC for your Markdown file.')
    parser.add_argument('input_filename', metavar='input_filename', type=str,
                        help='The file that need to generate TOC. You must spacify the input filename.')
    parser.add_argument('output_filename', metavar='output_filename', type=str, nargs='?',
                        help='The newly generated file with TOC from the original file.\
                        If the parameter is omitted, The original file will be overwritten with the newly generated file. NOTE: output_filename=input_filename in default.')
    parser.add_argument('placeholder', metavar='placeholder', type=str, nargs='?',
                        default='~~placeholder~~', help='Specify the placeholder, and it will generate TOC at the position of placeholder, otherwise the TOC will generate at the top. NOTE: placeholder="~~placeholder~~" in default.')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    input_filename = args.input_filename
    output_filename = args.output_filename
    placeholder = args.placeholder
    if not output_filename:
        confirm = input('You did not enter output_filename. Would you like to replace your original file with newly generated file? [Yes/No]\n')
        if confirm.strip().lower() != 'yes':
            print("### Generated TOC termination.\nThe program has finished.")
            exit()
        else:
            output_filename = input_filename
    print(f'### Generating markdown toc from {input_filename}, and wtite back to {output_filename}...')

    table_of_contents, output_file = parse_input_file(input_filename)
    write_back(output_filename, table_of_contents, output_file, placeholder)
    print('### Already generating markdown toc')
