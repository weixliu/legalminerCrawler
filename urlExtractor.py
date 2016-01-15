# coding:utf-8
from connection import downLoad
import json
from threading import Thread
import re
from mySQLInstance import conn
from lxml import etree
from urlPattern import extractNum
import MySQLdb

class Extractor(Thread):
    def setResultNum(self, lastType, resultNum, queue):
        self.lastType = lastType
        self.resultNum = resultNum
        self.queue = queue
    def run(self):
        idPattern = re.compile(r'<a class="title s" href="(.*?)">', re.M)
        urlPrefix = 'http://www.legalminer.com'
        startPage = 1
        endPage = self.resultNum/10 + 2 #开区间
        for pNum in range(startPage, endPage):
            urlPattern = 'http://www.legalminer.com/ajax_search/get_html?t=&page=%d&searchType=%s' % (pNum, self.lastType)
            content = downLoad(urlPattern)
            contentDict = json.loads(content)
            for html in contentDict['result']['html']:
                sr = idPattern.search(html)
                lid = sr.group(1)
                urlC = urlPrefix + lid
                #传入队列中
                self.queue.put(urlC)
        #结束
        self.queue.put('OVER')

class Transmit(Thread):
    def setEndNum(self, endNum, queue, ProcessQueue, PendNum):
        self.endNum = endNum
        self.queue = queue
        self.ProcessQueue = ProcessQueue
        self.PendNum = PendNum
    def run(self):
        endCount = 0
        while True:
            if not self.queue.empty():
                urlC = self.queue.get()
                if urlC == 'OVER':
                    endCount += 1
                    if endCount == self.endNum:
                        break
                else:
                    self.ProcessQueue.put(urlC)
        for i in range(self.PendNum):
            self.ProcessQueue.put('OVER')

class PTTransmit(Thread):
    def setParams(self, ProcessQueue, ThreadQueue, nextThreadNum):
        self.PQ = ProcessQueue
        self.TQ = ThreadQueue
        self.NTN = nextThreadNum
    def run(self):
        while True:
            if not self.PQ.empty():
                urlC = self.PQ.get()
                if urlC == 'OVER':
                    break
                else:
                    self.TQ.put(urlC)
        for i in range(self.NTN):
            self.TQ.put('OVER')

class DataExtractor(Thread):
    def setParams(self, ThreadQueue):
        self.TQ = ThreadQueue
    def run(self):
        while True:
            if not self.TQ.empty():
                urlC = self.TQ.get()
                if urlC == 'OVER':
                    break
                else:
                    if urlC.find('lawfirm') != -1:
                        processLawFirm(urlC, self.TQ)
                    elif urlC.find('lawyer') != -1:
                        processLawyer(urlC, self.TQ)
                    elif urlC.find('court') != -1:
                        processCourt(urlC, self.TQ)
                    elif urlC.find('judge') != -1:
                        processJudge(urlC, self.TQ)
                    elif urlC.find('corporate') != -1:
                        processCorporate(urlC, self.TQ)
                    else:
                        pass

