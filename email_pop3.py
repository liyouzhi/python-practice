import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = 'lyz317453967@163.com'
#password = 'uC49NZhxFNL?d6m'
password = '832435pop'
pop3_server = 'pop.163.com'

server = poplib.POP3(pop3_server)
#server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))
server.user(email)
server.pass_(password)
#return numbers and sizes of mails
print('Messages: %s. Size: %s' % server.stat())
#list()返回所有邮件的编号
resp, mails, octets = server.list()
#print(mails)
print('*' * 60)
#获取最新一封邮件，注意索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)
#lines储存了邮件的原始文本的每一行
msg_content = b'\r\n'.join(lines).decode('utf-8')
#print('msg_content', msg_content)
msg = Parser().parsestr(msg_content)

def decode_str(s):
#   print(decode_header(s))
    value, charset = decode_header(s)[0]
#   print('value: %s,charset: %s.' % (value, charset))
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
#       print('content_type:',content_type)
        pos = content_type.find('charset=')
#       print('pos:',pos)
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
#       print('charset:',charset)
    return charset

#indent用于缩进显示
def print_info(msg, indent=0):
#   print('indent=',indent)
    if indent == 0:
        for header in ('From','To', 'Subject'):
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  '*indent, header, value))
    if(msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%s------------------------------------------------------------' % ('  '*indent))
            print('%spart %s' % ('  '*indent, n))
            print('\n')
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  '*indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  '*indent, content_type))
            
print_info(msg)
print('*' * 60)
server.quit()
