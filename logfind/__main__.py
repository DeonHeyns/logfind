__author__ = 'deonheyns'
import argparse
from logfind import Logfind

def main():
    parser = argparse.ArgumentParser(description='Logfind...')
    parser.add_argument('-o', nargs='?',
                        help='uses or logic to find text in log files. As in deon OR has OR blue OR eyes')
    args, text = parser.parse_known_args()
    text.append(args.o or '')
    text = ' '.join(text)

    if not text:
        parser.error('No search text provided to logfind')

    lf = Logfind()
    files = lf.find(text, args.o is not None)
    print('\r\n'.join(files))

if __name__ == "__main__":
    main()
