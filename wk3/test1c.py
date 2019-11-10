import requests
import json
import timeit
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from nose.tools import assert_equal, assert_raises

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
#         print("fetch result::" + str(result)  )
        return result
    except NotImplementedError as e:
        # print(e)
        raise NotImplementedError() 
    
def requestUrl(url):
    heads={
        'x-api-version':'2',
        'content-type':'application/json'
    }
    return requests.get(url, headers=heads)

def checkUrlStatus(url):
    try:
        statusCode = str(requestUrl(url).status_code)
#         print("checkUrlStatus :: " + statusCode) 
        return statusCode
    except NotImplementedError as e:
        # print(e)
        raise NotImplementedError()

def requestUrlXmlType(url):
    heads={
        'x-api-version':'2',
        'content-type': 'application/xml'
    }
    return requests.get(url, headers=heads).text        
        
def checkParsableUrl(code):
    # only request valid - 200
    if(code == '200' or code == 'True' or code == True):
        return True
    # else : False
    return None


def parse_xml(url):
    """
    This function should parse the XML file, for example http://138.68.148.20/west_midlands/cannock_chase
    NOTE: Unlike for HTML, you need to use 'xml' as the second parameter for BeautifulSoup
    You may use any of Python's core libraries, or other libraries installed if you wish rather than BeautifulSoup
    """
    # YOUR CODE HERE 
    # robotStatus = check_robots(url)
    # reqStatus = checkUrlStatus(url) 
    #check robots.txt
    print("Now working url : " + url)
    
    
    
    robotStatus = check_robots(url)
    print("robotStatus :: " + str(robotStatus) )
    if(robotStatus):
#         print("robotStatus parsable :: " + str(checkParsableUrl(check_robots(url))))
        
        heads={
        'x-api-version':'2',
        'content-type':'application/json'
        }
        reqStatus = requests.get(url, headers=heads).status_code
        print("reqStatus :: " + str(reqStatus) )

        if(reqStatus == 200 ):
#             print("reqStatus parsable :: " + str(checkParsableUrl(checkUrlStatus(url))))
            # retDict = beautifulSoupParseXml(url)
            retDict = {}
            soupHeads={
                'x-api-version':'2',
                'content-type': 'application/xml'
            }
            soup = BeautifulSoup(requests.get(url, headers=soupHeads).text, 'xml') 
            # print("first_business :: "  + str(soup.findAll('EstablishmentDetail')[0].find('BusinessName').string) )
            # print("amount_of_records :: "  + str(soup.find('ItemCount').string))
            
            retDict["first_business"] = str(soup.findAll('EstablishmentDetail')[0].find('BusinessName').string)
            retDict["amount_of_records"] = int(soup.find('ItemCount').string)
        else:
#             print('Result: None')
            retDict = None 
    else:
#         print('Result: None')
        retDict = None 
    return retDict

for i in range(3):
    start = timeit.default_timer()
    print(parse_xml('http://138.68.148.20/data/wales/swansea'))
    stop = timeit.default_timer()
    print(stop - start)
# assert_equal(parse_xml('http://138.68.148.20/data/wales/swansea'), {'amount_of_records': 1700, 'first_business': '360 Beach and Watersports Centre'})