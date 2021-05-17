import pyperclip
import argparse
from pywinauto.application import Application


def message(text):
    app = Application(backend="uia").connect(title="BORGChat v0.9.9.435")
    window = app.top_window()
    pyperclip.copy(text.encode('utf-8').decode())
    window.type_keys('^v')
    window.type_keys('^{ENTER}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=False, help='File with message to send')
    parser.add_argument('-q', action='store_true', help='Whether quote message or not')
    parser.add_argument('text', nargs='?', help='Message to send')
    args = parser.parse_args()
    text = None
    if args.f:
        with open(args.f, encoding='utf-8') as s:
            text = s.read()
    elif args.text:
        text = args.text

    if text and args.q:
        text = '[QUOTE]{}[/QUOTE]'.format(text)

    if text:
        message(text)
