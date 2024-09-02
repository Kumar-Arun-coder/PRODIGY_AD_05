import pyqrcode
import png
from pyqrcode import QRCode

link=str(input("enter the website name:"))
url=pyqrcode.create(link)
url.png(link[4:-4]+".png",scale=6)