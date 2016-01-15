# coding:utf-8

from multiprocessing import Process
from multiprocessing import Queue as PQueue
from Queue import Queue as TQueue
import time
import multiprocessing
from connection import downLoad
from lxml import etree
import urlPattern
from urlExtractor import Extractor
from urlExtractor import Transmit
from urlExtractor import PTTransmit
from urlExtractor import DataExtractor
from mySQLInstance import conn

URL_QUEUE = PQueue()
LOG_QUEUE = PQueue()

CONTENT_CRAWLER_NUM = 4
CONTENT_CRAWLER_THREAD_NUM = 4

def urlCrawler(urlQueue, logQueue):
    rooturl =  {
        'lawfirm':  'http://www.legalminer.com/search/lawfirm?t=',
        'lawyer':   'http://www.legalminer.com/search/lawyer?t=',
        'court':    'http://www.legalminer.com/search/court?t=',
        'judge':    'http://www.legalminer.com/search/judge?t=',
        'corporate':'http://www.legalminer.com/search/corporate?t='
    }
    rootNum = {}
    for key, url in rooturl.items():
        content = downLoad(url)
        tree = etree.HTML(content)
        resultNumNode = tree.xpath(urlPattern.resultNumXpath)
        rootNum[key] = urlPattern.extractNum(resultNumNode[0].text)
    #每个链接创建一个生产线程提取url
    threadQueue = TQueue()
    ThreadLst = []
    for key, value in rootNum.items():
        extractor = Extractor()
        extractor.setResultNum(key, int(value), threadQueue)
        ThreadLst.append(extractor)
    transmit = Transmit()
    transmit.setEndNum(len(rootNum), threadQueue, urlQueue, CONTENT_CRAWLER_NUM)
    ThreadLst.append(transmit)
    for e in ThreadLst:
        e.start()
    for e in ThreadLst:
        e.join()

def contentCrawler(urlQueue, logQueue):
    ThreadLst = []
    threadQueue = TQueue()
    pttransmit = PTTransmit()
    pttransmit.setParams(urlQueue, threadQueue, CONTENT_CRAWLER_THREAD_NUM)
    ThreadLst.append(pttransmit)
    for i in range(CONTENT_CRAWLER_THREAD_NUM):
        dataExtractor = DataExtractor()
        dataExtractor.setParams(threadQueue)
        ThreadLst.append(dataExtractor)
    for e in ThreadLst:
        e.start()
    for e in ThreadLst:
        e.join()

def indicator(logQueue):
    pass

if __name__ == '__main__':
    urlCrawlerProcess = Process(target = urlCrawler, args = (URL_QUEUE, LOG_QUEUE), name = 'URL_PROCESS')
    urlCrawlerProcess.start()

    for i in range(CONTENT_CRAWLER_NUM):
        contentCrawlerProcess = Process(target = contentCrawler, args = (URL_QUEUE, LOG_QUEUE), name = 'CONTENT_PROCESS-%d' % i)
        contentCrawlerProcess.start()

    while(True):
        print u'**********************活跃子进程************************************'
        for p in multiprocessing.active_children():
            print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
        print u'**********************进程通信队列的长度****************************'
        print URL_QUEUE.qsize()
        if len( multiprocessing.active_children() ) == 0:
            print u'任务结束'
            conn.close()
            break
        time.sleep(60)


