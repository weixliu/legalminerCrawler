# coding:utf-8
import urllib2
import socket

TIMEOUT = 40
RETRIES = 10

def downLoad(url, timeout = TIMEOUT, retries = RETRIES):
    while True:
        try:
            response = urllib2.urlopen(url, timeout=40)
            content = response.read()
            break
        except socket.timeout, e:
            retries -= 1
            if retryTimes == 0:
                content = None
                break
        except urllib2.URLError, e:
            retries -= 1
            if retryTimes == 0:
                content = None
                break
        except Exception, e:
            retries -= 1
            if retryTimes == 0:
                content = None
                break
    return content
