from src.BibHelp.BiblePart import Book, Chapter, Verse, OldTestament, NewTestament
from src.BibHelp.Parser.PartParser import PartParser

testamentParser = PartParser(r'^((Новый Завет)|(Ветхий Завет))\n$',
                             lambda match: OldTestament() if match.group(
                                 1).strip() == "Ветхий Завет" else NewTestament())

bookParser = PartParser(r'^(\w(\w|-|\.|\s)+?)\n$',
                        lambda match: Book(match.group(1)))

chapterParser = PartParser(r'^((Глава)|(Псалом))\s+(\d+?)\n$',
                           lambda match: Chapter(int(match.group(4))))

verseParser = PartParser(r'^(\d+)\s(.+?)\n$',
                         lambda match: Verse(int(match.group(1)), match.group(2)))
