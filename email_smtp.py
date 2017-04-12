from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#from_addr = input('From: ')
#password = input('Password: ')
to_addr = input('To: ')
#smtp_server = input('SMTP server: ')
from_addr = 'lyz317453967@163.com'
#password = 'uC49NZhxFNL?d6m'
password = '832435pop'
#to_addr = 'lyz317453967@163.com'
smtp_server = 'smtp.163.com'
smtp_port = 25

msg = MIMEMultipart('alternative')
msg_text = MIMEText('<html><body><h1>Hello, ZP</h1>' +
        '<p>send by <a href="http://weibo.com/lasuna">LYZ</a>...\nsend with a file...</p>' +
                '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('妹妹<%s>' % from_addr)
msg['To'] = _format_addr('哥哥<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候2。。。', 'utf-8').encode()
msg.attach(MIMEText('HELLO', 'plain', 'utf-8'))
msg.attach(msg_text)

with open('/Users/liyouzhi/dev/python/code.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
