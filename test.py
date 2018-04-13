import random,time,json
from headers import headers_url
import requests
from lxml import etree


aconnt = random.choice(headers_url)

# 设置请求头
header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'22',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'m.youdao.com',
        'Origin':'https://m.youdao.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':aconnt
        }

# 请求地址
url = 'https://m.youdao.com/translate'

# 拼接时间戳
time_key = 'translate_uuid' + str(int(time.time() * 1000))

# 提交数据
data = {

    'type':'AUTO',
    'inputtext':input('请输入你要翻译的内容：'),

       }

def translate():
    # 组织发送体
    reponse = requests.post(url,data = data,headers = header)
    print(reponse)
    html = reponse.text
    obj_xpath = etree.HTML(html)
    node = obj_xpath.xpath('//*[@id="translateResult"]/li/text()')
    print(header.get('User-Agent'))
    print('翻译的内容为：{0}'.format(node))
if __name__ == '__main__':
    translate()