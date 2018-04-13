import random
from headers import headers_url


# 随机获取User-Agent
headers = random.choice(headers_url)

# 请求json的url
API_URL = "https://www.lagou.com/jobs/positionAjax.json"

# 爬取职位要求的url
INFO_URL = "https://www.lagou.com/jobs/%s.html"

# 请求json文件用的headers
HEADERS = {
    "User-Agent": headers,
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88?px=default&city=%E6%B7%B1%E5%9C%B3&district=%E5%8D%97%E5%B1%B1%E5%8C%BA",
    "X-Requested-With": "XMLHttpRequest",
    "Host": "www.lagou.com",
    "Connection": "keep-alive",
    "Origin": "https://www.lagou.com",
    "Upgrade-Insecure-Requests": "1",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8"
}

# 爬取职位要求的header
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
}

# 新加停用词
STOPWORD_NEW = {'公司', '团队', '介绍', '使用', '岗位职责', '就是', '不是', '回复', '以上', '设计', '任职', '要求', '职位', '描述', '技能', ' 岗位', '职责', '工作', '资格', '优先', '能力', '工作'}