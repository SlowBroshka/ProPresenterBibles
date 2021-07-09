-- Create db struct for ProPresenter using my struct from python code

-- Create table for books
BEGIN TRANSACTION;

DROP TABLE IF EXISTS ZBOOK;
CREATE TABLE ZBOOK
(
    Z_PK            INTEGER PRIMARY KEY,
    Z_ENT           INTEGER,
    Z_OPT           INTEGER,
    ZBOOK_INDEX     INTEGER,
    ZTOBIBLE        INTEGER,
    ZBOOK_NAME      VARCHAR,
    ZBOOK_TESTIMENT VARCHAR
);

INSERT INTO ZBOOK (Z_PK, Z_ENT, Z_OPT, ZBOOK_INDEX, ZTOBIBLE, ZBOOK_NAME, ZBOOK_TESTIMENT)
SELECT books.pk        AS PK,
       2               AS ENT,
       1               AS OPT,
       books.pk        AS BOOK_INDEX,
       1               AS TOBIBLE,
       books.book_name AS NAME,
       NULL            AS TESTIMENT
FROM books;

CREATE INDEX ZBOOK_ZTOBIBLE_INDEX ON ZBOOK (ZTOBIBLE);
COMMIT;

-- Create table for Chapters
BEGIN TRANSACTION;

DROP TABLE IF EXISTS ZCHAPTER;
CREATE TABLE ZCHAPTER
(
    Z_PK            INTEGER PRIMARY KEY,
    Z_ENT           INTEGER,
    Z_OPT           INTEGER,
    ZCHAPTER_NUMBER INTEGER,
    ZTOBOOK         INTEGER
);

INSERT INTO ZCHAPTER (Z_PK, Z_ENT, Z_OPT, ZCHAPTER_NUMBER, ZTOBOOK)
SELECT chapters.pk          AS PK,
       3                    AS ENT,
       2                    AS OPT,
       chapters.chapter_num AS CHAPTER_NUMBER,
       chapters.book_id     AS BOOK
FROM chapters;

CREATE INDEX ZCHAPTER_ZTOBOOK_INDEX ON ZCHAPTER (ZTOBOOK);
COMMIT;

-- Create table for Verses
BEGIN TRANSACTION;

DROP TABLE IF EXISTS ZVERSE;
CREATE TABLE ZVERSE
(
    Z_PK           INTEGER PRIMARY KEY,
    Z_ENT          INTEGER,
    Z_OPT          INTEGER,
    ZVERSE_NUMBER  INTEGER,
    ZTOCHAPTER     INTEGER,
    ZVERSE_CONTENT VARCHAR
);

INSERT INTO ZVERSE (Z_PK, Z_ENT, Z_OPT, ZVERSE_NUMBER, ZTOCHAPTER, ZVERSE_CONTENT)
SELECT verses.pk         AS PK,
       4                 AS ENT,
       1                 AS OPT,
       verses.verse_num  AS VERSE_NUMBER,
       verses.chapter_id AS CHAPTER,
       verses.content    AS CONTENT
FROM verses;

CREATE INDEX ZVERSE_ZTOCHAPTER_INDEX ON ZVERSE (ZTOCHAPTER);
COMMIT;

-- Create specific tables for PP (maybe can work without this table (not tested))
BEGIN TRANSACTION;

DROP TABLE IF EXISTS Z_PRIMARYKEY;
CREATE TABLE Z_PRIMARYKEY
(
    Z_ENT   INTEGER PRIMARY KEY,
    Z_NAME  VARCHAR,
    Z_SUPER INTEGER,
    Z_MAX   INTEGER
);

INSERT INTO Z_PRIMARYKEY(Z_ENT, Z_NAME, Z_SUPER, Z_MAX)
VALUES (1, 'Bible', 0, 1),
       (2, 'Book', 0, (SELECT COUNT(books.pk) FROM books)),
       (3, 'Chapter', 0, (SELECT COUNT(chapters.pk) FROM chapters)),
       (4, 'Verse', 0, (SELECT COUNT(verses.pk) FROM verses));
COMMIT;

-- Create specific tables for PP (maybe can work without this table (not tested))
BEGIN TRANSACTION;

DROP TABLE IF EXISTS ZBIBLE;
CREATE TABLE ZBIBLE
(
    Z_PK                       INTEGER PRIMARY KEY,
    Z_ENT                      INTEGER,
    Z_OPT                      INTEGER,
    ZBIBLE_PUBLISHER           VARCHAR,
    ZBIBLE_NAME                VARCHAR,
    ZBIBLE_COPYRIGHT           VARCHAR,
    ZBIBLE_CHECKSUM            VARCHAR,
    ZBIBLE_REGISTRATION_NAME   VARCHAR,
    ZBIBLE_LANGUAGE            VARCHAR,
    ZBIBLE_ABBREVIATION        VARCHAR,
    ZBIBLE_REGISTRATION_NUMBER VARCHAR
);

-- TODO: Use it like template
-- ZBIBLE_ABBREVIATION should be from translate that i want to replace
INSERT INTO ZBIBLE (Z_PK, Z_ENT, Z_OPT, ZBIBLE_PUBLISHER, ZBIBLE_NAME, ZBIBLE_COPYRIGHT, ZBIBLE_CHECKSUM,
                    ZBIBLE_REGISTRATION_NAME, ZBIBLE_LANGUAGE, ZBIBLE_ABBREVIATION, ZBIBLE_REGISTRATION_NUMBER)
VALUES (1, 2, 1, 'Public Domain', 'New Russian Translation', 'Public Domain', 'XXXXXXXXXXX', 'Public Domain', 'Russian',
        'ACV', 'Public Domain');
COMMIT;
