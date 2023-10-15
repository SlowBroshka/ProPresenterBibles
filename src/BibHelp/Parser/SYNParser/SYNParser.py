from src.BibHelp.Parser.IBiblePartParser import IBiblePartParser
from src.BibHelp.BookStructure import Book
from src.BibHelp.BookStructure import Chapter
from src.BibHelp.BookStructure.Verse import Verse
from src.BibHelp.BookStructure import OldTestament
from src.BibHelp.BookStructure import NewTestament
from src.BibHelp.Parser.PartParser import PartParser


class SYNPArser(IBiblePartParser):

    def testament_parser(self) -> PartParser:
        return PartParser(r'^((Новый Завет)|(Ветхий Завет))\n$',
                          lambda match: OldTestament() if match.group(1).strip() == "Ветхий Завет"
                          else NewTestament())

    def book_parser(self) -> PartParser:
        """
        """
        return PartParser(r'^(\w(\w|-|\.|\s)+?)\n$',
                          lambda match: Book(match.group(1)))

    def chapter_parser(self) -> PartParser:
        """
        """
        return PartParser(r'^((Глава)|(Псалом))\s+(\d+?)\n$',
                          lambda match: Chapter(int(match.group(4))))

    def verse_parser(self) -> PartParser:
        """
        """
        return PartParser(r'^(\d+)\s(.+?)\n$',
                          lambda match: Verse(int(match.group(1)), match.group(2)))
