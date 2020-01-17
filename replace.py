'''
基于正则表达式，替换文件中的字符串。
'''
import re
import argparse


parser = argparse.ArgumentParser(description=r"""This script is use to replace string in a file. For example: python replace.py --file 1.py --src "([\u4e00-\u9fa5])(\w)" --dst "$1 $2" """)
parser.add_argument('--file', help='a valid file path', type=str, required=True)
parser.add_argument('--src', help='the source string, which is a regular expression.', type=str, required=True)
parser.add_argument('--dst', help='the destination string', type=str, required=True)
parser.add_argument('--encoding', help='the encoding of the original file, which is utf-8 by default.', type=str, default='utf-8')
args = parser.parse_args()


try:
    # read the file
    with open(args.file, 'r', encoding=args.encoding) as f:
        text = f.read()
        print('Handling file: {}'.format(args.file), end='\t\t... ')

    # handling
    pattern = re.compile(args.src)
    result = text[:]
    for match in pattern.findall(text):
        if isinstance(match, str):
            result = result.replace(match, args.dst)
        elif isinstance(match, tuple):
            for i, m in enumerate(match, 1):
                dst = args.dst.replace('${}'.format(i), m)
                pattern.sub(dst, result)

    # save the result
    with open(args.file, 'w', encoding=args.encoding) as f:
        f.write(result)
        print('done')

except Exception as e:
    print('Error: {}'.format(str(e)))
