import requests
from bs4 import BeautifulSoup

# 저장할 파일을 열고, 검색어를 파일명으로 합니다.
with open('SSAFY.txt', 'w', encoding='utf-8') as f:
    # 1페이지부터 10페이지까지 반복합니다.
    for i in range(1, 11):
        # 페이지 주소를 설정합니다.
        url = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query=SSAFY&start={i}1"
        
        # 해당 웹페이지를 requests를 이용해 가져옵니다.
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 기사 제목이 담긴 a 태그를 모두 찾습니다.
        titles = soup.select('a.news_tit')
        
        # 각 기사 제목을 파일에 씁니다. 
        for title in titles:
            f.write(title.get_text() + '\n')
