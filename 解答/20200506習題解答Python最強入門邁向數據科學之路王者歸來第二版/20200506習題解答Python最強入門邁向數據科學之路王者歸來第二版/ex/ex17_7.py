# ex17_7.py
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=5,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data("http://www.mcut.edu.tw")
img = qr.make_image(fill_color='blue')
width, height = img.size            # QR code的寬與高
with Image.open('logo17_7.jpg') as obj:
    obj_width, obj_height = obj.size
    img.paste(obj, ((width-obj_width)//2, (height-obj_height)//2))
img.save("fig17_7.jpg")




