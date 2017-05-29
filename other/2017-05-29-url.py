# encoding:UTF-8
import urllib.request

url = input("Input a URL pls.http://kangjian.net")
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)