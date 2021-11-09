import sys
# from pprint import pprint as print
from itertools import chain
from colorama import init as cinit, Fore, Back, Style
from NHentai.entities.doujin import Doujin
from NHentai.nhentai import NHentai
import argparse

cinit(autoreset=True)

parser = argparse.ArgumentParser(
    description='This app usage to find data of doujinshi on nhentai.net')

parser.add_argument('ID', type=int)

parser.add_argument('-t', '--tag',
                    dest='TAG',     action='store_true',
                    help='show tags of doujinshi')

parser.add_argument('-tt', '--title',
                    dest='TITLE',   action='store_true',
                    help='show title of doujinshi')

parser.add_argument('-a', '--artist',
                    dest='ARTIST',  action='store_true',
                    help='show artists of doujinshi')

parser.add_argument('-l', '--lang',
                    dest='LANG',    action='store_true',
                    help='show language of doujinshi')

parser.add_argument('-c', '--cat',
                    dest='CAT',     action='store_true',
                    help='show categories of doujinshi')

parser.add_argument('-ch', '--char',
                    dest='CHAR',    action='store_true',
                    help='show characters of doujinshi')

parser.add_argument('-p', '--par',
                    dest='PAROD',   action='store_true',
                    help='show parodies of doujinshi')

parser.add_argument('-g', '--group',
                    dest='GROUP',   action='store_true',
                    help='show groups of doujinshi')

parser.add_argument('-pg', '--pages',
                    dest='PAGES',   action='store_true',
                    help='show total pages of doujinshi')

parser.add_argument('-u', '--url',
                    dest='URL', action='store_true')

argc = parser.parse_args()

# print(vars(argc))


class MyDoujin:
    id: str = Fore.LIGHTGREEN_EX + 'Id: ' + Fore.LIGHTCYAN_EX
    title: str = Fore.LIGHTGREEN_EX + 'Title: ' + Fore.LIGHTCYAN_EX
    tag: str = Fore.LIGHTGREEN_EX + 'Tags: ' + Fore.LIGHTCYAN_EX
    artist: str = Fore.LIGHTGREEN_EX + 'Artists: ' + Fore.LIGHTCYAN_EX
    language: str = Fore.LIGHTGREEN_EX + 'Languages: ' + Fore.LIGHTCYAN_EX
    categories: str = Fore.LIGHTGREEN_EX + 'Categories: ' + Fore.LIGHTCYAN_EX
    characters: str = Fore.LIGHTGREEN_EX + 'Characters: ' + Fore.LIGHTCYAN_EX
    parodies: str = Fore.LIGHTGREEN_EX + 'Parodies: ' + Fore.LIGHTCYAN_EX
    groups: str = Fore.LIGHTGREEN_EX + 'Groups: ' + Fore.LIGHTCYAN_EX
    pages: str = Fore.LIGHTGREEN_EX + 'Total pages: ' + Fore.LIGHTCYAN_EX
    url: str = Fore.LIGHTGREEN_EX + 'URL: ' + Fore.YELLOW

    def __init__(self, id, title, tag, artist, lang, cat, char, par, groups, pages) -> None:
        self.id += id + '\n'
        self.title += title + '\n'
        self.tag += '#' + ' #'.join(tag) + '\n'
        self.artist += artist + '\n'
        self.language += lang + '\n'
        self.categories += cat + '\n'
        self.characters += char + '\n'
        self.parodies += par + '\n'
        self.groups += groups + '\n'
        self.pages += pages + '\n'
        self.url += f'nhentai.net/g/{id}\n'

    def all_data(self):
        return self.title +\
            self.tag +\
            self.artist +\
            self.language +\
            self.categories +\
            self.characters +\
            self.parodies +\
            self.groups +\
            self.pages +\
            self.url


def get_data(argc):
    manga_id: int = argc.ID
    is_alone = True

    nhentai = NHentai()
    doujin: Doujin = nhentai.get_doujin(manga_id)
    mydoujin: MyDoujin = MyDoujin(str(doujin.id),
                                  str(doujin.title),
                                  sorted(doujin.tags),
                                  str(doujin.artists),
                                  str(doujin.languages),
                                  str(doujin.categories),
                                  str(doujin.characters),
                                  str(doujin.parodies),
                                  str(doujin.groups),
                                  str(doujin.total_pages))

    if argc.TITLE:
        is_alone = False
        yield mydoujin.title

    if argc.TAG:
        is_alone = False
        yield mydoujin.tag
        # yield f'#{tag.replace(" ", "_").replace("-", "")} '

    if argc.ARTIST:
        is_alone = False
        yield mydoujin.artist

    if argc.LANG:
        is_alone = False
        yield mydoujin.language

    if argc.CAT:
        is_alone = False
        yield mydoujin.categories

    if argc.CHAR:
        is_alone = False
        yield mydoujin.characters

    if argc.PAROD:
        is_alone = False
        yield mydoujin.parodies

    if argc.GROUP:
        is_alone = False
        yield mydoujin.groups

    if argc.PAGES:
        is_alone = False
        yield mydoujin.pages

    if argc.URL:
        is_alone = False
        yield mydoujin.url

    if is_alone:
        yield mydoujin.all_data()


def main():
    # argc = sys.argv[1:]
    print(''.join(get_data(argc)))
    # pass


if __name__ == '__main__':
    main()
