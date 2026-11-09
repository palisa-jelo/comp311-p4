"""Convert one RV32I hexadecimal word per line to Digital ROM CSV."""
import csv
import re
import sys


def convert_to_csv(input_file, output_file):
    words = []
    with open(input_file) as source:
        for number, line in enumerate(source, 1):
            word = line.strip()
            if not word:
                continue
            if not re.fullmatch(r'(?:0[xX])?[0-9a-fA-F]{1,8}', word):
                raise ValueError(f'Line {number}: expected one 32-bit hexadecimal word')
            words.append(f'0x{int(word, 16):08x}')
    if not words:
        raise ValueError('Input contains no instructions')
    if len(words) > 1024:
        raise ValueError('Program exceeds the 1024-word instruction ROM')
    # Clear the rest of ROM so shorter programs do not retain stale instructions.
    words += ['0x00000000'] * (1024 - len(words))
    with open(output_file, 'w', newline='') as output:
        csv.writer(output).writerows(words[i:i + 8] for i in range(0, 1024, 8))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('Usage: python3 format.py INPUT.mem OUTPUT.csv')
    try:
        convert_to_csv(sys.argv[1], sys.argv[2])
    except (OSError, ValueError) as error:
        sys.exit(str(error))
    print(f'Wrote {sys.argv[2]} (1024 ROM cells, eight per row).')
