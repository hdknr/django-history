from datetime import datetime, timedelta
import os
import shutil


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.expanduser('~') + '/Library/Application Support/Google/Chrome/Default/history'
DST = os.path.join(BASE_DIR, 'chrome.sqlite3')


def clonedb():
    shutil.copy2(SRC, DST)


if __name__ == '__main__':
    clonedb()