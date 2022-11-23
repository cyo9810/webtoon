import bs4
from bs4 import BeautifulSoup 
import requests

def scrape_weather():
    print("[오늘의 날씨]")
    
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9C%A8+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EC%9D%98%EB%82%A0%EC%94%A8&tqi=hozkfsp0YidssFe4f10ssssssil-235188"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    cast = soup.find("p",attrs={"class":"summary"}).get_text()
    s_list = soup.find("dl",attrs={"class":"summary_list"}).get_text()
    chart_list = soup.find("ul",attrs={"class":"today_chart_list"}).get_text()

    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("도씨","")
    
    """"""
    print(curr_temp)
    print(cast)
    print(s_list)
    print(chart_list)
    """"""
    
    weather = []
    cast = cast.split(' ')
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
        
    except IndexError:
        pass
    return weather

    
if __name__ == "__main__":
    scrape_weather() 