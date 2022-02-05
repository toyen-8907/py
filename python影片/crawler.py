# 抓取網頁原始碼(HTML)
import bs4
import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url, headers={
   
    "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
})
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")

# 解析原始碼 ， 取得每篇文章的標題
root = bs4.BeautifulSoup(data, "html.parser")  # 用 beautifulsoup4 來解析 html 資料
titles = root.find_all("div", class_="title")  # 尋找class = "title" 的 div 標籤
print(titles.a.string)
for title in titles:
    if title.a != None:  # 如果標題包含 a 標籤(沒有被刪除) 印出來
        print(title.a.string)
