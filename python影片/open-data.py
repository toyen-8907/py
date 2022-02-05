# 下載特定網址資料
# import urllib.request as request
# with request.urlopen as response:
#    data = response.read()


# 尋找適合的資料 有意義的(台北市政府公開資料)
# 確認資料格式 json,csv or others  解讀json 用內建的json模組

# 網路連線
'''
import urllib.request as request
src = "https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8")
print(data)
'''
# 串接、截取公開資料
import urllib.request as request
import json  # json檔案讀取要 import
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)  # 利用json模組  處理json資料格式

# 將公司名稱列表出來
clist = data["result"]["results"]
'''
for company in clist:
    print(company["公司名稱"])
'''
with open("dada.txt", mode="w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"] + "\n")
