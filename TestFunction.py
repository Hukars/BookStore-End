import re
import time

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