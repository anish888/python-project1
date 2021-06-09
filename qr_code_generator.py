#pyqrcode is a module which is used to generating qrcode
import pyqrcode 

from pyqrcode import QRCode 
  
# link of the String which represent the QR code 
s = "https://www.youtube.com/" 
#taking user from the input
#s=input(" enter the link which you want to generate the qrcode")
  
# url used for  Generating the  QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.svg"
# scale for taking the size of the qrcode 
url.svg("myqr.svg", scale = 6) 