import io

from BibHelp.Bible import *


IBS_FILE_PATH = r'../IBS.txt'
DB_NAME = 'bible_db.sqlite'


def main():
    bible = Bible()

    with io.open(IBS_FILE_PATH, encoding='utf-8') as reader:
        for line in reader:
            bible.parse_line(line)
    bible.dump_to_sql(DB_NAME)
    bible.modify_sql_for_pp()
    bible.close()

if __name__ == '__main__':
    main()
