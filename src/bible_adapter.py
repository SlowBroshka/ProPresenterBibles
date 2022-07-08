import os

from src.utils.Utils import Utils
from src.BibHelp.Parser.VisioBibleParser.VisioBibleParser import VisioBibleParser
from src.BibHelp.Parser.SYNParser.SYNPartParsers import *
from src.BibHelp.Parser.BibleParser import BibleParser
from src.dump.DBDumper import SQLiteDBumper
from src.dump.USXDumper import USXDumper
from src.usx.simpleRuUSXWriter.SimpleRuUSXWriter import SimpleRuUSXWriter

# For visiobible to usx and sql
DB_NAME = '../tmp/bible.db3'
VISIOBIBLE_FOLDER_PATH = r'/home/vladk/Desktop/RU_RST/'
NRT_TXT_FILE = r'/home/vladk/git/ProPresenterBibles/versions/IBS.txt'
USX_RES_FOLDER = r'../tmp/usx_nrt'


def parse_ru_visiobible_and_dump_to_sql_and_usx(ru_visiobible_path: str,
                                                sql_dump_path: str,
                                                usx_dump_path: str):
    usx_res_path = Utils.prep_path(usx_dump_path)

    visio_bible_parser = VisioBibleParser()
    bible = visio_bible_parser.parse_all(ru_visiobible_path)

    bible.print_all_books_info()

    sqlite_dumper = SQLiteDBumper(bible=bible)
    sqlite_dumper.dump(sql_dump_path)
    sqlite_dumper.modify_for_pp()
    sqlite_dumper.close()

    usx_dumper = USXDumper(bible=bible, usx_writer=SimpleRuUSXWriter(os.getcwd()))
    usx_dumper.dump(usx_res_path)


def parse_simple_txt_and_dump_to_sql_and_usx(src_bible_path: str,
                                             sql_dump_path: str,
                                             usx_dump_path: str):
    usx_res_path = Utils.prep_path(usx_dump_path)

    bible_parser = BibleParser(testament_parser=testamentParser,
                               book_parser=bookParser,
                               chapter_parser=chapterParser,
                               verse_parser=verseParser)

    bible = bible_parser.parse_all(src_bible_path)
    bible.print_all_books_info()

    sqlite_dumper = SQLiteDBumper(bible=bible)
    sqlite_dumper.dump(sql_dump_path)
    sqlite_dumper.modify_for_pp()
    sqlite_dumper.close()

    usx_dumper = USXDumper(bible=bible, usx_writer=SimpleRuUSXWriter(os.getcwd()))
    usx_dumper.dump(usx_res_path)


def main():
    # parse_ru_visiobible_and_dump_to_sql_and_usx(ru_visiobible_path=VISIOBIBLE_FOLDER_PATH,
    #                                             sql_dump_path=DB_NAME,
    #                                             usx_dump_path=USX_RES_FOLDER)

    parse_simple_txt_and_dump_to_sql_and_usx(src_bible_path=NRT_TXT_FILE,
                                             sql_dump_path=DB_NAME,
                                             usx_dump_path=USX_RES_FOLDER)


if __name__ == '__main__':
    main()
