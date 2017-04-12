from urllib import request, parse
from xml.parsers.expat import ParserCreate
from datetime import datetime,timedelta

class WeatherSaxHandler(object):
    def __init__(self):
        self.weatherdata = {'today':{},'tomorrow':{}}
    
    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.weatherdata['city'] = attrs['city']
            self.weatherdata['country'] = attrs['country']
        if name == 'yweather:condition':
            datetext = attrs['date']
            self.weatherdata['today']['date'] = datetime.strptime(datetext,'%a, %d %b %Y %I:%M %p %Z')
            self.weatherdata['tomorrow']['date'] = self.weatherdata['today']['date'] + timedelta(days=1)
            #print(self.weatherdata['today']['date'].strftime('%a'))
            #print(self.weatherdata['today']['date'].weekday())
        if name == 'yweather:forecast':
            if attrs['day'] == self.weatherdata['today']['date'].strftime('%a'):
                self.weatherdata['today']['text'] = attrs['text']
                self.weatherdata['today']['low'] = int(attrs['low'])
                self.weatherdata['today']['high'] = int(attrs['high'])
            if attrs['day'] == self.weatherdata['tomorrow']['date'].strftime('%a'):
                self.weatherdata['tomorrow']['text'] = attrs['text']
                self.weatherdata['tomorrow']['low'] = int(attrs['low'])
                self.weatherdata['tomorrow']['high'] = int(attrs['high'])

def fetch_xml(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
#   print(data)
#   print(type())
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(data)
    return handler.weatherdata

url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22beijing%2C%20china%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeysw%2C%20scotland%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

print(fetch_xml(url))
