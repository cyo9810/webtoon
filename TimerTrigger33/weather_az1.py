import bs4
from bs4 import BeautifulSoup 
import requests

def scrape_weather():
    print("[오늘의 인기 웹툰 순위]")
    
    url = "https://comic.naver.com/webtoon/weekday"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    s=[]
    count =0
    for li in soup.find('ol',{'class':'asideBoxRank'}).find_all('li'):
        count+=1
        print(count,li.a.text)
        s.append(li.a.text)
    return s

    
    weather = []
    cast = cast.split('\n')
    s_list = s_list.split()
    chart_list = chart_list.split()
    weather1={}
    try:
        
        
        weather.append(curr_temp)
        #weather.append(cast)
        weather.extend(s_list)
        weather.extend(chart_list)
        # weather.append(s_list)
        # weather.append(chart_list)
        weather.append(rank5)
        weather.append(rank6)
        weather.append(rank7)
        weather.append(rank8)
        weather.append(rank9)
        weather.append(rank10)
        
    except IndexError:
        pass
    return weather

    
if __name__ == "__main__":
    scrape_weather() 