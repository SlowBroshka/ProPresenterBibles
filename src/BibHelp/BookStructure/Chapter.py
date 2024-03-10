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
        if verse not in self.verses:
            self.verses.insert(verse.number, verse)
        else:
            raise ValueError(f'Verse [({verse.number}) {verse.content}] exist in Chapter: [{self.number}]')
        return self

    def get_verse(self, number: int) -> Verse | None:
        for verse in self.verses:
            if verse.number == number:
                return verse
        return None


    def get_verses_count(self):
        return len(self.verses)

    def print(self):
        print(f'[Chapter] {self.number}')

    def count(self):
        return len(self.verses)

    def __eq__(self, item):
        if isinstance(item, Verse):
            return self.number == item.number and self.verses == item.verses
        raise TypeError(f'Invalid type')
