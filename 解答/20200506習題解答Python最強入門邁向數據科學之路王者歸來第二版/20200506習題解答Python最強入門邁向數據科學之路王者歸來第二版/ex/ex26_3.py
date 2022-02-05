# ex26_3.py
import requests

url = 'http://www.olemiss.edu'
htmlfile = requests.get(url)
print(htmlfile.text)




