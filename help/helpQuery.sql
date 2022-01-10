-- Verse count in each book
SELECT
       books.book_name AS bookName,
       count(verses.verse_num) AS verseCount
FROM verses
JOIN chapters on verses.chapter_id = chapters.pk
    JOIN books ON books.pk = chapters.book_id
GROUP BY books.book_name
ORDER BY books.book_name

-- Like previous query but use table struct from ProPresenter
SELECT
       ZBOOK.ZBOOK_NAME AS bookName,
       count(ZVERSE.ZVERSE_NUMBER) AS verseCount
FROM ZVERSE
JOIN ZCHAPTER on ZVERSE.ZTOCHAPTER = ZCHAPTER.Z_PK
    JOIN ZBOOK ON ZBOOK.Z_PK = ZCHAPTER.ZTOBOOK
GROUP BY ZBOOK.ZBOOK_NAME
ORDER BY ZBOOK.ZBOOK_NAME

------------------------------------------------------------

-- Verse count in each chapter in each book
SELECT
       books.book_name AS bookName,
       chapters.chapter_num AS chapter,
       count(verses.verse_num) AS verseCount
FROM verses
JOIN chapters on verses.chapter_id = chapters.pk
    JOIN books ON books.pk = chapters.book_id
GROUP BY books.book_name, chapters.chapter_num
ORDER BY books.book_name, chapters.chapter_num

-- Like previous query but use table struct from ProPresenter
SELECT
       ZBOOK.ZBOOK_NAME AS bookName,
       ZCHAPTER.ZCHAPTER_NUMBER AS chapter,
       count(ZVERSE.ZVERSE_NUMBER) AS verseCount
FROM ZVERSE
JOIN ZCHAPTER on ZVERSE.ZTOCHAPTER = ZCHAPTER.Z_PK
    JOIN ZBOOK ON ZBOOK.Z_PK = ZCHAPTER.ZTOBOOK
GROUP BY ZBOOK.ZBOOK_NAME, ZCHAPTER.ZCHAPTER_NUMBER
ORDER BY ZBOOK.ZBOOK_NAME, ZCHAPTER.ZCHAPTER_NUMBER

------------------------------------------------------------

-- Table like: | Book name | Chapter num | Verse num | verse content |
SELECT
       books.book_name AS bookName,
       chapters.chapter_num AS chapter,
       verses.verse_num AS verseNumber,
       verses.content AS content
FROM verses
JOIN chapters on verses.chapter_id = chapters.pk
    JOIN books ON books.pk = chapters.book_id
ORDER BY books.book_name, chapters.chapter_num, verses.verse_num

-- Like previous query but use table struct from ProPresenter
SELECT
       ZBOOK.ZBOOK_NAME AS book,
       ZCHAPTER.ZCHAPTER_NUMBER AS chapter,
       ZVERSE.ZVERSE_NUMBER AS number,
       ZVERSE.ZVERSE_CONTENT AS content
FROM ZVERSE
JOIN ZCHAPTER on ZVERSE.ZTOCHAPTER = ZCHAPTER.Z_PK
    JOIN ZBOOK ON ZBOOK.Z_PK = ZCHAPTER.ZTOBOOK
ORDER BY ZBOOK.ZBOOK_NAME, ZCHAPTER.ZCHAPTER_NUMBER, ZVERSE.ZVERSE_NUMBER