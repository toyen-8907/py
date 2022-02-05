# 抓取網頁原始碼(HTML)

import urllib.request as req


def getdata(url):
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44"

    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 解析原始碼 ， 取得每篇文章的標題
    import bs4
    # 用 beautifulsoup4 來解析 html 資料
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")  # 尋找class = "title" 的 div 標籤
    for title in titles:
        if title.a != None:  # 如果標題包含 a 標籤(沒有被刪除) 印出來
            print(title.a.string)
    nextlink = root.find("a", string="‹ 上頁")
    return nextlink["href"]


a = "https://www.ptt.cc/bbs/Gossiping/index.html"
getdata(a)
count = 0
while count < 3:
    a = "https://www.ptt.cc" + getdata(a)
    count += 1
