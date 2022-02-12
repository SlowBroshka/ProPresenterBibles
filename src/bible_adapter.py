import os

from src.utils.Utils import Utils
from src.BibHelp.Parser.VisioBibleParser.VisioBibleParser import VisioBibleParser
from src.BibHelp.Parser.USXParser.USXBibleParser import USXBibleParser
from src.dump.DBDumper import SQLiteDBumper
from src.dump.USXDumper import USXDumper
from src.usx.simpleRuUSXWriter.SimpleRuUSXWriter import SimpleRuUSXWriter

# For visiobible to usx and sql
DB_NAME = '../tmp/niv_bible.db3'
VISIOBIBLE_FOLDER_PATH = r'/home/vladk/Рабочий стол/NIV_SRS/'
USX_RES_FOLDER = r'../tmp/niv_usx'


def parse_niv_usx_and_dump_to_sql_and_usx(path: str, sql_dump_path: str, usx_dump_path: str):
    usx_res_path = Utils.prep_path(usx_dump_path)

    bible_parser = USXBibleParser()
    bible = bible_parser.parse_all(path)

    bible.print_all_books_info()


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


# Not worked yet
def parse_simple_txt_and_dump_to_sql_and_usx():
    pass
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
    #
    # bible.dump_to_usx_format(usx_res_path)


def main():
    # parse_ru_visiobible_and_dump_to_sql_and_usx(ru_visiobible_path=VISIOBIBLE_FOLDER_PATH,
    #                                             sql_dump_path=DB_NAME,
    #                                             usx_dump_path=USX_RES_FOLDER)

    parse_niv_usx_and_dump_to_sql_and_usx(path=VISIOBIBLE_FOLDER_PATH,
                                          sql_dump_path=DB_NAME,
                                          usx_dump_path=USX_RES_FOLDER)


if __name__ == '__main__':
    main()
