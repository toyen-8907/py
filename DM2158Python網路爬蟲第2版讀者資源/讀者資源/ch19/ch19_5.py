# ch19_5.py
import facebook

token = "EAAIZCihE7RSkBAKGOOmFqV2ZAsYwwDN1TizKjJZApI8DTJeD68Tgv6zZBisL6urRixy2Ikw9FIG5PhbYeXLXVwQCpLuZB8mRv2wr4N5iDBDMPZCZCDToPLqjjxPY7zqxCFnYCtwBhFXQ7yX3Dch4ZBSm6nt5GZCbc1Vw8KrkgBgpQhJt9JE3BbWZA3V5F40nBqyBV3vxFNxHscs6boNa6cAbZBt"
graph = facebook.GraphAPI(access_token=token, version='3.1')

mypost = graph.get_object(id='1116138285252667_1792295917636897?fields=message')
print("列出發文資料內容 : ", mypost)
print("發文內容 : ", mypost['message'])














