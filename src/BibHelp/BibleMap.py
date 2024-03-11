class BookName:

    # TODO: Put information about the Testament in this struct
    def __init__(self, aliases: list, ntc_ru_long: str, en_abbr: str):
        self.aliases = aliases
        self.ntc_ru_long = ntc_ru_long
        self.en_abbr = en_abbr

    def has_alias(self, alias: str) -> bool:
        return alias in self.aliases

    def to_str(self):
        return f'{self.ntc_ru_long}: {self.en_abbr}'


class BookInBible:

    def __init__(self, book: BookName, index: int):
        self.book = book
        self.index = index


class BookNameManager:

    @staticmethod
    def book_name(name: str) -> BookName:
        for bookName in BookNameManager.all_books:
            if bookName.has_alias(name):
                return bookName
        raise NameError(f'[ERROR]: Can\'t map book: [{name}]')

    @staticmethod
    def index_in_bible(name: str) -> int:
        index = 1
        for bookName in BookNameManager.all_books:
            if bookName.has_alias(name):
                return index
            index += 1
        raise NameError(f'[ERROR]: Can\'t find book by name: [{name}]')

    @staticmethod
    def book_in_bible(name: str) -> BookInBible:
        index = 1
        for bookName in BookNameManager.all_books:
            if bookName.has_alias(name):
                return BookInBible(bookName, index)
            index += 1
        raise NameError(f'[ERROR]: Can\'t map book: [{name}]')

    all_books = [
        BookName(['Бытие'], 'Бытие', 'GEN'),
        BookName(['Исход'], 'Исход', 'EXO'),
        BookName(['Левит'], 'Левит', 'LEV'),
        BookName(['Числа'], 'Числа', 'NUM'),
        BookName(['Второзаконие'], 'Второзаконие', 'DEU'),
        BookName(['Иисус Навин', 'Книга Иисуса Навина'], 'Иисус Навин', 'JOS'),
        BookName(['Судьи', 'Книга Судей израилевых', 'Книга судей'], 'Судьи', 'JDG'),
        BookName(['Руфь', 'Книга Руфи'], 'Руфь', 'RUT'),
        BookName(['1 Царств', '1-я Царств', 'Первая книга Царств [Первая Самуила]', 'Первая книга Царств',
                  'Первая книга царств'], '1 Царств',
                 '1SA'),
        BookName(['2 Царств', '2-я Царств', 'Вторая книга Царств [Вторая Самуила]', 'Вторая книга Царств',
                  'Вторая книга царств'], '2 Царств',
                 '2SA'),
        BookName(['3 Царств', '3-я Царств', 'Третья книга Царств [Первая Царей]', 'Третья книга Царств',
                  'Третья книга царств'], '3 Царств',
                 '1KI'),
        BookName(['4 Царств', '4-я Царств', 'Четвертая книга Царств [Вторая Царей]', 'Четвертая книга Царств',
                  'Четвертая книга царств'],
                 '4 Царств',
                 '2KI'),
        BookName(['1 Паралипоменон', '1-я Паралипоменон', 'Первая книга Паралипоменон'],
                 '1 Паралипоменон', '1CH'),
        BookName(['2 Паралипоменон', '2-я Паралипоменон', 'Вторая книга Паралипоменон'],
                 '2 Паралипоменон', '2CH'),
        BookName(['Ездра', 'Первая книга Ездры', 'Книга Эзры'], 'Ездра', 'EZR'),
        BookName(['Неемия', 'Книга Неемии'], 'Неемия', 'NEH'),
        BookName(['Есфирь', 'Книга Есфири', 'Книга Эсфири'], 'Есфирь', 'EST'),
        BookName(['Иов', 'Книга Иова'], 'Иов', 'JOB'),
        BookName(['Псалтирь', 'Псалтырь'], 'Псалтирь', 'PSA'),
        BookName(['Притчи', 'Притчи Соломона', 'Книга притчей Соломоновых'], 'Притчи', 'PRO'),
        BookName(['Екклесиаст', 'Книга Екклезиаста, или Проповедника', 'Книга Экклезиаста, или Проповедника'],
                 'Екклесиаст', 'ECC'),
        BookName(['Песня Песней', 'Песнь песней Соломона'], 'Песня Песней', 'SNG'),
        BookName(['Исаия', 'Книга пророка Исаии', 'Книга пророка Исайи'], 'Исаия', 'ISA'),
        BookName(['Иеремия', 'Книга пророка Иеремии'], 'Иеремия', 'JER'),
        BookName(['Плач Иеремии'], 'Плач Иеремии', 'LAM'),
        BookName(['Иезекииль', 'Книга пророка Иезекииля'], 'Иезекииль', 'EZK'),
        BookName(['Даниил', 'Книга пророка Даниила'], 'Даниил', 'DAN'),
        BookName(['Осия', 'Книга пророка Осии'], 'Осия', 'HOS'),
        BookName(['Иоиль', 'Книга пророка Иоиля'], 'Иоиль', 'JOL'),
        BookName(['Амос', 'Книга пророка Амоса'], 'Амос', 'AMO'),
        BookName(['Авдий', 'Книга пророка Авдия'], 'Авдий', 'OBA'),
        BookName(['Иона', 'Книга пророка Ионы'], 'Иона', 'JON'),
        BookName(['Михей', 'Книга пророка Михея'], 'Михей', 'MIC'),
        BookName(['Наум', 'Книга пророка Наума'], 'Наум', 'NAM'),
        BookName(['Аввакум', 'Книга пророка Аввакума'], 'Аввакум', 'HAB'),
        BookName(['Софония', 'Книга пророка Софонии'], 'Софония', 'ZEP'),
        BookName(['Аггей', 'Книга пророка Аггея'], 'Аггей', 'HAG'),
        BookName(['Захария', 'Книга пророка Захарии'], 'Захария', 'ZEC'),
        BookName(['Малахия', 'Книга пророка Малахии'], 'Малахия', 'MAL'),
        BookName(['От Матфея', 'От Матфея святое благовествование', 'Евангелие по Матфею'], 'От Матфея', 'MAT'),
        BookName(['От Марка', 'От Марка святое благовествование', 'Евангелие по Марку'], 'От Марка', 'MRK'),
        BookName(['От Луки', 'От Луки святое благовествование', 'Евангелие по Луке'], 'От Луки', 'LUK'),
        BookName(['От Иоанна', 'От Иоанна святое благовествование', 'Евангелие по Иоанну'], 'От Иоанна', 'JHN'),
        BookName(['Деяния', 'Деяния святых апостолов', 'Деяния апостолов'], 'Деяния', 'ACT'),
        BookName(['К Римлянам', 'Послание к Римлянам святого апостола Павла', 'Послание к Римлянам',
                  'Послание апостола Павла христианам в Риме'], 'К Римлянам',
                 'ROM'),
        BookName(['1 Коринфянам', '1-е Коринфянам', 'Первое послание к Коринфянам святого апостола Павла',
                  'Первое послание к Коринфянам', 'Первое послание апостола христианам в Коринфе'],
                 '1 Коринфянам',
                 '1CO'),
        BookName(['2 Коринфянам', '2-е Коринфянам', 'Второе послание к Коринфянам святого апостола Павла',
                  'Второе послание к Коринфянам', 'Второе послание апостола христианам в Коринфе'],
                 '2 Коринфянам',
                 '2CO'),
        BookName(['К Галатам', 'Послание к Галатам святого апостоля Павла', 'Послание к Галатам',
                  'Послание апостола Павла христианам в Галатии'], 'К Галатам', 'GAL'),
        BookName(['К Ефесянам', 'Послание к Ефесянам святого апостола Павла', 'Послание к Ефесянам',
                  'Послание апостола Павла христианам в Эфесе'], 'К Ефесянам',
                 'EPH'),
        BookName(['К Филиппийцам', 'Послание к Филиппийцам святого апостола Павла', 'Послание к Филиппийцам',
                  'Послание апостола Павла христианам в Филиппах'],
                 'К Филиппийцам', 'PHP'),
        BookName(['К Колоссянам', 'Послание к Колоссянам святого апостола Павла', 'Послание к Колоссянам',
                  'Послание апостола Павла христианам в Колоссах'],
                 'К Колоссянам', 'COL'),
        BookName(['1 Фессалоникийцам', '1-е Фессалоникийцам',
                  'Первое послание к Фессалоникийцам (Солунянам) святого апостола Павла',
                  'Первое послание к Фессалоникийцам...', 'Первое послание к Фессалоникийцам',
                  'Первое послание апостола Павла христианам в Фессалонике'], '1 Фессалоникийцам',
                 '1TH'),
        BookName(['2 Фессалоникийцам', '2-е Фессалоникийцам',
                  'Второе послание к Фессалоникийцам (Солунянам) святого апостола Павла',
                  'Второе послание к Фессалоникийцам...', 'Второе послание к Фессалоникийцам',
                  'Второе послание апостола Павла христианам в Фессалонике'], '2 Фессалоникийцам',
                 '2TH'),
        BookName(['1 Тимофею', '1-е Тимофею', 'Первое послание к Тимофею святого апостола Павла',
                  'Первое послание к Тимофею', 'Первое послание апостола Павла Тимофею'], '1 Тимофею',
                 '1TI'),
        BookName(['2 Тимофею', '2-е Тимофею', 'Второе послание к Тимофею святого апостола Павла',
                  'Второе послание к Тимофею', 'Второе послание апостола Павла Тимофею'], '2 Тимофею',
                 '2TI'),
        BookName(
            ['К Титу', 'Послание к Титу святого апостола Павла', 'Послание к Титу', 'Послание апостола Павла Титу'],
            'К Титу', 'TIT'),
        BookName(['К Филимону', 'Послание к Филимону святого апостола Павла', 'Послание к Филимону',
                  'Послание апостола Павла Филимону'], 'К Филимону',
                 'PHM'),
        BookName(['К Евреям', 'Послание к Евреям святого апостола Павла', 'Послание к Евреям', 'Послание к евреям'],
                 'К Евреям', 'HEB'),
        BookName(['Иакова', 'Соборное послание святого апостола Иакова', 'Послание Иакова'], 'Иакова', 'JAS'),
        BookName(['1 Петра', '1-е Петра', 'Первое соборное послание святого апостола Петра', 'Первое послание Петра'],
                 '1 Петра', '1PE'),
        BookName(['2 Петра', '2-е Петра', 'Второе соборное послание святого апостола Петра', 'Второе послание Петра',
                  'Второе послание апостола Петра', 'Первое послание апостола Петра'],
                 '2 Петра', '2PE'),
        BookName(
            ['1 Иоанна', '1-е Иоанна', 'Первое соборное послание святого апостола Иоанна', 'Первое послание Иоанна',
             'Первое послание апостола Иоанна'],
            '1 Иоанна',
            '1JN'),
        BookName(
            ['2 Иоанна', '2-е Иоанна', 'Второе соборное послание святого апостола Иоанна', 'Второе послание Иоанна',
             'Второе послание апостола Иоанна'],
            '2 Иоанна',
            '2JN'),
        BookName(
            ['3 Иоанна', '3-е Иоанна', 'Третье соборное послание святого апостола Иоанна', 'Третье послание Иоанна',
             'Третье послание апостола Иоанна'],
            '3 Иоанна',
            '3JN'),
        BookName(['Иуды', 'Соборное послание святого апостола Иуды', 'Послание Иуды'], 'Иуды', 'JUD'),
        BookName(
            ['Откровение', 'Откровение святого Иоанна Богослова (Апокалипсис)', 'Откровение ап. Иоанна Богослова...',
             'Откровение ап. Иоанна Богослова', 'Откровение Иоанна'],
            'Откровение', 'REV')
    ]
