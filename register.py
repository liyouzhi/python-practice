import hashlib

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'liyouzhi-the-salt')

def get_md5(s):
    md5  = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def login(username, password):
    if username in db:
        if db[username] == get_md5(password + username + 'liyouzhi-the-salt'):
            print('success!')
        else:
            print('password error!')
    else:
        print('username error!')


register('zhaopeng','asiadlfdkalfl!#@789')
register('liyouzhi','asdfghjkl!@#123')
login('zhaopeng','asiadlfdkalfl!#@789')
login('liyouzhi','adsfadf')
login('vx','sdffs')