def processLawFirm(urlC, queue):
    content = downLoad(urlC)

    mc_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw heading']/div[@class='title']"
    zh_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='rw val'][1]"
    dz_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='rw val'][2]"
    dh_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='rw val'][3]"
    cz_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='rw val'][4]"
    gw_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='rw val'][5]/a"
    ssaj_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell'][1]/a[@class='rw val textLink']"
    slsj_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell'][2]/div[@class='rw val']"
    zyzt_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell'][3]/div[@class='rw val']"
    fzr_path="/html/body[@class='lvzhi lawfirm']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell'][4]/div[@class='rw val']"

    tree=etree.HTML(content)

    pattern_zh = re.compile(r'<div class="rw val"><i class="fa fa-info-circle icon highlight"></i>(.*?)</div>',re.M)
    pattern_dz = re.compile(r'<div class="rw val"><i class="fa fa-location-arrow icon highlight"></i>(.*?)</div>',re.M)
    pattern_dh = re.compile(r'<div class="rw val"><i class="fa fa-phone icon highlight"></i>(.*?)</div>',re.M)
    pattern_cz = re.compile(r'<div class="rw val"><i class="fa fa-print icon highlight"></i>(.*?)</div>',re.M)
    pattern_gw = re.compile(r'<div class="rw val"><a href="(.*?)" target="_blank"><i class="fa fa-external-link icon highlight"></i>官网链接</a></div>',re.M)
    pattern_lssl = re.compile(r'>([0-9]*?)位律师</a>',re.M)

    node_mc = tree.xpath(mc_path)
    node_ssaj = tree.xpath(ssaj_path)
    node_slsj = tree.xpath(slsj_path)
    node_zyzt = tree.xpath(zyzt_path)
    node_fzr = tree.xpath(fzr_path)

    reLst = []

    match1 = pattern_zh.search(content)
    match2 = pattern_dz.search(content)
    match3 = pattern_dh.search(content)
    match4 = pattern_cz.search(content)
    match5 = pattern_gw.search(content)
    match6 = pattern_lssl.search(content)
    
    reLst.append(urlC)
    law_firm_name = u'未知';
    law_firm_lawyer_number = 0;
    occupation_number = u'未知';
    address = u'未知';
    phone_number = u'未知';
    fax_number = u'未知';
    link = u'未知'
    case_number = 0
    history = 0
    state = u'未知'
    principle = u'未知'
    if node_mc[0].text != None:
        law_firm_name = node_mc[0].text.strip().replace('\n','').replace('\t','').replace('\r','').split('  ')[0].strip()
    if match6 != None:
        law_firm_lawyer_number = int(match6.group(1))
    if match1 != None:
        occupation_number = match1.group(1)
        occupation_number = occupation_number if occupation_number.find(' ') == -1 else occupation_number.split(' ')[1]
    if match2 != None:
        address = match2.group(1)
    if match3 != None:
        phone_number = match3.group(1)
    if match4 != None:
        fax_number = match4.group(1)
    if match5 != None:
        link = match5.group(1)
    if node_ssaj[0].text!=None:
        case_number = extractNum(node_ssaj[0].text.strip())
    if node_slsj[0].text!=None:
        history = extractNum(node_slsj[0].text.strip())
    if node_zyzt[0].text!=None:
        state = node_slsj[0].text.strip()
    if node_fzr[0].text!=None:
        principle = node_fzr[0].text.strip()

    reLst.append(law_firm_name)
    reLst.append(law_firm_lawyer_number)
    reLst.append(occupation_number)
    reLst.append(address)
    reLst.append(phone_number)
    reLst.append(fax_number)
    reLst.append(link)
    reLst.append(case_number)
    reLst.append(history)
    reLst.append(state)
    reLst.append(principle)

    try:
        cur=conn.cursor()
        cur.execute('insert into lawfirm values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', reLst)
        conn.commit()
        cur.close()
    except MySQLdb.Error,e:
        queue.put(urlC)

def processLawyer(urlC, queue):
    content = downLoad(urlC)

    xm_path="/html/body[@class='lvzhi lawyer']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw heading']/div[@class='title']"
    zyzh_path="/html/body[@class='lvzhi lawyer']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='rw val highlight']"
    lsmc_path="/html/body[@class='lvzhi lawyer']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='rw val'][1]"
    ssaj_path="/html/body[@class='lvzhi lawyer']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell'][1]/a[@class='rw val textLink']"
    jy_path="/html/body[@class='lvzhi lawyer']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell'][2]/div[@class='rw val']"
    xl_path="/html/body[@class='lvzhi lawyer']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell'][3]/div[@class='rw val']"
    xb_path="/html/body[@class='lvzhi lawyer']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell'][4]/div[@class='rw val']"
    zyzt_path="/html/body[@class='lvzhi lawyer']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell'][5]/div[@class='rw val']"
    
    tree=etree.HTML(content)

    node_xm = tree.xpath(xm_path)
    node_zyzh = tree.xpath(zyzh_path)
    node_lsmc = tree.xpath(lsmc_path)
    node_ssaj = tree.xpath(ssaj_path)
    node_jy = tree.xpath(jy_path)
    node_xl = tree.xpath(xl_path)
    node_xb = tree.xpath(xb_path)
    node_zyzt = tree.xpath(zyzt_path)

    reLst = []

    reLst.append(urlC)
    lawyer_name = u'未知'
    occupation_number = u'未知'
    law_firm_name = u'未知'
    case_number = 0
    history = 0
    education = u'未知'
    gender = u'未知'
    state = u'未知'

    if node_xm[0].text != None:
        lawyer_name = node_xm[0].text.split(' ')[0]
    if node_zyzh[0].text != None:
        occupation_number = node_zyzh[0].text.split(' ')[1]
    if node_lsmc[0].text != None:
        law_firm_name = node_lsmc[0].text
    if node_ssaj[0].text != None:
        case_number = extractNum(node_ssaj[0].text)
    if node_jy[0].text != None:
        history = extractNum(node_jy[0].text)
    if node_xl[0].text != None:
        education = node_xl[0].text
    if node_xb[0].text != None:
        gender = node_xb[0].text
    if node_zyzt[0].text != None:
        state = node_zyzt[0].text

    """
    reLst.append('None' if node_xm[0].text==None else node_xm[0].text.encode('utf-8'))
    reLst.append('None' if node_zyzh[0].text==None else node_zyzh[0].text.encode('utf-8'))
    reLst.append('None' if node_lsmc[0].text==None else node_lsmc[0].text.encode('utf-8'))
    reLst.append('None' if node_ssaj[0].text==None else node_ssaj[0].text.encode('utf-8'))
    reLst.append('None' if node_jy[0].text==None else node_jy[0].text.encode('utf-8'))
    reLst.append('None' if node_xl[0].text==None else node_xl[0].text.encode('utf-8'))
    reLst.append('None' if node_xb[0].text==None else node_xb[0].text.encode('utf-8'))
    reLst.append('None' if node_zyzt[0].text==None else node_zyzt[0].text.encode('utf-8'))
    """

    reLst.append(lawyer_name)
    reLst.append(occupation_number)
    reLst.append(law_firm_name)
    reLst.append(case_number)
    reLst.append(history)
    reLst.append(education)
    reLst.append(gender)
    reLst.append(state)

    try:
        cur=conn.cursor()
        cur.execute('insert into lawyer values(%s, %s, %s, %s, %s, %s, %s, %s, %s)', reLst)
        conn.commit()
        cur.close()
    except MySQLdb.Error,e:
        queue.put(urlC)

