import random
from redis import StrictRedis
from headers import headers_url


# 随机获取User-Agent
headers = random.choice(headers_url)

# 代理池地址
proxy_url = 'http://proxy.httpdaili.com/api.asp?'

# 代理请求头
header_proxy = {
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding':'gzip, deflate',
                    'Accept-Language':'zh-CN,zh;q=0.9',
                    'Cache-Control':'max-age=0',
                    'Connection':'keep-alive',
                    'Cookie':'UM_distinctid=162c87237d817e-058b36ed072e94-3b604b0a-149c48-162c87237d979c; ASPSESSIONIDASBRACTC=NBHHNPOAJNOCNJABGCKHLIEN',
                    'Host':'proxy.httpdaili.com',
                    'Upgrade-Insecure-Requests':'1',
                    'User-Agent':headers
                }

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

HEADERSS = {
        'User-Agent':headers,
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'_ga=GA1.2.844227049.1513435019; user_trace_token=20171216223659-92c9a9d5-e26e-11e7-9cb4-525400f775ce; LGUID=20171216223659-92c9afb1-e26e-11e7-9cb4-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; LG_LOGIN_USER_ID=2be0999abcadea15f4eb8f4341fadb97fba7658af2934faf; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; WEBTJ-ID=20180414093335-162c1c943643b5-0f79c928603f7b-3b604b0a-1350728-162c1c94368a00; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523346633,1523368358,1523627778,1523669616; LGSID=20180414093339-dbba048b-3f83-11e8-b838-5254005c3644; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.0s0000KlmKuCTsdU2X-kJ-IqO471zq1j8qoOJ77hqDq4VRVA-elHMOSIQcakZa4s51SNF9m8qUDf_ijVW4lk9AR8wNv0bGPwJqGUa-_wLwnCOCrCzeAC3c3MknvsPcQF2HLCjmKOpmnOf-Ge6b7bJ_HSAwms7ZAGVniUyvYvLryZupt-ws.DR_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzkt52h881gE4TMH8Hgo4T5MY3IMo9vUt5MEsethZvedPHV2XgZJyAp7BEuuEv20.U1Yk0ZDqs2v4_sK9uZ745TaV8Un0mywkIjYz0ZKGm1Yk0Zfqs2v4_sKGUHYznWR0u1dBUW0s0ZNG5yF9pywd0ZKGujYY0APGujY4nsKVIjY1nHnvg1DsnHIxnH0krNtznjmzg1DsnWPxn1msnfKopHYs0ZFY5HfsnsK-pyfqnHfYrNtznH0LrNtznjm4n6KBpHYznjf0UynqnHRvg1T1njDYP1m4PdtLn10kPjTLnjKxn1nvnW63PW63P7tkg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjY4PjT3nWDLPWT0UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0ZwdT1YknjckrH61PjTknHT4Pjc4PHRsPfKzug7Y5HDdnWnvPWbvnHcvrj00Tv-b5H9Bn1Fbnyn1nj0snWc4n1R0mLPV5HFKPDPKwW03f1uarHTvwH60mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg1Kxn0Ksmgwxuhk9u1Ys0AwWpyfqnWm3PjndPjRv0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqnHm0uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00mLFW5Hb4nHn%26ck%3D4409.1.80.305.150.304.158.228%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.302.0%26wd%3D%25E6%258B%2589%25E9%2592%25A9%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D669%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_sz_e110f9_265e1f_%25E6%258B%2589%25E9%2592%25A9; _putrc=63695F86C56DE12D; JSESSIONID=ABAAABAAAGGABCBAE3C3B2FF38F0DD7FEAC3CFAD3B96439; login=true; unick=%E5%8D%93%E6%9E%97; gate_login_token=8606e8c02048f49d76129cea76f8ab83d136bb368a346175; TG-TRACK-CODE=index_search; SEARCH_ID=5925f281733541c1a9655edb8d320d9b; _gat=1; LGRID=20180414094832-efe57ec7-3f85-11e8-82cb-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523670513',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=',
        'Upgrade-Insecure-Requests':'1'
}

# 爬取职位要求的header
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
}

# 新加停用词
STOPWORD_NEW = {'良好','以上学历','工作','职位','公司', '团队', '介绍', '使用', '岗位职责', '就是', '不是', '回复', '以上', '设计', '任职', '要求', '职位', '描述', '技能', ' 岗位', '职责', '工作', '资格', '优先', '能力', '工作'}

# 链接redris

re_redis = StrictRedis(host='192.168.44.160',port=6379)