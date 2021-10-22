import requests
import serial
import time
from bs4 import BeautifulSoup

s = serial.Serial('COM2','9600') #Enter Arduino Port Number Here

price =[63,425.50]

while (True):
  url = 'https://www.google.com/search?&q=bitcoin price in america'
  req = requests.get(url)
  scrap = BeautifulSoup(req.text, 'html.parser')
  bitcoin_price = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
  a = bitcoin_price.split()
  b = a[0]
  print(b)
  price.append(b)
  size = len(price)
  if (price[len(price)-2]!=price[len(price)-1]):
    s.write("H".encode())
    time.sleep(1)
    s.write("L".encode())
    time.sleep(1)

  else:
    print("")
  
  