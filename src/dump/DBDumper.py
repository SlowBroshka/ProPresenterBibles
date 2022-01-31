from src.dump.AbstractDumper import AbstractDump
from src.BibHelp.Bible import Bible
from src.dump.DBManager import DBConnection


class SQLiteDBumper(AbstractDump):

    def __init__(self, bible: Bible):
        super().__init__(bible)
        self.db = ...  # type: DBConnection

    def dump(self, path: str = 'bible_db.sqlite'):
        self.db = DBConnection(path)
        self.db.create_db_struct()

        all_books = self.bible.get_all_books()
        self.db.fill_all(all_books)

    def modify_for_pp(self):
        self.db.adap_db_for_pp()

    def close(self):
        self.db.close()
