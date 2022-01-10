import re
import abc

from src.BibHelp.BibleMap import BookNameManager


class BiblePart(abc.ABC):

    @abc.abstractmethod
    def print(self):
        pass

    @staticmethod
    def clean_content(patterns: dict, content: str) -> str:
        """
        Some string in translate has double spaces,
        and maybe other not good readable parts
        Use regexp patterns to fix it.
        :param patterns: dict{regex -> replaced str}
        :param content:
        :return:
        """
        for pattern, replaced in patterns.items():
            content = pattern.sub(replaced, content)
        return content


class Verse(BiblePart):
    __clean_patterns = {re.compile(r' {2,}'): ' '}

    def __init__(self, number: int, content: str):
        self.number = number
        self.content = BiblePart.clean_content(Verse.__clean_patterns, content)

    @classmethod
    def from_reg_exp(cls, match: re.Match):
        verse_num = int(match.group(1))
        verse_content = match.group(2)
        return cls(verse_num, verse_content)

    def print(self):
        print(f'[Verse] {self.number} {self.content}')


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
        return f'[{self.name.ntc_ru_long}]: Chapters: {len(self.chapters)}. All verses: {self.all_count()} '


class Testament(BiblePart):
    def __init__(self):
        self.name = str()
        self.books = list()

    def add_book(self, book: Book):
        self.books.append(book)

    def print(self):
        print(f'[Testament] {self.name}')

    @staticmethod
    def from_reg_exp(math: re.Match):
        text = math.group(1)
        stripped = text.strip()
        if stripped == "Ветхий Завет":
            return OldTestament()
        elif stripped == "Новый Завет":
            return NewTestament()


class NewTestament(Testament):
    def __init__(self):
        super().__init__()
        self.name = "Новый Завет"


class OldTestament(Testament):
    def __init__(self):
        super().__init__()
        self.name = "Ветхий Завет"
