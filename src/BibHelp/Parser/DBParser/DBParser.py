import sqlite3


class DBParser:
    # -- Table like: | Book name | Chapter num | Verse num | verse content |
    __query = """
SELECT
       books.book_name AS bookName,
       chapters.chapter_num AS chapter,
       verses.verse_num AS verseNumber,
       verses.content AS content
FROM verses
JOIN chapters on verses.chapter_id = chapters.pk
    JOIN books ON books.pk = chapters.book_id
ORDER BY books.book_name, chapters.chapter_num, verses.verse_num
"""

    @staticmethod
    def all_verses(path='bible_db.sqlite'):
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(DBParser.__query)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return records
