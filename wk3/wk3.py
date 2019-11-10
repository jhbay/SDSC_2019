import requests
import json
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from nose.tools import assert_equal, assert_raises
# from pymongo import MongoClient
import time

# try:
#     imports = [requests, BeautifulSoup, RobotFileParser, assert_equal, assert_raises, json
#     # , MongoClient
#     ]
# except NameError as e:
#     print(e)
#     raise AssertionError('You appear to be missing one of the required libraries or functions')
# assert True
# print('Successfully imported libraries and functions')

def startTime():
    return time.time()  # 시작 시간 저장

def endTime(msg, sTime):
    print('msg: ', msg, " // time :", time.time() - sTime)  # 현재시각 - 시작시간 = 실행 시간


def get_establishment_by_id(id):
    # YOUR CODE HERE
    url = 'http://api.ratings.food.gov.uk/establishments/' + str(id)
    r = requestUrl(url)
    # print(r.json()['BusinessName'])
    return r.json()['BusinessName']


def requestUrl(url):
    heads={
        'x-api-version':'2',
        'content-type':'application/json'
    }
    return requests.get(url, headers=heads)

def requestUrlXmlType(url):
    heads={
        'x-api-version':'2',
        'content-type': 'application/xml'
    }
    return requests.get(url, headers=heads).text


def check_robots(url):
    # YOUR CODE HERE
    """
    Use the RobotFileParser to check if a page on the server can be visited
    """
    root = 'http://' + url.replace('http://', '').split('/')[0]
    try:
        rp = RobotFileParser()
        rp.set_url(root + '/robots.txt')
        rp.read()
        result = rp.can_fetch("*", url)
        print("fetch result::" + str(result)  )
        return result
    except NotImplementedError as e:
        # print(e)
        raise NotImplementedError() 
    
    
 
###### Main ####### 
# 1.a.
def quiz1a():
    print(get_establishment_by_id(990000))

# 1.b
def quiz1b():
    # Testing whether your code works correctly.  
    # You don't need to write anything here
    # Confirm an allowed page returns True
    assert check_robots('http://138.68.148.20/index.html')

    # Confirm a disallowed page returns False
    # 사실 false나와야함. 환경문제?
    assert not check_robots('http://138.68.148.20/data/scotland/glasgow_city') 
    # cf doc:: https://docs.python.org/ko/3/library/urllib.robotparser.html
    # ISSUE :: https://stackoverflow.com/questions/15344253/robotparser-doesnt-seem-to-parse-correctly

    print('Passed all the tests')

# 1.3


def parse_xml(url):
    """
    This function should parse the XML file, for example http://138.68.148.20/west_midlands/cannock_chase
    NOTE: Unlike for HTML, you need to use 'xml' as the second parameter for BeautifulSoup
    You may use any of Python's core libraries, or other libraries installed if you wish rather than BeautifulSoup
    """
    # YOUR CODE HERE 
    # 로봇유효성 확인- robots.txt // True / False(None)
    if(check_robots(url)):
        
        # url request 유효성 확인 
        urlHeads={
        'x-api-version':'2',
        'content-type':'application/xml'
        }
        requestStatus = requests.get(url, headers=urlHeads).status_code # 200 / 404(None)
        if(requestStatus == 200 ):
            # 답안 dictionary 생성.
            retDict = {}
            xmlHeads={
                'x-api-version':'2',
                'content-type': 'application/xml'
                , "Range": "bytes=0-1000" # xml의 부분만을 추출하기에 시간단축에 도움이 된다. 평균 36초 -> 6초.
            }
            # xml 형태로 반환 받아 크롤링. 시간 다소소요.(평균 36s)
            soup = BeautifulSoup(requests.get(url, headers=xmlHeads).text , 'xml') 
            retDict["first_business"] = str(soup.findAll('EstablishmentDetail')[0].find('BusinessName').string)
            retDict["amount_of_records"] = int(soup.find('ItemCount').string)
        else:
            # url request 가 404 인경우 None 반환
            retDict = None 
    else:
        # 로봇유효성이 False 인경우 None 반환
        retDict = None 
    return retDict




def quiz1c():
    # You don't need to write anything here
    # Confirm that the function calls the check_robots function
    sTime = startTime()
    parse_xml('http://138.68.148.20/data/west_midlands/cannock_chase')
    endTime('cannock_chase test',sTime)


    # tmp_requests = requests
    # del requests
    # parse_xml('http://138.68.148.20/data/scotland/glasgow_city')
    # parse_xml('http://138.68.148.20/data/scotland/clackmannanshire')

    sTime = startTime()
    assert_equal(parse_xml('http://138.68.148.20/data/west_midlands/cannock_chase'), {'amount_of_records': 731, 'first_business': '1st Choice Pizza/Fish & Chips'})
    endTime('assert cannock_chase - ',sTime)
    sTime = startTime()
    assert_equal(parse_xml('http://138.68.148.20/data/wales/swansea'), {'amount_of_records': 1700, 'first_business': '360 Beach and Watersports Centre'})
    endTime('assert swansea - ',sTime)
    # TEST HANDLING 404
    sTime = startTime()
    assert_equal(parse_xml('http://138.68.148.20/data/calderdale'), None)
    endTime('assert calderdale - ',sTime)
    print('All test successfully passed')



# quiz1a();
# quiz1b()
quiz1c()


