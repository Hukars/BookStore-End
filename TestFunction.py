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


def splitPictureURL(image_url):
    """
    以逗号为分隔符切割图片URL，转化为一个数组
    """
    images = image_url.split('jpg,')
    finalImages = []
    for e in images:
        if 'jpg' not in e:
            e += 'jpg'
            finalImages.append(e)
        else:
            finalImages.append(e)
    print(finalImages)
    return finalImages

splitPictureURL('https://images-cn.ssl-images-amazon.com/images/I/51kxMQVKCwL._SX325_BO1,204,203,200_.jpg,https://images-cn.ssl-images-amazon.com/images/I/51QIzxaHz8L._AC_SX60_CR,0,0,60,60_.jpg')