from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.google.cn')) as page:
    for line in page:
        print(line)


