#Author: Tonmoy M
#URL: https://qinetique.github.io

from html.parser import HTMLParser
class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print('Start :',tag)
        for x in attrs:
            print('->', x[0], '>', x[1])

    def handle_endtag(self, tag: str) -> None:
        print('End   :', tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print('Empty :', tag)
        for x in attrs:
            print('->' , x[0], '>', x[1])

parser = CustomHTMLParser()

for i in range(int(input())):
    parser.feed(input())
