import requests,random
from setting import proxy_url,header_proxy


def creat_proxy():
    data = {
            'spm':'a1z09.3.0.0.30ea4a7fHgaaZ3',
            'text':'true',
            'noinfo':'true',
            'sl':3,
            'ddbh':148610782044530917
    }
    proxie = requests.get(proxy_url,params=data, headers = header_proxy)
    url_list=proxie.content.decode('utf-8')
    url_dict = url_list.split()
    suiji_proxy = 'http://'+random.choice(url_dict)
    aaa = {'http':suiji_proxy}
    return aaa



