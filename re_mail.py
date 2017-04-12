import re

address1 = re.compile(r'^[\w\d][\w\d!#\$%&\'\*\+-/=\?\^_`\{\|\}~\.]*@\w+\.\w+$')
address2 = re.compile(r'^<(\w+\s\w+)>\s([\w\d][\w\d!#\$%&\'\*\+-/=\?\^_`\{\|\}~\.]*@\w+\.\w+$)')

print(address1.match('someone@gmail.com'))
print(address1.match('bill.gates@microsoft.com'))
print(address2.match('<Tom Paris> tom@voyager.org').groups())




