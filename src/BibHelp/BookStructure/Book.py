import re
from src.BibHelp.BookStructure.BiblePart import BiblePart
from src.BibHelp.BookStructure.Chapter import Chapter
from src.BibHelp.BibleMap import BookNameManager


class Book(BiblePart):
    def __init__(self, name: str):
        book_name = name.strip()

        self.name = BookNameManager.book_name(book_name)
        self.chapters = []

    @classmethod
    def from_reg_exp(cls, match: re.Match):
        book_name = match.group(1)
        return cls(book_name)

    def add_chapter(self, chapter: Chapter):
        self.chapters.insert(chapter.number, chapter)

    def get_chapter_count(self):
        return len(self.chapters)

    def print(self):
        print(f'[Book] {self.name}')

    def all_count(self):
        res = 0
        for chapter in self.chapters:
            res = res + chapter.count()
        return res

    def info(self):
        return f'[{self.name.ntc_ru_long}]: Chapters: {len(self.chapters)}. All verses: {self.all_count()}'
