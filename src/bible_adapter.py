import io
import os
from pathlib import Path

from src.BibHelp.Parser.VisioBibleParser.VisioBibleParser import VisioBibleParser
from src.BibHelp.Parser.BibleParser import BibleParser
from src.dump.DBDumper import SQLiteDBumper

TXT_BIBLE_PATH = r'SYN.txt'
DB_NAME = 'bible.db3'

VISIOBIBLE_FOLDER_PATH = r'/home/vladk/Desktop/RU_RST/'


def clean_dir(path: str):
    [f.unlink() for f in Path(path).glob('*') if f.is_file()]


def prep_path(dest_folder_name: str) -> str:
    cwd = os.getcwd()
    res_path = os.path.join(cwd, dest_folder_name)
    Path(res_path).mkdir(parents=True, exist_ok=True)
    clean_dir(res_path)
    return res_path


def main():
    # usx_res_path = prep_path('tmp')

    visioBibleParser = VisioBibleParser()
    bible = visioBibleParser.parse_all(VISIOBIBLE_FOLDER_PATH)
    sqlite_dumper = SQLiteDBumper(bible=bible)
    sqlite_dumper.dump(DB_NAME)
    sqlite_dumper.close()

    # bible_parser = BibleParser(testament_parser=testamentParser,
    #                            book_parser=bookParser,
    #                            chapter_parser=chapterParser,
    #                            verse_parser=verseParser)
    #
    # bible = bible_parser.parse_all(TXT_BIBLE_PATH)
    #
    # sqlite_dumper = SQLiteDBumper(bible=bible)
    # sqlite_dumper.dump(DB_NAME)
    # sqlite_dumper.close()

    # bible.dump_to_usx_format(usx_res_path)


if __name__ == '__main__':
    main()
