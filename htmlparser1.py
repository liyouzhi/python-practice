from html.parser import HTMLParser
from contextlib import closing
from urllib.request import urlopen

class MyHTMLParser(HTMLParser):

    def __init__(self):
        self.title = []
        self.time = []
        self.location = []
        self.sign = ''
        self.isShow = False
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if attrs:
            if attrs[0][1] == 'event-title':
                self.sign = 'title'
            elif tag == 'time':
                self.sign = 'time'
            elif attrs[0][1] == 'event-location':
                self.sign = 'location'
    
    def handle_data(self, data):
        if data == 'Upcoming Events':
            self.isShow = True
        elif data == 'You just missed...':
            self.isShow = False
        if self.isShow:
            if self.sign == 'title':
                self.title.append(data)
                self.sign = ''
            elif self.sign == 'time':
                self.time.append(data)
                self.sign = ''
            elif self.sign == 'location':
                self.location.append(data)
                self.sign = ''

parser = MyHTMLParser()
with closing(urlopen('https://www.python.org/events/python-events/')) as page:
    for line in page:
        parser.feed(str(line))

for i in range(len(parser.title)):
    print('-' * 25)
    print('Title: %s\nTime: %s\nLocation:%s' % (parser.title[i],parser.time[i],parser.location[i]))
print('-' * 25)

