import os

from src.utils.Utils import Utils
from src.BibHelp.Parser.VisioBibleParser.VisioBibleHTMParser import VisioBibleHTMParser
from src.BibHelp.Parser.BibleParser import BibleParser
from src.BibHelp.Parser.DBParser.DBParser import DBParser
from src.dump.DBDumper import SQLiteDBumper
from src.dump.USXDumper import USXDumper
from src.usx.simpleRuUSXWriter.SimpleRuUSXWriter import SimpleRuUSXWriter
from src.BibHelp.Parser.NRTParser import NRTParser
from src.BibHelp.Bible import Bible

# For visiobible to usx and sql
DB_NAME = '/home/vladk/Desktop/bible_work/bible.db3'
VISIOBIBLE_FOLDER_PATH = r'/home/vladk/Desktop/bible_work/nrt/'
# NRT_TXT_FILE = r'/home/vladk/git/ProPresenterBibles/versions/IBS.txt'
USX_RES_FOLDER = r'/home/vladk/Desktop/bible_work/res'



def parse_ru_visiobible_and_dump_to_sql_and_usx(ru_visiobible_path: str,
                                                sql_dump_path: str,
                                                usx_dump_path: str):
    usx_res_path = Utils.prep_path(usx_dump_path)

    visio_bible_parser = VisioBibleHTMParser()
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

    bible_parser = BibleParser(NRTParser.NRTParser())

    bible = bible_parser.parse_all_dir(src_bible_path, '*.html')
    bible.print_all_books_info()

    sqlite_dumper = SQLiteDBumper(bible=bible)
    sqlite_dumper.dump(sql_dump_path)
    sqlite_dumper.modify_for_pp()
    sqlite_dumper.close()

    usx_dumper = USXDumper(bible=bible, usx_writer=SimpleRuUSXWriter(os.getcwd()))
    usx_dumper.dump(usx_res_path)


def parse_from_another_sqlite(sql_src_path: str,
                              sql_dump_path: str,
                              usx_dump_path: str):
    usx_res_path = Utils.prep_path(usx_dump_path)
    veses_list = DBParser.all_verses(sql_src_path)

    bible = Bible.from_db(veses_list)
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

    # parse_simple_txt_and_dump_to_sql_and_usx(src_bible_path=VISIOBIBLE_FOLDER_PATH,
    #                                          sql_dump_path=DB_NAME,
    #                                          usx_dump_path=USX_RES_FOLDER)

    DB_SRC_PATH = r'/home/vladk/Desktop/bible_work/BTI/BTI15.SQLite3'
    parse_from_another_sqlite(sql_src_path=DB_SRC_PATH,
                                             sql_dump_path=DB_NAME,
                                             usx_dump_path=USX_RES_FOLDER)


if __name__ == '__main__':
    main()
