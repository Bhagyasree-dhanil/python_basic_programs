"""
install required packages

pip install PyQRCode
pip install pypng

"""
# creating QRcode
import pyqrcode
import png
link = "https://instagram.com/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png",scale=5)

# Decode  a QRCode

"""
pip install pyzbar
pip install pillow

"""

from pyzbar.pyzbar import decode
from PIL import Image
decodeQR = decode(Image.open("instagram.png"))
print(decodeQR[0].data.decode('ascii'))

