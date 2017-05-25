# _*_ coding: utf-8 _*_

"""
python_spider.py by xianhu
"""

import urllib.error
import urllib.parse
import urllib.request
import http.cookiejar

# ���ȶ����±߿�����Ҫ�ı���
url = "https://www.baidu.com"
headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}

# ��򵥵���ҳץȡ��ʽ
response = urllib.request.urlopen(url, timeout=10)
html = response.read().decode("utf-8")


# ʹ��Requestʵ������url
request = urllib.request.Request(url, data=None, headers={})
response = urllib.request.urlopen(request, timeout=10)


# �������ݣ�����Request()�����data����
data = urllib.parse.urlencode({"act": "login", "email": "xianhu@qq.com", "password": "123456"})
request1 = urllib.request.Request(url, data=data)           # POST����
request2 = urllib.request.Request(url+"?%s" % data)         # GET����
response = urllib.request.urlopen(request, timeout=10)


# ����Header������Request()�����headers����
request = urllib.request.Request(url, data=data, headers=headers)   # ���������header����
request.add_header("Referer", "http://www.baidu.com")               # ��һ�����header�ķ�ʽ,���Referer��Ϊ��Ӧ��"������"
response = urllib.request.urlopen(request, timeout=10)


# ��ҳץȡ�����쳣��urllib.error.HTTPError, urllib.error.URLError, ���ߴ��ڼ̳й�ϵ
try:
    urllib.request.urlopen(request, timeout=10)
except urllib.error.HTTPError as e:
    print(e.code, e.reason)
except urllib.error.URLError as e:
    print(e.errno, e.reason)


# ʹ�ô����Է�ֹIP�����IP�������ޣ�
proxy_handler = urllib.request.ProxyHandler(proxies={"http": "111.123.76.12:8080"})

opener = urllib.request.build_opener(proxy_handler)     # ���ô�����openerʵ��
response = opener.open(url)                             # ֱ������openerʵ����url

urllib.request.install_opener(opener)                   # ��װȫ��opener��Ȼ������urlopen��url
response = urllib.request.urlopen(url)


# ʹ��cookie��cookiejar,Ӧ�Է��������
cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)
response = opener.open(url)


# ������������л�ȡ��cookie,���ַ�ʽ:
# (1)ֱ�ӷŵ�headers��
headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Cookie": "PHPSESSID=btqkg9amjrtoeev8coq0m78396; USERINFO=n6nxTHTY%2BJA39z6CpNB4eKN8f0KsYLjAQTwPe%2BhLHLruEbjaeh4ulhWAS5RysUM%2B; "
}
request = urllib.request.Request(url, headers=headers)

# (2)����cookie,��ӵ�cookiejar��
cookie = http.cookiejar.Cookie(name="xx", value="xx", domain="xx", ...)
cookie_jar.set_cookie(cookie)
response = opener.open(url)


# ͬʱʹ�ô����cookiejar
opener = urllib.request.build_opener(cookie_jar_handler)
opener.add_handler(proxy_handler)
response = opener.open("https://www.baidu.com/")


# ץȡ��ҳ�е�ͼƬ��ͬ��������ץȡ�����ϵ��ļ����һ���꣬�ҵ�ͼƬ�����еĵ�ַ��Ȼ����б��档
response = urllib.request.urlopen("http://ww3.sinaimg.cn/large/7d742c99tw1ee7dac2766j204q04qmxq.jpg", timeout=120)
with open("test.jpg", "wb") as file_img:
    file_img.write(response.read())


# HTTP��֤����HTTP�����֤
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()     # ����һ��PasswordMgr
password_mgr.add_password(realm=None, uri=url, user='username', passwd='password')   # ����û���������
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)         # ����HTTPBasicAuthHandler
opener = urllib.request.build_opener(handler)                       # ����opner
response = opener.open(url, timeout=10)                             # ��ȡ����
