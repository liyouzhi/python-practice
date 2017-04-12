import os

def find_str(s):
    for i in os.walk('.'):
        for j in i[2]:
            if j.find(s) != -1:
                print('filename:',j, '\npath:', i[0])

