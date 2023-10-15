import re
from src.BibHelp.BookStructure.BiblePart import BiblePart
from src.BibHelp.BookStructure.Verse import Verse


class Chapter(BiblePart):
    def __init__(self, number: int):
        self.number = number
        self.verses = []

    @classmethod
    def from_reg_exp(cls, match: re.Match):
        chapter_num = int(match.group(1))
        return cls(chapter_num)

    def add_verse(self, verse: Verse):
        self.verses.insert(verse.number, verse)
        return self

    def get_verses_count(self):
        return len(self.verses)

    def print(self):
        print(f'[Chapter] {self.number}')

    def count(self):
        return len(self.verses)