def processCourt(urlC, queue):
    content = downLoad(urlC)

    xm_path = "/html/body[@class='lvzhi court']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw heading']/div[@class='title']"
    ssaj_path = "/html/body[@class='lvzhi court']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell']/a[@class='rw val textLink']"

    tree=etree.HTML(content)

    node_xm = tree.xpath(xm_path)
    node_ssaj = tree.xpath(ssaj_path)

    reLst = []

    reLst.append(urlC)
    court_name = u'未知'
    case_number = 0

    if node_xm[0].text != None:
        court_name = node_xm[0].text.strip()
    if node_ssaj[0].text != None:
        case_number = extractNum(node_ssaj[0].text)
    """
    reLst.append('None' if node_xm[0].text==None else node_xm[0].text.encode('utf-8'))
    reLst.append('None' if node_ssaj[0].text==None else node_ssaj[0].text.encode('utf-8'))
    """

    reLst.append(court_name)
    reLst.append(case_number)

    try:
        cur=conn.cursor()
        cur.execute('insert into court values(%s, %s, %s)', reLst)
        conn.commit()
        cur.close()
    except MySQLdb.Error,e:
        queue.put(urlC)

def processJudge(urlC, queue):
    content = downLoad(urlC)

    xm_path = "/html/body[@class='lvzhi judge']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw heading']/div[@class='title']"
    fy_path = "/html/body[@class='lvzhi judge']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='rw val']"
    ssaj_path = "/html/body[@class='lvzhi judge']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='info-cell pull-right']/div[@class='cell']/a[@class='rw val textLink']"

    tree=etree.HTML(content)

    node_xm = tree.xpath(xm_path)
    node_fy = tree.xpath(fy_path)
    node_ssaj = tree.xpath(ssaj_path)

    reLst = []

    reLst.append(urlC)
    judge_name = u'未知'
    court = u'未知'
    case_number = 0

    if node_xm[0].text != None:
        judge_name = node_xm[0].text.split(' ')[0]
    if node_fy[0].text != None:
        court = node_fy[0].text
    if node_ssaj[0].text != None:
        case_number = extractNum(node_ssaj[0].text)

    """
    reLst.append('None' if node_xm[0].text==None else node_xm[0].text.encode('utf-8'))
    reLst.append('None' if node_fy[0].text==None else node_fy[0].text.encode('utf-8'))
    reLst.append('None' if node_ssaj[0].text==None else node_ssaj[0].text.encode('utf-8'))
    """

    reLst.append(judge_name)
    reLst.append(court)
    reLst.append(case_number)

    try:
        cur=conn.cursor()
        cur.execute('insert into judge values(%s, %s, %s, %s)', reLst)
        conn.commit()
        cur.close()
    except MySQLdb.Error,e:
        queue.put(urlC)

