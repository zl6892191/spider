import requests, json,random
from lxml import etree
from setting import INFO_URL, API_URL, HEADERS,HEADERSS,re_redis
from HandleData import handle
from wordcloud import  STOPWORDS
from setting import STOPWORD_NEW
import re,os
from test1 import creat_proxy
import threading


class Spider(object):
    """构造请求头信息！"""
    url = API_URL
    parameters = {
        "city": "深圳",
        'needAddtionalResult': 'false'
    }

    pattern = re.compile(r'[\u4e00-\u9fa5]+|')

    @classmethod
    def gett(cls):
        azo = os.listdir('./')
        if 'info.png' in azo or 'info.txt' in azo:
            os.remove('./info.png')
            os.remove('./info.txt')
        # 拿到页面额详情页列表
        for j in range(0,5):
            j+=1
            # 提交表单数据
            if j==1:
                # 提交表单数据
                data = {
                    'first': 'true',
                    'pn': j,
                    'kd': '爬虫工程师'
                }
            else:
                data = {
                'first': 'false',
                'pn': j,
                'kd': '爬虫工程师'
            }
            response = requests.post(cls.url, params=cls.parameters, data=data, headers=HEADERS)
            data = response.content.decode('utf-8')
            dict_data = json.loads(data)
            pamare = dict_data['content']["positionResult"]['result']
            # 遍历详情列表并拼接
            for b in pamare:
                a = b["positionId"]
                url = INFO_URL % a
            # 存入redis 数据库
                pipeline = re_redis.pipeline()
                try:
                    pipeline.multi()
                    re_redis.lpush('lagou_xiangqing_url', url)
                except Exception as e:
                    print(e)
                    print('存入数据库失败!')
                    pipeline.execute()

    @classmethod
    def run(cls):
        # time.sleep(3)
        # 从数据库拿取
        num = re_redis.llen('lagou_xiangqing_url')
        for i in range(0,num):
            url = re_redis.lpop('lagou_xiangqing_url')
            response = requests.get(url, headers = HEADERSS,proxies=creat_proxy())
            html = response.text
            print('---1---')
            obj_xpath = etree.HTML(html)
            # 公司详情
            node = obj_xpath.xpath("//dd[@class='job_bt']")[0]
            # 公司名字
            node1 = obj_xpath.xpath('//*[@id="job_company"]/dt/a/div/h2/text()')[0]
            # 公司地址
            node2 = obj_xpath.xpath('//*[@id="job_detail"]/dd[3]/div[1]')[0]
            print(node1)
            # print(node2)
            info_text = node.xpath("string(.)").strip()
            # info_text1 = node1.xpath().strip()
            info_text2 = node2.xpath("string(.)").strip()
            info_text3 = cls.pattern.findall(info_text2)
            a = ''.join(info_text3)
            print(a)
            with open('info.txt', 'a', encoding='utf-8') as f:
                f.write(node1+'\n\n')
                f.write(a+'\n\n')
                f.write(info_text+'\n'+'================@@@@@@@================'+'\n\n')


t1 = threading.Thread(target=Spider.run())
t1.start()
t2 = threading.Thread(target=Spider.run())
t2.start()
t1.join()
t2.join()
if __name__ == '__main__':
    Spider.gett()
    Spider.run()
    handle('info.txt',STOPWORDS | STOPWORD_NEW)





