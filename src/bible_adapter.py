import io
import os
from pathlib import Path

from BibHelp.Bible import *
from src.usx.simpleRuUSXWriter.SimpleRuUSXWriter import SimpleRuUSXWriter
from src.BibHelp.Parser.TXTParser import Parsers
from src.dump.DBDumper import SQLiteDBumper

IBS_FILE_PATH = r'SYN.txt'
DB_NAME = 'bible.db3'


def clean_dir(path: str):
    [f.unlink() for f in Path(path).glob('*') if f.is_file()]


def prep_path(dest_folder_name: str) -> str:
    cwd = os.getcwd()
    res_path = os.path.join(cwd, dest_folder_name)
    Path(res_path).mkdir(parents=True, exist_ok=True)
    clean_dir(res_path)
    return res_path


def main():
    usx_res_path = prep_path('tmp')

    bible = Bible()

    sqlite_dumper = SQLiteDBumper(bible=bible)
    sqlite_dumper.dump(DB_NAME)
    sqlite_dumper.close()




    # bible.dump_to_usx_format(usx_res_path)

if __name__ == '__main__':
    main()
