import urllib.request
import sys
import time

ipv4 = urllib.request.urlopen('http://ident.me').read().decode('utf8')

def sloweler(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)

sloweler(ipv4)