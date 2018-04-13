import requests, json
from lxml import etree
from setting import INFO_URL, API_URL, HEADERS,HEADER
from HandleData import handle
from wordcloud import  STOPWORDS
from setting import STOPWORD_NEW
import time


class Spider(object):
    """构造请求头信息！"""
    url = API_URL
    headers = HEADERS
    parameters = {
        "city": "深圳",
        'needAddtionalResult': 'false'
    }
    # 提交表单数据
    data = {
        'first': 'true',
        'pn':1,
        'kd': '爬虫工程师'
    }

    @classmethod
    def run(cls):
        response = requests.post(cls.url, params=cls.parameters, data=cls.data, headers=cls.headers)
        data = response.content.decode('utf-8')
        dict_data = json.loads(data)
        pamare = dict_data['content']["positionResult"]['result']
        # print(len(pamare))
        # print(pamare)
        for i in pamare:
            a = i["positionId"]
            url = INFO_URL % a
            # print(url)
            time.sleep(1)
            response = requests.get(url, headers = HEADER )
            html = response.text
            print(type(html))
            print('---1---')
            obj_xpath = etree.HTML(html)
            node = obj_xpath.xpath("//dd[@class='job_bt']")
            info_node = node[0]
            info_text = info_node.xpath("string(.)").strip()
            with open('info.txt', 'a', encoding='utf-8') as f:
                f.write(info_text+'\n')
        handle('info.txt',STOPWORDS | STOPWORD_NEW)

if __name__ == '__main__':
    Spider.run()





