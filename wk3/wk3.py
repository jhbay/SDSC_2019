import requests
import json
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from nose.tools import assert_equal, assert_raises
# from pymongo import MongoClient


# try:
#     imports = [requests, BeautifulSoup, RobotFileParser, assert_equal, assert_raises, json
#     # , MongoClient
#     ]
# except NameError as e:
#     print(e)
#     raise AssertionError('You appear to be missing one of the required libraries or functions')
# assert True
# print('Successfully imported libraries and functions')

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

html = """
    <div id="main" class="classy">
        <h1>The Main Content of the Document</h1>
        
        <p>This is some content inside a &lt;p&gt; tag.  It is normal writing.  It can contain other tags
        within it.  For example, to emphasise a word I would use <em>the &lt;em&gt; tag</em>, or to move
        onto a new ine I could use the &lt;br /&gt; tag.
        </p>
        
        <table>
            <tr>
                <th>Table heading cell</th><th>Another heading</th>
            </tr>
            <tr>
                <td>Normal table cell</td><td>This cell has a link going <a href="#">Somewhere</a></td>
            </tr>
        </table>
    
    </div>
"""

def checkUrlStatus(url):
    try:
        statusCode = str(requestUrl(url).status_code)
        print("checkUrlStatus :: " + statusCode) 
        return statusCode
    except NotImplementedError as e:
        # print(e)
        raise NotImplementedError()
    
# checkUrlStatus('http://138.68.148.20/data/west_midlands/cannock_chase') #Valid 200
# checkUrlStatus('http://138.68.148.20/west_midlands/cannock_chase') # None

def checkParsableUrl(code):
    # only request valid - 200
    if(code == '200' or code == 'True' or code == True):
        return True
    # else : False
    return None

def beautifulSoupParseXml(url):
    try:
        retDict = {}
        soup = BeautifulSoup(requestUrlXmlType(url), 'xml') 
        # print("first_business :: "  + str(soup.findAll('EstablishmentDetail')[0].find('BusinessName').string) )
        # print("amount_of_records :: "  + str(soup.find('ItemCount').string))
        retDict["first_business"] = str(soup.findAll('EstablishmentDetail')[0].find('BusinessName').string)
        retDict["amount_of_records"] = int(soup.find('ItemCount').string)
        print("parse_xml retDict::" + str(retDict) )
        return retDict
    except NotImplementedError as e:
        # print(e)
        raise NotImplementedError()

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
    if(checkParsableUrl(check_robots(url))):
        print("robotStatus parsable :: " + str(checkParsableUrl(check_robots(url))))
        
        if(checkParsableUrl(checkUrlStatus(url))):
            print("reqStatus parsable :: " + str(checkParsableUrl(checkUrlStatus(url))))
            retDict = beautifulSoupParseXml(url)
        else:
            print('Result: None')
            retDict = None 
    else:
        print('Result: None')
        retDict = None 
    return retDict


def quiz1c():
    parse_xml("http://138.68.148.20/data/west_midlands/cannock_chase")
    # parse_xml("http://138.68.148.20/data/scotland/clackmannanshire")  
    del requests 
    parse_xml('http://138.68.148.20/data/scotland/glasgow_city')
    parse_xml('http://138.68.148.20/data/scotland/clackmannanshire')
    #assert
    parse_xml('http://138.68.148.20/data/west_midlands/cannock_chase')
    parse_xml('http://138.68.148.20/data/wales/swansea')
    parse_xml('http://138.68.148.20/data/calderdale') # None.








# quiz1a();
# quiz1b()
quiz1c()












