import os.path

from src.usx.USXWriter import AbstractUSXWriter


class SimpleRuUSXWriter(AbstractUSXWriter):

    def __init__(self, current_work_dir: str):
        super().__init__(current_work_dir)

    def start_book(self, alias: str, name: str) -> str:
        super(SimpleRuUSXWriter, self).add_book(alias, name)

        pattern_str = f'<?xml version="1.0" encoding="utf-8"?>\n' \
                      f'<usx version="2.0">\n' \
                      f'  <book code="{alias}" style="id">{name}</book>\n' \
                      f'<para style="mt">{name}</para>\n'
        return pattern_str

    def end_book(self, alias: str, name: str) -> str:
        pattern_str = f'</usx>'
        return pattern_str

    def start_chapter(self, number: int) -> str:
        pattern_str = f'  <chapter number="{str(number)}" style="c" />\n'
        return pattern_str

    def end_chapter(self, number: int) -> str:
        return super(SimpleRuUSXWriter, self).end_chapter(number)

    def start_verse(self, number: int, content: str) -> str:
        pattern_str = f'    <para style="p">\n' \
                      f'    <verse number="{str(number)}" style="v" />{content}</para>\n'
        return pattern_str

    def end_verse(self, number: int, content: str) -> str:
        return super(SimpleRuUSXWriter, self).end_verse(number, content)

    def generate_metadata(self) -> str:
        res = str()
        with open(self.__get_template_file_path(), "r") as template:
            res = f"{template.read()}".format(
                book_names_list=self.__generate_book_names(),
                codes=self.__generate_codes())
        return res

    def __generate_book_names(self):
        res_str = str()
        for code, book in self.code_to_name_map.items():
            pattern = f'        <book code="{code}">\n' \
                      f'            <long>{book}</long>\n' \
                      f'            <short>{book}</short>\n' \
                      f'            <abbr>{book}</abbr>\n' \
                      f'        </book>\n'
            res_str += pattern
        return res_str

    def __generate_codes(self):
        res_str = str()
        for code, _, in self.code_to_name_map.items():
            pattern = f'                <book code="{code}" />\n'
            res_str += pattern
        return res_str

    def __get_template_file_path(self):
        template_file_path = "usx/simpleRuUSXWriter/metadata-in.xml"
        return os.path.join(self.cwd, template_file_path)
