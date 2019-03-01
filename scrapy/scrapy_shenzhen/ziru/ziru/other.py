from img2num import img2num
import os
import requests

#filepath = 'D:\\ziru\\full\\111.jpg'
#filepath = 'D:\\ziru\\full\\11111.png'

url = 'http://static8.ziroom.com/phoenix/pc/images/price/6b8a3fdb72f557032810e060e3cd52b3s.png'

r = requests.get(url)
#r.raise_for_status()
with open('D:\\ziru\\full\\cza.png',"wb") as f:
    f.write(r.content)

list = img2num('D:\\ziru\\full\\cza.png')

print(list)