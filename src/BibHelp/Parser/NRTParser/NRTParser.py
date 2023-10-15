from src.BibHelp.Parser.IBiblePartParser import IBiblePartParser

from src.BibHelp.BookStructure.Book import Book
from src.BibHelp.BookStructure.Chapter import Chapter
from src.BibHelp.BookStructure.Verse import Verse
from src.BibHelp.BookStructure.Testament import NewTestament, OldTestament
from src.BibHelp.Parser.PartParser import PartParser


class NRTParser(IBiblePartParser):

    def __init__(self):
        super().__init__()

    def testament_parser(self) -> PartParser:
        """
        The file does not contain any information about the Testament.
        And I'm too lazy to insert this information into the book structure in BibleMap.py
        """
        return PartParser(r'^((Новый Завет)|(Ветхий Завет))\n$',
                          lambda match: OldTestament() if match.group(1).strip() == "Ветхий Завет"
                          else NewTestament())

    def book_parser(self) -> PartParser:
        """
        Parse book: <body><div><h1>Бытие</h1>
        """
        return PartParser(r'^\<body\>\<div\>\<h1\>(.+)\<\/h1\>$', lambda match: Book(match.group(1)))

    def chapter_parser(self) -> PartParser:
        """
        Parse digit <br><strong>8</strong>
        """
        return PartParser(r'\<br\>\<strong\>(\d+)\<\/strong\>', lambda match: Chapter(int(match.group(1))))

    def verse_parser(self) -> PartParser:
        """
        Parse and clean up text: <sup>1</sup><pb/>Было ко мне слово Господне: <pb/>
        """
        return PartParser(r'^\<sup\>(\d+)\<\/sup\>(.+)$', lambda match: Verse(int(match.group(1)), match.group(2)))

# Смотри в BibleParser
# Тут пишешь регулярки для всех + делаешь функции фильтрации
# в книги добавляешь параметр из какого он завета
