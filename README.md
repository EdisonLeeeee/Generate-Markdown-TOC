# Generate markdown TOC
Since GitHub cannot automatically generate TOC using the TOC command, Inspired by [Markdown toclify](https://github.com/rasbt/markdown-toclify), I write a script that could help you generate TOC in your file.
This 

# Requires
+ Python 3.x (Since I used f-strings)
+ argparse

# Usage
# Generate_TOC
```bash
$  python .\Generate_TOC.py -h
usage: Generate_TOC.py [-h] input_filename [output_filename]

Generate TOC for your Markdown file.

positional arguments:
  input_filename   The file that need to generate TOC.
  output_filename  The newly generated file with TOC from the original file.
                   If the parameter is omitted, The original file will be
                   overwritten with the newly generated file. i.e., default:
                   output_filename = input_filename.

optional arguments:
  -h, --help       show this help message and exit

```
You can specify the file name to generate the TOC, as well as the output file name
**Note**: If you do not specify `output_filename`, it overwrites the original file by default.


## Recovery
```bash
$  python .\Recover.py -h
usage: Recover.py [-h] recovery_filename

Recover your Markdown file than has generated TOC by Generate_TOC.py.

positional arguments:
  recovery_filename  The file that need to recover.

optional arguments:
  -h, --help         show this help message and exit
```
You can specify the file name you want to recover, and remove the TOC from it to recover to the original file.
**Note**: Before using the script, make sure the file is generated by `Generate_TOC.py`, otherwise some wrong would be happen.
