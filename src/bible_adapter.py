import io
from pathlib import Path

from BibHelp.Bible import *
from src.usx.simpleRuUSXWriter.SimpleRuUSXWriter import SimpleRuUSXWriter


IBS_FILE_PATH = r'IBS.txt'
DB_NAME = 'bible.db3'


def prep_path(dest_folder_name: str) -> str:
    cwd = os.getcwd()
    res_path = os.path.join(cwd, dest_folder_name)
    Path(res_path).mkdir(parents=True, exist_ok=True)
    [f.unlink() for f in Path(res_path).glob('*') if f.is_file()]
    return res_path


def main():
    usx_res_path = prep_path('tmp')


    bible = Bible(SimpleRuUSXWriter(os.getcwd()))

    with io.open(IBS_FILE_PATH, encoding='utf-8') as reader:
        for line in reader:
            bible.parse_line(line)
    bible.dump_to_sql(DB_NAME)
    bible.modify_sql_for_pp()
    bible.close()

    bible.dump_to_usx_format(usx_res_path)

if __name__ == '__main__':
    main()
