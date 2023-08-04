#Author: Tonmoy M
#URL: https://qinetique.github.io

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print(tag)
        for x in attrs:
            print('->', x[0], '>', x[1])

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print(tag)
        for x in attrs:
            print('->' , x[0], '>', x[1])

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
