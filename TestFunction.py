import re
import time
import http.client,urllib.parse

def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            print('good')
            # return 1
    # return 0
    print('exit')

def validateEmail1(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            print('ok')
    print('gg')


validateEmail1("2@q.c")


requestDict = {'ids':[1,2]}
cartItemsIds = requestDict['ids']
for e in cartItemsIds:
    #e = re.sub("\D", "", e)
    print(int(e))


data={
    'adminId': 1,
    'password': 'hukars',
    'ruleId':6,
    'ruleDetail':'hhhhhhhhhh'
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/helps/rules/add/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)