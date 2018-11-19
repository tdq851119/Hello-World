# -* - coding:gbk -* -
"""
Auther:   tong
Date:     2018-11-19
Language: Python 2.7
"""

import urllib2,requests
import urllib,json

# request = urllib2.Request("http://passport.cnblogs.com/login.aspx")
# request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
# data={"tbUserName":"test_username", "tbPassword":"test_password"}
#
# response = urllib2.urlopen(request, urllib.urlencode(data))
# print response.getcode()
# print response.geturl()
# print response.read()

def test1():
    url = "http://passport.cnblogs.com/login.aspx"
    header = {"Content-Type":"application/json"}
    body = {"tbUserName":"test_username", "tbPassword":"test_password"}
    response = requests.post(url,data = json.dumps(body))
    print  response.text,'\n'#,response.content
    print  '\n',response.status_code,'\n',response.reason,'\n',response.url,'\n',response.raw
    print response
test1()

#
# def test():
#     url = "http://172.24.7.186:22001/com.jd.jr.baitiao.outside.export.ZshResource/bt-outside-test/takeZsh/113812"
#     header = {"Content-Type":"application/json"}
#     body = {}
#     response = requests.post(url,data = json.dumps(body))
#     print  response.text,'\n',response.content,'\n',response.status_code,'\n',response.reason,response.url,'\n',response.raw
#     print response
# test()

request = urllib2.Request("http://172.24.7.186:22001/com.jd.jr.baitiao.outside.export.ZshResource/bt-outside-test/takeZsh/113812")
request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
data={"tbUserName":"test_username", "tbPassword":"test_password"}

response = urllib2.urlopen(request, urllib.urlencode(data))
print response.getcode()
print response.geturl()
print response.read() 
