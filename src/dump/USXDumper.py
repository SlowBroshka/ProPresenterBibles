import os

from src.dump.AbstractDumper import AbstractDump
from src.BibHelp.Bible import Bible
from src.usx.USXWriter import AbstractUSXWriter


class USXDumper(AbstractDump):

    def __init__(self, bible: Bible, usx_writer: AbstractUSXWriter):
        super().__init__(bible)
        self.usx_writer = usx_writer

    def dump(self, path: str):
        all_books = self.bible.get_all_books()
        for book in all_books:
            en_abbr = book.name.en_abbr
            path_to_file = os.path.join(path, en_abbr + AbstractUSXWriter.USX_EXTENSION)

            with open(path_to_file, 'w') as file:
                file.write(self.usx_writer.start_book(en_abbr, book.name.ntc_ru_long))
                for chapter in book.chapters:
                    file.write(self.usx_writer.start_chapter(chapter.number))
                    for verse in chapter.verses:
                        file.write(self.usx_writer.start_verse(verse.number, verse.content))
                        file.write(self.usx_writer.end_verse(verse.number, verse.content))
                    file.write(self.usx_writer.end_chapter(chapter.number))
                file.write(self.usx_writer.end_book(en_abbr, book.name.ntc_ru_long))

        path_to_metadata = os.path.join(path, "metadata.xml")
        with open(path_to_metadata, 'w') as file:
            file.write(self.usx_writer.generate_metadata())
