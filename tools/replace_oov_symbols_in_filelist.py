"""
Replaces out-of-vocabulary symbols from a VITS filelist TXT file and outputs the results in a separate file

Leaves the symbols that may be written as a word for further manual processing.
 The symbols may include %, $,*, etc., for Lithuanian, foreign language letters q, w, x, etc.

VITS filelist is a TXT file where every line has an entry corresponding to a audio/text pair zipper entry.
 Each entry has a format of <path-to-wav>|<text>
"""
import itertools
import re
from dataclasses import dataclass, replace
from pathlib import Path

from src.file import read_txt
from src.text.cleaners import collapse_whitespace
from src.zipper.core import oov_replacement_vocabulary


@dataclass
class Entry:
    filepath: str
    text: str


def line_to_entry(line: str):
    return Entry(filepath=line.split('|')[0], text=line.split('|')[1])


def replace_oov_symbols(entry: Entry):
    return [replace(entry, text=re.sub(fr"{symbol}", replacement, entry.text))
            for symbol, replacement in oov_replacement_vocabulary.items()]


# def collapse_whitespace(entry):
#     return replace(entry, text=re.sub(r"[ ]{2,}", ' ', entry.text))


def collapse_newlines(entry: Entry):
    return replace(entry, text=re.sub(r"\n\s*\n", r'\n', entry.text))


if __name__ == '__main__':
    in_filepath = Path(
        "/files/files/filelists/aurimas_stressed_val_filelist.txt")
    out_filepath = Path("/home/arnas/Downloads/aurimas_stressed_val_filelist.txt")

    text = read_txt(in_filepath)
    lines = text.split('\n')
    entries = map(line_to_entry, lines)
    entries = map(replace_oov_symbols, entries)
    entries = itertools.chain.from_iterable(entries)
    entries = map(collapse_whitespace, entries) # did not test with the cleaners' version of collapse_whitespace method
    entries = map(collapse_newlines, entries)

    contents = '\n'.join([f"{entry.filepath}|{entry.text}" for entry in entries])
    with open(out_filepath, mode='w', encoding='utf-8') as f:
        f.write(contents)
