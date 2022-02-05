# ex17_11.py
from wordcloud import WordCloud

with open("text17_28.txt") as fp:   # 英文字的文字檔
    txt = fp.read()                 # 讀取檔案
    
wd = WordCloud(background_color="white").generate(txt)      
imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔      
imageCloud.show()                   # 顯示詞雲影像檔








