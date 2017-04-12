import struct

def bmpinfo(path):
    with open(path, 'rb') as f:
        s = f.read(30)
    t = struct.unpack('<ccIIIIIIHH', s)
    if t[0] == b'B' and (t[1] == b'M' or t[1] == b'A'):
        print('size:',t[2],'color:',t[9])
    else:
        print('NOT BMP!')

bmpinfo('/Users/liyouzhi/dev/python/thumb.jpg')
bmpinfo('/Users/liyouzhi/dev/python/sss.bmp')

