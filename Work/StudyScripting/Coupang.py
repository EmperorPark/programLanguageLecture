import requests
from bs4 import BeautifulSoup
import time

import json

def web_request(method_name, url, dict_data, is_urlencoded=True):
    """Web GET or POST request를 호출 후 그 결과를 dict형으로 반환 """
    method_name = method_name.upper() # 메소드이름을 대문자로 바꾼다 
    if method_name not in ('GET', 'POST'):
        raise Exception('method_name is GET or POST plz...')
        
    if method_name == 'GET': # GET방식인 경우
        response = requests.get(url=url, params=dict_data)
    elif method_name == 'POST': # POST방식인 경우
        if is_urlencoded is True:
            response = requests.post(url=url, data=dict_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        else:
            response = requests.post(url=url, data=json.dumps(dict_data), headers={'Content-Type': 'application/json'})
    
    dict_meta = {'status_code':response.status_code, 'ok':response.ok, 'encoding':response.encoding, 'Content-Type': response.headers['Content-Type']}
    if 'json' in str(response.headers['Content-Type']): # JSON 형태인 경우
        return {**dict_meta, **response.json()}
    elif 'text/html' in str(response.headers['Content-Type']): # HTML
        return response.content
    else: # 문자열 형태인 경우
        return {**dict_meta, **{'text':response.text}}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}


keywords = ['iphone', '12', 'pro']
#keywords = ['iphone', '12', 'mini']
trans = []

for keyword in keywords:
    url = "http://kornorms.korean.go.kr/example/exampleList.do?regltn_code=0003"
    data = {'example_no':'',
    'example_search_list[0].searchCondition':'srclang_mark',
    'example_search_list[0].searchEquals':'equal',
    'example_search_list[0].searchKeyword':keyword,
    'allCheck1':'all',
    's_foreign_gubun':'0001',
    's_foreign_gubun':'0002',
    's_foreign_gubun':'0003',
    '_s_foreign_gubun':'on',
    's_guk_nm':'',
    's_lang_nm':'',
    'pageUnit':'10',
    'pageIndex':'1' }
    response = web_request(method_name='POST', url=url, dict_data=data)
    soup_obj = BeautifulSoup(response, "html.parser")
    table = soup_obj.findAll("table", {"class": "tableList01"})
    a = table[0].findAll("a", {"class": "korean"})
    if len(a) > 0:
        trans.append(a[0].text)
        trans.append(keyword)
    else:
        trans.append(keyword)
    


# 휴대폰 - 쿠팡랭킹순 모든 상품,가격 가져오기
for idx in range(1, 6):
    time.sleep(2)
    url = "https://www.coupang.com/np/categories/490103?page=" + str(idx)

    print(url)
    result = requests.get(url, headers=headers)
    with open('Coupang/result.html', 'w') as file_handle:
        file_handle.write(str(result.content))
    soup_obj = BeautifulSoup(result.content, "html.parser")
    div = soup_obj.findAll("div", {"class": "name"})
    lis = soup_obj.find("ul", {"id": "productList"}).findAll("li")

    for li in lis:
        product = li.find("div", {"class": "name"})
        em = li.find("em", {"class": "sale"})
        priceStr = ''
        if em != None:
            price = em.find(
                "strong", {"class": "price-value"}
            )
            priceStr = price.text.strip()
        
        if any(word in product.text.strip() for word in trans):
            print("상품명: " + product.text.strip() + " / " + "상품가격: " + priceStr)









## 참고
# enumerate 내장함수 사용하여 Index 출력할 경우
# price_list = list(enumerate(strong))
# for idx, var in enumerate(0):
#     print(idx, var)

# for idx, var in enumerate(strong):
#     print(idx, var)

# CSS를 활용해 select로 찾는 방법
# strong = soup_obj.select(
#     "li > a > dl > dd > div.price-area > div > div.price > em.sale > strong"
# )