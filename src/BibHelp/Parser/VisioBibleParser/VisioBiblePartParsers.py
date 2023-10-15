from src.BibHelp.BookStructure import Chapter
from src.BibHelp.BookStructure.Verse import Verse
from src.BibHelp.Parser.PartParser import PartParser

chapterParser = PartParser(r'^.*?(\d+?)$', lambda match: Chapter(int(match.group(1))))

verseParser = PartParser(r'^(\d+)\s(.+?)$', lambda match: Verse(int(match.group(1)), match.group(2)))
