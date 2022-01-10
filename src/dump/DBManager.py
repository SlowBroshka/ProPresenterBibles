import sqlite3

CREATE_BOOKS = '''
DROP TABLE IF EXISTS books;
CREATE TABLE books
  (
     pk        INTEGER PRIMARY KEY,
     book_name VARCHAR
  ); 
'''

CREATE_CHAPTERS = '''
DROP TABLE IF EXISTS chapters;
CREATE TABLE chapters
  (
     pk          INTEGER PRIMARY KEY,
     book_id     INTEGER REFERENCES books,
     chapter_num INTEGER
  ); 
'''

CREATE_VERSES = '''
DROP TABLE IF EXISTS verses;
CREATE TABLE verses
  (
     pk         INTEGER PRIMARY KEY,
     chapter_id INTEGER REFERENCES chapters,
     verse_num  INTEGER,
     content    VARCHAR
  ); 
'''


class DBConnection:
    def __init__(self, path='bible_db.sqlite'):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def create_db_struct(self):
        self.cursor.executescript(CREATE_BOOKS)
        self.cursor.executescript(CREATE_CHAPTERS)
        self.cursor.executescript(CREATE_VERSES)
        self.conn.commit()

    def fill_all(self, all_books: list):
        # So important to pass equal books in fill_* functions
        self.__fill_books(all_books)
        self.__fill_chapters(all_books)
        self.__fill_verses(all_books)

    # Fragile and shitty inserting :(
    def __fill_books(self, books: list):
        pk_books = [[i + 1, books[i].name.ntc_ru_long] for i in range(len(books))]
        self.cursor.executemany('INSERT INTO books (PK, book_name) VALUES (?, ?)', pk_books)
        self.conn.commit()

    # More fragile and shitty inserting :(
    def __fill_chapters(self, books: list):
        pk = 0
        book_num = 0
        for book in books:
            book_num += 1
            chapters = [[pk := pk + 1, book_num, x + 1] for x in range(book.get_chapter_count())]
            self.cursor.executemany('INSERT INTO chapters (PK, book_id, chapter_num) VALUES (?, ?, ?)',
                                    chapters)
        self.conn.commit()

    # More and more fragile and shitty inserting :(
    def __fill_verses(self, books: list):
        pk = 0
        book_num = 0
        chapter_num = 0
        for book in books:
            book_num += 1
            for chapter in book.chapters:
                chapter_num += 1
                verses = [[pk := pk + 1, chapter_num, chapter.verses[x].number, chapter.verses[x].content] for x in
                          range(chapter.get_verses_count())]
                self.cursor.executemany('INSERT INTO verses (PK, chapter_id, verse_num, content) VALUES (?, ?, ?, ?)',
                                        verses)
        self.conn.commit()

    def adap_db_for_pp(self, path_to_sql_script='adaptDBStruct.sql'):
        with open(path_to_sql_script, 'r') as sql_file:
            sql_script = sql_file.read()
        self.cursor.executescript(sql_script)
        self.conn.commit()

    def close(self):
        self.conn.close()
