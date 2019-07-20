import fileinput
from collections import defaultdict

filename = "test.md"
toc = []
n = 0
file = []
with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith("#"):
            space_pos = line.find(' ')
            if space_pos == 1:
                title_dict = defaultdict(int)
                n += 1
                index = str(n)
                title_dict[1] = n
            else:
                title_dict[space_pos] += 1
                index = str(n)
                for i in range(2, space_pos+1):
                    index += '-' + str(title_dict[i])

            tab = (space_pos-1) * '\t'
            title = line[space_pos+1:-1] if line[-1] == '\n' else line[space_pos+1:]
            toc.append(f'{tab}+ [{title}](#{index})\n')
            line = f'\n<h{space_pos} id ="{index}">{title}</h{space_pos}>\n\n'
        file.append(line)

filename = 't.md'
with open(filename, 'w', encoding='utf-8') as f:
    for line in toc:
        f.write(line)
    for line in file:
        f.write(line)

# for line in fileinput.input(filename):
#     if line.startswith("#"):
#         space_pos = line.find(' ')
#         print(space_pos)
