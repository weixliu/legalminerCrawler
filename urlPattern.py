# coding:utf-8
import re

resultNumXpath = "/html/body[@class='lvzhi search index']/div[@id='bodyWrapper']/div[@id='content']/div[@id='searchResult']/div[@class='content row']/div[@class='title resultTitle col-sm-12']"

def extractNum(string):
    intPattern = re.compile(r'[0-9]+', re.M)
    match = intPattern.search(string)
    if match != None:
        return match.group(0)
    return None