def processCorporate(urlC, queue):
    content = downLoad(urlC)

    gspath="/html/body[@class='lvzhi corporate']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw heading']/div[@class='title']"
    gppath="/html/body[@class='lvzhi corporate']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='col']/div[@class='rw val'][1]"
    dzpath="/html/body[@class='lvzhi corporate']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='col']/div[@class='rw val'][2]"
    dhpath="/html/body[@class='lvzhi corporate']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='col']/div[@class='rw val'][3]"
    gwpath="/html/body[@class='lvzhi corporate']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list']/div[@class='col']/div[@class='rw val'][4]/a"
    sjpath="/html/body[@class='lvzhi corporate']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list pull-right']/div[@class='col']/div[@class='rw val'][1]"
    dbpath="/html/body[@class='lvzhi corporate']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list pull-right']/div[@class='col']/div[@class='rw val'][2]"
    hypath="/html/body[@class='lvzhi corporate']/div[@id='bodyWrapper']/div[@id='content']/div[@id='basicInfo']/div[@class='content row']/div[@class='info col-sm-10']/div[@class='rw']/div[@class='list pull-right']/div[@class='col']/div[@class='rw val'][3]"

    tree=etree.HTML(content)

    node_gs = tree.xpath(gspath)
    node_gp = tree.xpath(gppath)
    node_dz = tree.xpath(dzpath)
    node_dh = tree.xpath(dhpath)
    node_gw = tree.xpath(gwpath)
    node_sj = tree.xpath(sjpath)
    node_db = tree.xpath(dbpath)
    node_hy = tree.xpath(hypath)

    reLst = []

    reLst.append(urlC)
    corporate_name = u'未知'
    stock_id = u'未知'
    address = u'未知'
    phone = u'未知'
    link = u'未知'
    ipo_time = u'未知'
    principle = u'未知'
    industry = u'未知'

    if node_gs[0].text != None:
        corporate_name = node_gs[0].text
    if node_gp[0].text != None:
        stock_id = node_gp[0].text
    if node_dz[0].text != None:
        address = node_dz[0].text
    if len(node_dh) != 0:
        phone = "".join(node_dh[0].itertext()).strip().replace('\n','').replace('\t','').replace('\r','')
    if len(node_gw) != 0:
        link = node_gw[0].attrib.get('href','None')
    if len(node_sj) != 0:
        ipo_time = "".join(node_sj[0].itertext()).strip().replace('\n','').replace('\t','').replace('\r','')
    if len(node_db) != 0:
        principle = "".join(node_db[0].itertext()).strip().replace('\n','').replace('\t','').replace('\r','')
    if len(node_hy) != 0:
        industry = "".join(node_hy[0].itertext()).strip().replace('\n','').replace('\t','').replace('\r','')

    """
    reLst.append('None' if node_gs[0].text==None else node_gs[0].text.encode('utf-8'))
    reLst.append('None' if node_gp[0].text==None else node_gp[0].text.encode('utf-8'))
    reLst.append('None' if node_dz[0].text==None else node_dz[0].text.encode('utf-8'))
    reLst.append('None' if len(node_dh)==0 else "".join(node_dh[0].itertext()).encode('utf-8').strip().replace('\n','').replace('\t','').replace('\r',''))
    reLst.append('None' if len(node_gw)==0 else node_gw[0].attrib.get('href','None').encode('utf-8'))
    reLst.append('None' if len(node_sj)==0 else "".join(node_sj[0].itertext()).encode('utf-8').strip().replace('\n','').replace('\t','').replace('\r',''))
    reLst.append('None' if len(node_db)==0 else "".join(node_db[0].itertext()).encode('utf-8').strip().replace('\n','').replace('\t','').replace('\r',''))
    reLst.append('None' if len(node_hy)==0 else "".join(node_hy[0].itertext()).encode('utf-8').strip().replace('\n','').replace('\t','').replace('\r',''))
    """

    reLst.append(corporate_name)
    reLst.append(stock_id)
    reLst.append(address)
    reLst.append(phone)
    reLst.append(link)
    reLst.append(ipo_time)
    reLst.append(principle)
    reLst.append(industry)

    try:
        cur=conn.cursor()
        cur.execute('insert into corporate values(%s, %s, %s, %s, %s, %s, %s, %s, %s)', reLst)
        conn.commit()
        cur.close()
    except MySQLdb.Error,e:
        queue.put(urlC)